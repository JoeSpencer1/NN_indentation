from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import KFold, LeaveOneOut, RepeatedKFold, ShuffleSplit, StratifiedKFold

import deepxde as dde
from data import FileData
import tensorflow as tf
tf.config.run_functions_eagerly(False)
import os
import multiprocessing
dde.backend.set_default_backend("tensorflow.compat.v1")
dde.backend.tf.Session()

global apeG, yG

def svm(data):
    clf = SVR(kernel='rbf')
    clf.fit(data.train_x, data.train_y[:, 0])
    y_pred = clf.predict(data.test_x)[:, None]
    return dde.metrics.get('MAPE')(data.test_y, y_pred)

def t2s(names):
    if type(names) is str:
        return names
    else:
        return '[' + ','.join(names) + ']'

import deepxde as dde
    
def nn(data, lay, wid):
    #lay, wid = 2, 32
    layer_size = [data.train_x.shape[1]] + [wid] * lay + [1]
    activation = 'selu'
    initializer = 'LeCun normal'
    regularization = ['l2', 0.01]
    
    loss = 'MAPE'
    optimizer = 'adam'
    lr = 0.0001 if data.train_x.shape[1] == 3 else 0.001
    epochs = 30000
    net = dde.maps.FNN(
        layer_size, activation, initializer, regularization=regularization
    )
    model = dde.Model(data, net)
    model.compile(optimizer, lr=lr, loss=loss, metrics=['MAPE'])
    losshistory, train_state = model.train(epochs=epochs)
    dde.saveplot(losshistory, train_state, issave=True, isplot=False)
    return train_state.best_metrics[0]

def mfnn(data, lay, wid, xdim):
    #lay, wid = 2, 128
    x_dim, y_dim = xdim, 1
    activation = 'selu'
    initializer = 'LeCun normal'
    regularization = ['l2', 0.01]
    net = dde.maps.MfNN(
        [x_dim] + [wid] * lay + [y_dim],
        [8] * lay + [y_dim],
        activation,
        initializer,
        regularization=regularization,
        residue=True,
        trainable_low_fidelity=True,
        trainable_high_fidelity=True
    )

    model = dde.Model(data, net)
    model.compile('adam', lr=0.0001, loss='MAPE', metrics=['MAPE', 'APE SD'])
    losshistory, train_state = model.train(epochs=30000)

    dde.saveplot(losshistory, train_state, issave=True, isplot=False)
    return (
        train_state.best_metrics[1],
        train_state.best_metrics[3],
        train_state.best_y[1],
    )

def validation_one(yname, testname, trainname, n_hi, n_vd=0.2, lay=2, wid=32):
    datatrain = FileData(trainname, yname)
    datatest = FileData(testname, yname)

    n_vd = int(n_vd * datatrain.X.shape[0]) if n_vd < 1 else int(n_vd)
    v_ind = np.random.choice(datatrain.X.shape[0], size=n_vd, replace=False)
    t_ind = np.setdiff1d(np.arange(datatrain.X.shape[0]), v_ind)
    dataval = FileData(testname, yname)
    dataval.X = datatrain.X[v_ind]
    dataval.y = datatrain.y[v_ind]
    datatrain.X = datatrain.X[t_ind]
    datatrain.y = datatrain.y[t_ind]

    kf = ShuffleSplit(
        n_splits=10, train_size=n_hi, test_size=len(datatrain.X) - n_hi, random_state=0
    )

    mape = []
    iter = 0
    for train_index, test_index in kf.split(datatest.X):
        iter += 1
        print('\nCross-validation iteration: {}'.format(iter))
        train_index = train_index * len(datatrain.X) // len(datatest.X)

        X_train, X_test = datatrain.X[train_index], datatest.X[test_index]
        y_train, y_test = datatrain.y[train_index], datatest.y[test_index]

        data = dde.data.DataSet(
            X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, standardize=True
        )
        mape.append(dde.utils.apply(nn, (data,lay,wid,)))

    print(mape)
    print(yname, n_hi, np.mean(mape), np.std(mape))
    with open('output.txt', 'a') as f:
        f.write('validation_one ' + yname + ' ' + f'{np.mean(mape):.2f}' + ' ' + f'{np.std(mape):.2f}' + ' ' + t2s(testname) + ' ' + t2s(trainname) + ' ' + str(n_hi) + ' ' + str(n_vd) + ' ' + str(lay) + ' ' + str(wid) + '\n')
    # return 'validation_one ' + yname + ' ' + f'{np.mean(mape):.2f}' + ' ' + f'{np.std(mape):.2f}' + ' ' + t2s(testname) + ' ' + t2s(trainname) + ' ' + str(n_hi) + ' ' + str(n_vd) + ' ' + str(lay) + ' ' + str(wid) + '\n'

def validation_two(yname, testname, trainhigh, n_hi, trainlow, n_lo, v_lo=0, n_vd=0.2, lay=2, wid=128):
    datalow = FileData(trainlow, yname)
    datahigh = FileData(trainhigh, yname)
    datatest = FileData(testname, yname)

    n_vd = int(n_vd * datahigh.X.shape[0]) if n_vd < 1 else int(n_vd)
    v_ind = np.random.choice(datahigh.X.shape[0], size=n_vd, replace=False)
    t_ind = np.setdiff1d(np.arange(datahigh.X.shape[0]), v_ind)
    dataval = FileData(testname, yname)
    dataval.X = datahigh.X[v_ind]
    dataval.y = datahigh.y[v_ind]
    datahigh.X = datahigh.X[t_ind]
    datahigh.y = datahigh.y[t_ind]

    datalow.y *= 1 + v_lo * np.random.normal(loc=0, scale=1, size=datalow.y.shape)

    mape = []
    iter = 0

    if n_hi == 0:
        kf = ShuffleSplit(
            n_splits=10, test_size=len(datalow.y) - n_lo, random_state=0
        )
        for train_index, test_index in kf.split(datatest.X):
            iter += 1
            print('\nCross-validation iteration: {}'.format(iter))
            train_index = train_index * len(datalow.X) // len(datatest.X)
            X_train, X_test = datalow.X[train_index], datatest.X[test_index]
            y_train, y_test = datalow.y[train_index], datatest.y[test_index]
            data = dde.data.DataSet(
                X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, standardize=True
            )
            mape.append(dde.utils.apply(nn, (data,lay,wid,)))

    else:
        kf = ShuffleSplit(
            n_splits=10, test_size=len(datahigh.y) - n_hi, random_state=0
        )
        for train_index, test_index in kf.split(datatest.X):
            iter += 1
            print('\nIteration: {}'.format(iter), flush=True)
            for i in range(len(train_index)):
                train_index[i] = train_index[i] * len(datahigh.y) // len(datatest.y)

            lo_index = np.random.choice(datalow.X.shape[0], size=n_lo, replace=False)
            data = dde.data.MfDataSet(
                X_lo_train=datalow.X[lo_index],
                X_hi_train=datahigh.X[train_index],
                y_lo_train=datalow.y[lo_index],
                y_hi_train=datahigh.y[train_index],
                X_hi_test=datatest.X[test_index],
                y_hi_test=datatest.y[test_index],
                standardize=True
            )
            mape.append(dde.utils.apply(mfnn, (data, lay, wid, 3, ))[0])

    with open('output.txt', 'a') as f:
        f.write('validation_two ' + yname + ' ' + f'{np.mean(mape, axis=0):.2f}' + ' ' + f'{np.std(mape, axis=0):.2f}' + ' ' + t2s(testname) + ' ' + t2s(trainhigh) + ' ' + str(n_hi) + ' ' + t2s(trainlow) + ' ' + str(n_lo) + ' ' + str(v_lo) + ' ' + str(n_vd) + ' ' + str(lay) + ' ' + str(wid) + '\n')
    print(np.std(mape))
    print(mape)
    print(yname, 'validation_two ', t2s(trainlow), ' ', t2s(trainhigh), ' ', str(n_hi), ' ', np.mean(mape), np.std(mape))

def validation_three(yname, testname, trainexp, n_exp, trainhigh, n_hi, trainlow, n_lo, typ='hi', n_vd=0.2, v_lo=0, v_hi=0, lay=2, wid=128):
    datalow = FileData(trainlow, yname)
    datahigh = FileData(trainhigh, yname)
    dataexp = FileData(trainexp, yname)
    datatest = FileData(testname, yname)

    n_vd = (int(n_vd * dataexp.X.shape[0])) if n_vd < 1 else int(n_vd)
    v_ind = np.random.choice(dataexp.X.shape[0], size=n_vd, replace=False)
    t_ind = np.setdiff1d(np.arange(dataexp.X.shape[0]), v_ind)
    dataval = FileData(testname, yname)
    dataval.X = dataexp.X[v_ind]
    dataval.y = dataexp.y[v_ind]
    dataexp.X = dataexp.X[t_ind]
    dataexp.y = dataexp.y[t_ind]

    datalow.y *= 1 + v_lo * np.random.normal(loc=0, scale=1, size=datalow.y.shape)
    datahigh.y *= 1 + v_hi * np.random.normal(loc=0, scale=1, size=datahigh.y.shape)

    ape = []
    y = []

    if n_exp == 0:
        kf = ShuffleSplit(
            n_splits=10, train_size = n_hi, random_state=0
        )
        if typ == 'hi':
            for train_index, test_index in kf.split(datatest.X):
                iter += 1
                print('\nIteration: {}'.format(iter), flush=True)
                for i in range(len(train_index)):
                    train_index[i] = train_index[i] * len(datahigh.y) // len(datatest.y)
                lo_index = np.random.choice(datalow.X.shape[0], size=n_lo, replace=False)  
                data = dde.data.MfDataSet(
                    X_lo_train=datalow.X[lo_index],
                    X_hi_train=datahigh.X[train_index],
                    y_lo_train=datalow.y[lo_index],
                    y_hi_train=datahigh.y[train_index],
                    X_hi_test=datatest.X[test_index],
                    y_hi_test=datatest.y[test_index],
                    standardize=True
                )
                ape.append(dde.utils.apply(mfnn, (data, lay, wid, 3, ))[0])
        else:
            for train_index, test_index in kf.split(datatest.X):
                iter += 1
                print('\nCross-validation iteration: {}'.format(iter))
                lo_index = np.random.choice(datalow.X.shape[0], size=n_lo, replace=False)
                hi_index = np.random.choice(datahigh.X.shape[0], size=n_hi, replace=False)
                datatrain = datalow
                datatrain.X = np.vstack((datalow.X[lo_index], datahigh.X[hi_index]))
                datatrain.y = np.vstack((datalow.y[lo_index], datahigh.y[hi_index]))
                train_index = train_index * len(datatrain.X) // len(datatest.X)
                X_train, X_test = datatrain.X[train_index], datatest.X[test_index]
                y_train, y_test = datatrain.y[train_index], datatest.y[test_index]
                data = dde.data.DataSet(
                    X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, standardize=True
                )
                ape.append(dde.utils.apply(nn, (data,lay,wid,)))
    else:
        kf = ShuffleSplit(n_splits=10, train_size=n_exp, random_state=0)
        for train_index, _ in kf.split(dataexp.X):
            print('\nIteration: {}'.format(len(ape)))
            lo_index = np.random.choice(datalow.X.shape[0], size=n_lo, replace=False)
            hi_index = np.random.choice(datahigh.X.shape[0], size=n_hi, replace=False)
            if typ == 'hi':
                data = dde.data.MfDataSet(
                    X_lo_train=datalow.X[lo_index],
                    X_hi_train=np.vstack((datahigh.X[hi_index], dataexp.X[train_index])),
                    y_lo_train=datalow.y[lo_index],
                    y_hi_train=np.vstack((datahigh.y[hi_index], dataexp.y[train_index])),
                    X_hi_test=datatest.X,
                    y_hi_test=datatest.y,
                    standardize=True
                )
            else:
                data = dde.data.MfDataSet(
                    X_lo_train=np.vstack((datalow.X[lo_index],datahigh.X[hi_index])),
                    X_hi_train=dataexp.X[train_index],
                    y_lo_train=np.vstack((datalow.y[lo_index],datahigh.y[hi_index])),
                    y_hi_train=dataexp.y[train_index],
                    X_hi_test=datatest.X,
                    y_hi_test=datatest.y,
                    standardize=True
                )
            res = dde.utils.apply(mfnn, (data, lay, wid, 3, ))
            ape.append(res[:2])
            y.append(res[2])

    with open('output.txt', 'a') as f:
        f.write('validation_three ' + yname + ' ' + f'{np.mean(ape, axis=0)[0]:.2f}' + ' ' + f'{np.std(ape, axis=0)[0]:.2f}' + ' ' + t2s(testname) + ' ' + t2s(trainexp) + ' ' + str(n_exp) + ' ' + t2s(trainhigh) + ' ' + str(n_hi) + ' ' + t2s(trainlow) + ' ' + str(n_lo) + ' ' + typ + ' ' + str(n_vd) + ' ' + str(v_hi) + ' ' + str(v_lo) + ' ' + str(lay) + ' ' + str(wid) + '\n')

def find_properties(yname, expname, train_hi, train_lo, lay=2, wid=128):
    datalow = FileData(train_lo, yname)
    datahigh = FileData(train_hi, yname)
    dataexp = FileData(expname, yname, new=True)

    ape = []
    y = []
    
    for _ in range(10):
        print("\nIteration: {}".format(len(ape)))

        data = dde.data.MfDataSet(
            X_lo_train=datalow.X,
            X_hi_train=datahigh.X,
            y_lo_train=datalow.y,
            y_hi_train=datahigh.y,
            X_hi_test=dataexp.X,
            y_hi_test=dataexp.y,
            standardize=True
        )
        if yname == 'n':
            data.y_lo_train *= 10
            data.y_hi_train *= 10
            res = dde.utils.apply(mfnn, (data,lay,wid,5,))
            y.append(res[2] / 10)
        elif yname == 's0.033':
            res = dde.utils.apply(mfnn, (data,lay,wid,5,))
            y.append(res[2])
        else:
            res = dde.utils.apply(mfnn, (data, lay, wid, 3,)) 
            y.append(res[2])
        ape.append(res[:2])

    print(np.mean(y, axis=0))
    print(np.std(y, axis=0))
    print(np.mean(np.mean(y, axis=0), axis=0))
    print(np.mean(np.std(y, axis=0), axis=0))

def main(argument=None):
    if argument != None:
        exec(argument)
    return

if __name__ == '__main__':
    main()