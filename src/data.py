from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import pandas as pd

class FileData(object):
    def __init__(self, filename, yname, new=False):
        
        self.filename = filename
        self.yname = yname
        self.new = new

        self.X = None
        self.y = None

        if type(self.filename) is tuple:
            for i in range(len(self.filename)):
                self.read(self.filename[i], self.new)

        else:
            self.read(self.filename, self.new)

    def read(self, name, new):
        df = pd.read_csv('../data/' + name + '.csv')

        # This is for Al alloys
        if 'Al7075' in name or 'Al6061' in name:
            df['dP/dh (N/m)'] *= 0.2 * (df['C (GPa)'] / 3) ** 0.5 * 10 ** (-1.5)
        # This is for Ti alloys
        if 'B3090' in name or 'B3067' in name:
            df['dP/dh (N/m)'] *= 0.2 / df['hmax(um)']
        # Scale TI33 to hm=0.2μm
        if 'TI33' in name or '2D' in name or '3D' in name:
            # For 25˚ case
            df['dP/dh (N/m)'] *= 0.2 / df['hmax(um)']
        # Scale from Conical to Berkovich with small deformations
        if 'FEM_70deg' in name:
            df['dP/dh (N/m)'] *= 1.167 / 1.128
        # Scale from Conical to Berkovich with large deformations (See Dao et al. 2001
        if '2D' in name:
            df['dP/dh (N/m)'] *= 1.2370 / 1.1957
        # Get Estar if none provided
        if 'FEM_70deg' in name or 'Berkovich' in name or 'conical' in name or '2D' in name or '3D' in name:
            df['Er (GPa)'] = EtoEr(df['E (GPa)'].values, df['nu'].values)[:, None]

        print(df.describe())

        if self.X is None:
            if self.yname == 'n' or self.yname == 's0.033':
                self.X = df[['C (GPa)', 'dP/dh (N/m)', 'Wp/Wt', 'sy (GPa)', 'Er (GPa)']].values
            else:
                self.X = df[['C (GPa)', 'dP/dh (N/m)', 'Wp/Wt']].values
        else:
            if self.yname == 'n' or self.yname == 's0.033':
                self.X = np.vstack((self.X, df[['C (GPa)', 'dP/dh (N/m)', 'Wp/Wt', 'sy (GPa)', 'Er (GPa)']].values))
            else:
                self.X = np.vstack((self.X, df[['C (GPa)', 'dP/dh (N/m)', 'Wp/Wt']].values))
        if self.new == True:
            if self.y is None:
                self.y = df[['C (GPa)']].values
            else:
                self.y = np.vstack((self.y, df[['C (GPa)']].values))
        elif self.yname == 'Er':
            if self.y is None:
                self.y = df['Er (GPa)'].values[:, None]
            else:
                self.y = np.vstack((self.y, df['Er (GPa)'].values[:, None]))
        elif self.yname == 'sy':
            if self.y is None:
                self.y = df['sy (GPa)'].values[:, None]
            else:
                self.y = np.vstack((self.y, df['sy (GPa)'].values[:, None]))
        elif self.yname == 'n':
            if self.y is None:
                self.y = df[['n']].values
            else:
                self.y = np.vstack((self.y, df[['n']].values))
        elif self.yname == 's0.033':
            if 'Lu' in name or 'TI33' in name or '2D' in name or '3D' in name:
                df['s0.033 (GPa)'] = s033(df['Er (GPa)'].values, df['sy (GPa)'].values, df['n'].values, df['nu'].values)[:, None]
            if self.y is None:
                self.y = df['s0.033 (GPa)'].values[:, None]
            else:
                self.y = np.vstack((self.y, df['s0.033 (GPa)'].values[:, None]))

    def pop(self, index):
        self.X = np.delete(self.X, index, axis=0)
        self.y = np.delete(self.y, index, axis=0)
    
    def push(self, index):
        self.X = np.append(index.X)
        self.y = np.append(index.y)
    
def EtoEr(E, nu):
    nu_i, E_i = 0.0691, 1143
    return 1 / ((1 - nu ** 2) / E + (1 - nu_i ** 2) / E_i)

def ErtoE(Er, nu):
    nu_i, E_i = 0.0691, 1143
    return (1 - nu ** 2) / (1 / Er -(1 - nu_i ** 2) / E_i)

def s033(Er, sy, n, nu):
    E = ErtoE(Er, nu)
    ey = sy / E + 0.002
    K = sy / (ey ** n)
    return K * (ey + 0.033) ** n