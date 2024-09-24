import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)

def run_processes(arguments):
    processes = []
    num_processes = len(arguments)
    for i in range(num_processes):        
        process = multiprocessing.Process(target=run_main, args=(arguments[i],))
        processes.append(process)

    for process in processes:
        process.start()
    for process in processes:
        process.join()
    with open('output.txt', 'a') as f:
        f.write('\n')

if __name__ == '__main__':
    run_processes([
        "validation_one('sy', 'TI33_25', 'TI33_25', 10)",
        "validation_one('sy', 'TI33_25', 'TI33_25', 5)",
        "validation_one('sy', 'TI33_25', 'TI33_25', 2)"
    ])
    # run_processes(np.array([
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 0, '3D_linear', 0, '2D_70_linear', 0, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 1, '3D_linear', 1, '2D_70_linear', 1, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 2, '3D_linear', 2, '2D_70_linear', 2, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 3, '3D_linear', 3, '2D_70_linear', 3, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 4, '3D_linear', 4, '2D_70_linear', 4, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 5, '3D_linear', 5, '2D_70_linear', 5, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 6, '3D_linear', 6, '2D_70_linear', 6, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 8, '3D_linear', 8, '2D_70_linear', 8, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 10, '3D_linear', 10, '2D_70_linear', 10, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 15, '3D_linear', 15, '2D_70_linear', 15, typ='lo')"
    #     ]))
    # run_processes(np.array([
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 0, '3D_linear', 0, '2D_70_linear', 0, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 1, '3D_linear', 1, '2D_70_linear', 1, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 2, '3D_linear', 2, '2D_70_linear', 2, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 3, '3D_linear', 3, '2D_70_linear', 3, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 4, '3D_linear', 4, '2D_70_linear', 4, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 5, '3D_linear', 5, '2D_70_linear', 5, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 6, '3D_linear', 6, '2D_70_linear', 6, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 8, '3D_linear', 8, '2D_70_linear', 8, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 10, '3D_linear', 10, '2D_70_linear', 10, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 15, '3D_linear', 15, '2D_70_linear', 15, typ='lo')"
    #     ]))
    # run_processes(np.array([
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 0, '3D_quad_r', 0, '2D_70_quad_r', 0, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 1, '3D_quad_r', 1, '2D_70_quad_r', 1, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 2, '3D_quad_r', 2, '2D_70_quad_r', 2, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 3, '3D_quad_r', 3, '2D_70_quad_r', 3, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 4, '3D_quad_r', 4, '2D_70_quad_r', 4, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 5, '3D_quad_r', 5, '2D_70_quad_r', 5, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 6, '3D_quad_r', 6, '2D_70_quad_r', 6, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 8, '3D_quad_r', 8, '2D_70_quad_r', 8, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 10, '3D_quad_r', 10, '2D_70_quad_r', 10, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 15, '3D_quad_r', 15, '2D_70_quad_r', 15, typ='lo')"
    #     ]))
    # run_processes(np.array([
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 0, '3D_quad_r', 0, '2D_70_quad_r', 0, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 1, '3D_quad_r', 1, '2D_70_quad_r', 1, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 2, '3D_quad_r', 2, '2D_70_quad_r', 2, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 3, '3D_quad_r', 3, '2D_70_quad_r', 3, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 4, '3D_quad_r', 4, '2D_70_quad_r', 4, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 5, '3D_quad_r', 5, '2D_70_quad_r', 5, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 6, '3D_quad_r', 6, '2D_70_quad_r', 6, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 8, '3D_quad_r', 8, '2D_70_quad_r', 8, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 10, '3D_quad_r', 10, '2D_70_quad_r', 10, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 15, '3D_quad_r', 15, '2D_70_quad_r', 15, typ='lo')"
    #     ]))
    # run_processes(np.array([
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 0, '3D_linear_r', 0, '2D_70_linear_r', 0, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 1, '3D_linear_r', 1, '2D_70_linear_r', 1, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 2, '3D_linear_r', 2, '2D_70_linear_r', 2, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 3, '3D_linear_r', 3, '2D_70_linear_r', 3, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 4, '3D_linear_r', 4, '2D_70_linear_r', 4, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 5, '3D_linear_r', 5, '2D_70_linear_r', 5, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 6, '3D_linear_r', 6, '2D_70_linear_r', 6, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 8, '3D_linear_r', 8, '2D_70_linear_r', 8, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 10, '3D_linear_r', 10, '2D_70_linear_r', 10, typ='lo')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 15, '3D_linear_r', 15, '2D_70_linear_r', 15, typ='lo')"
    # ]))
    # run_processes(np.array([
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 0, '3D_linear_r', 0, '2D_70_linear_r', 0, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 1, '3D_linear_r', 1, '2D_70_linear_r', 1, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 2, '3D_linear_r', 2, '2D_70_linear_r', 2, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 3, '3D_linear_r', 3, '2D_70_linear_r', 3, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 4, '3D_linear_r', 4, '2D_70_linear_r', 4, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 5, '3D_linear_r', 5, '2D_70_linear_r', 5, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 6, '3D_linear_r', 6, '2D_70_linear_r', 6, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 8, '3D_linear_r', 8, '2D_70_linear_r', 8, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 10, '3D_linear_r', 10, '2D_70_linear_r', 10, typ='lo')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 15, '3D_linear_r', 15, '2D_70_linear_r', 15, typ='lo')"
    # ]))
    # run_processes(np.array([
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 0, '3D_quad', 0, '2D_70_quad', 0, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 1, '3D_quad', 1, '2D_70_quad', 1, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 2, '3D_quad', 2, '2D_70_quad', 2, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 3, '3D_quad', 3, '2D_70_quad', 3, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 4, '3D_quad', 4, '2D_70_quad', 4, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 5, '3D_quad', 5, '2D_70_quad', 5, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 6, '3D_quad', 6, '2D_70_quad', 6, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 8, '3D_quad', 8, '2D_70_quad', 8, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 10, '3D_quad', 10, '2D_70_quad', 10, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 15, '3D_quad', 15, '2D_70_quad', 15, typ='hi')"
    #     ]))
    # run_processes(np.array([
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 0, '3D_quad', 0, '2D_70_quad', 0, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 1, '3D_quad', 1, '2D_70_quad', 1, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 2, '3D_quad', 2, '2D_70_quad', 2, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 3, '3D_quad', 3, '2D_70_quad', 3, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 4, '3D_quad', 4, '2D_70_quad', 4, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 5, '3D_quad', 5, '2D_70_quad', 5, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 6, '3D_quad', 6, '2D_70_quad', 6, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 8, '3D_quad', 8, '2D_70_quad', 8, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 10, '3D_quad', 10, '2D_70_quad', 10, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 15, '3D_quad', 15, '2D_70_quad', 15, typ='hi')"
    # ]))
    # run_processes(np.array([
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 0, '3D_linear', 0, '2D_70_linear', 0, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 1, '3D_linear', 1, '2D_70_linear', 1, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 2, '3D_linear', 2, '2D_70_linear', 2, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 3, '3D_linear', 3, '2D_70_linear', 3, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 4, '3D_linear', 4, '2D_70_linear', 4, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 5, '3D_linear', 5, '2D_70_linear', 5, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 6, '3D_linear', 6, '2D_70_linear', 6, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 8, '3D_linear', 8, '2D_70_linear', 8, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 10, '3D_linear', 10, '2D_70_linear', 10, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 15, '3D_linear', 15, '2D_70_linear', 15, typ='hi')"
    #     ]))
    # run_processes(np.array([
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 0, '3D_linear', 0, '2D_70_linear', 0, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 1, '3D_linear', 1, '2D_70_linear', 1, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 2, '3D_linear', 2, '2D_70_linear', 2, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 3, '3D_linear', 3, '2D_70_linear', 3, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 4, '3D_linear', 4, '2D_70_linear', 4, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 5, '3D_linear', 5, '2D_70_linear', 5, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 6, '3D_linear', 6, '2D_70_linear', 6, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 8, '3D_linear', 8, '2D_70_linear', 8, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 10, '3D_linear', 10, '2D_70_linear', 10, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 15, '3D_linear', 15, '2D_70_linear', 15, typ='hi')"
    #     ]))
    # run_processes(np.array([
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 0, '3D_quad_r', 0, '2D_70_quad_r', 0, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 1, '3D_quad_r', 1, '2D_70_quad_r', 1, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 2, '3D_quad_r', 2, '2D_70_quad_r', 2, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 3, '3D_quad_r', 3, '2D_70_quad_r', 3, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 4, '3D_quad_r', 4, '2D_70_quad_r', 4, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 5, '3D_quad_r', 5, '2D_70_quad_r', 5, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 6, '3D_quad_r', 6, '2D_70_quad_r', 6, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 8, '3D_quad_r', 8, '2D_70_quad_r', 8, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 10, '3D_quad_r', 10, '2D_70_quad_r', 10, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 15, '3D_quad_r', 15, '2D_70_quad_r', 15, typ='hi')"
    #     ]))
    # run_processes(np.array([
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 0, '3D_quad_r', 0, '2D_70_quad_r', 0, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 1, '3D_quad_r', 1, '2D_70_quad_r', 1, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 2, '3D_quad_r', 2, '2D_70_quad_r', 2, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 3, '3D_quad_r', 3, '2D_70_quad_r', 3, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 4, '3D_quad_r', 4, '2D_70_quad_r', 4, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 5, '3D_quad_r', 5, '2D_70_quad_r', 5, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 6, '3D_quad_r', 6, '2D_70_quad_r', 6, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 8, '3D_quad_r', 8, '2D_70_quad_r', 8, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 10, '3D_quad_r', 10, '2D_70_quad_r', 10, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 15, '3D_quad_r', 15, '2D_70_quad_r', 15, typ='hi')"
    #     ]))
    # run_processes(np.array([
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 0, '3D_linear_r', 0, '2D_70_linear_r', 0, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 1, '3D_linear_r', 1, '2D_70_linear_r', 1, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 2, '3D_linear_r', 2, '2D_70_linear_r', 2, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 3, '3D_linear_r', 3, '2D_70_linear_r', 3, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 4, '3D_linear_r', 4, '2D_70_linear_r', 4, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 5, '3D_linear_r', 5, '2D_70_linear_r', 5, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 6, '3D_linear_r', 6, '2D_70_linear_r', 6, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 8, '3D_linear_r', 8, '2D_70_linear_r', 8, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 10, '3D_linear_r', 10, '2D_70_linear_r', 10, typ='hi')",
    #     "validation_three('sy', 'TI33_25', 'TI33_25', 15, '3D_linear_r', 15, '2D_70_linear_r', 15, typ='hi')"
    # ]))
    # run_processes(np.array([
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 0, '3D_linear_r', 0, '2D_70_linear_r', 0, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 1, '3D_linear_r', 1, '2D_70_linear_r', 1, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 2, '3D_linear_r', 2, '2D_70_linear_r', 2, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 3, '3D_linear_r', 3, '2D_70_linear_r', 3, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 4, '3D_linear_r', 4, '2D_70_linear_r', 4, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 5, '3D_linear_r', 5, '2D_70_linear_r', 5, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 6, '3D_linear_r', 6, '2D_70_linear_r', 6, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 8, '3D_linear_r', 8, '2D_70_linear_r', 8, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 10, '3D_linear_r', 10, '2D_70_linear_r', 10, typ='hi')",
    #     "validation_three('Er', 'TI33_25', 'TI33_25', 15, '3D_linear_r', 15, '2D_70_linear_r', 15, typ='hi')"
    # ]))
    # run_processes(np.array([
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 0, '3D_quad', 0)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 1, '3D_quad', 1)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 2, '3D_quad', 2)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 3, '3D_quad', 3)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 4, '3D_quad', 4)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 5, '3D_quad', 5)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 6, '3D_quad', 6)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 8, '3D_quad', 8)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 10, '3D_quad', 10)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 15, '3D_quad', 15)"
    #     ]))
    # run_processes(np.array([
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 0, '3D_quad', 0)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 1, '3D_quad', 1)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 2, '3D_quad', 2)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 3, '3D_quad', 3)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 4, '3D_quad', 4)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 5, '3D_quad', 5)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 6, '3D_quad', 6)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 8, '3D_quad', 8)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 10, '3D_quad', 10)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 15, '3D_quad', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 0, '3D_linear', 0)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 1, '3D_linear', 1)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 2, '3D_linear', 2)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 3, '3D_linear', 3)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 4, '3D_linear', 4)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 5, '3D_linear', 5)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 6, '3D_linear', 6)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 8, '3D_linear', 8)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 10, '3D_linear', 10)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 15, '3D_linear', 15)"
    #     ]))
    # run_processes(np.array([
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 0, '3D_linear', 0)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 1, '3D_linear', 1)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 2, '3D_linear', 2)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 3, '3D_linear', 3)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 4, '3D_linear', 4)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 5, '3D_linear', 5)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 6, '3D_linear', 6)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 8, '3D_linear', 8)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 10, '3D_linear', 10)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 15, '3D_linear', 15)"
    #     ]))
    # run_processes(np.array([
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 0, '3D_quad_r', 0)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 1, '3D_quad_r', 1)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 2, '3D_quad_r', 2)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 3, '3D_quad_r', 3)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 4, '3D_quad_r', 4)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 5, '3D_quad_r', 5)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 6, '3D_quad_r', 6)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 8, '3D_quad_r', 8)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 10, '3D_quad_r', 10)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 15, '3D_quad_r', 15)"
    #     ]))
    # run_processes(np.array([
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 0, '3D_quad_r', 0)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 1, '3D_quad_r', 1)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 2, '3D_quad_r', 2)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 3, '3D_quad_r', 3)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 4, '3D_quad_r', 4)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 5, '3D_quad_r', 5)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 6, '3D_quad_r', 6)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 8, '3D_quad_r', 8)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 10, '3D_quad_r', 10)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 15, '3D_quad_r', 15)"
    #     ]))
    # run_processes(np.array([
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 0, '3D_linear_r', 0)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 1, '3D_linear_r', 1)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 2, '3D_linear_r', 2)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 3, '3D_linear_r', 3)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 4, '3D_linear_r', 4)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 5, '3D_linear_r', 5)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 6, '3D_linear_r', 6)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 8, '3D_linear_r', 8)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 10, '3D_linear_r', 10)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 15, '3D_linear_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 0, '3D_linear_r', 0)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 1, '3D_linear_r', 1)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 2, '3D_linear_r', 2)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 3, '3D_linear_r', 3)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 4, '3D_linear_r', 4)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 5, '3D_linear_r', 5)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 6, '3D_linear_r', 6)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 8, '3D_linear_r', 8)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 10, '3D_linear_r', 10)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 15, '3D_linear_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 0, '2D_70_quad', 0)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 1, '2D_70_quad', 1)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 2, '2D_70_quad', 2)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 3, '2D_70_quad', 3)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 4, '2D_70_quad', 4)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 5, '2D_70_quad', 5)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 6, '2D_70_quad', 6)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 8, '2D_70_quad', 8)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 10, '2D_70_quad', 10)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 15, '2D_70_quad', 15)"
    #     ]))
    # run_processes(np.array([
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 0, '2D_70_quad', 0)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 1, '2D_70_quad', 1)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 2, '2D_70_quad', 2)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 3, '2D_70_quad', 3)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 4, '2D_70_quad', 4)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 5, '2D_70_quad', 5)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 6, '2D_70_quad', 6)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 8, '2D_70_quad', 8)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 10, '2D_70_quad', 10)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 15, '2D_70_quad', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 0, '2D_70_linear', 0)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 1, '2D_70_linear', 1)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 2, '2D_70_linear', 2)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 3, '2D_70_linear', 3)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 4, '2D_70_linear', 4)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 5, '2D_70_linear', 5)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 6, '2D_70_linear', 6)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 8, '2D_70_linear', 8)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 10, '2D_70_linear', 10)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 15, '2D_70_linear', 15)"
    #     ]))
    # run_processes(np.array([
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 0, '2D_70_linear', 0)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 1, '2D_70_linear', 1)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 2, '2D_70_linear', 2)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 3, '2D_70_linear', 3)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 4, '2D_70_linear', 4)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 5, '2D_70_linear', 5)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 6, '2D_70_linear', 6)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 8, '2D_70_linear', 8)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 10, '2D_70_linear', 10)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 15, '2D_70_linear', 15)"
    #     ]))
    # run_processes(np.array([
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 0, '2D_70_quad_r', 0)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 1, '2D_70_quad_r', 1)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 2, '2D_70_quad_r', 2)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 3, '2D_70_quad_r', 3)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 4, '2D_70_quad_r', 4)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 5, '2D_70_quad_r', 5)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 6, '2D_70_quad_r', 6)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 8, '2D_70_quad_r', 8)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 10, '2D_70_quad_r', 10)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 15, '2D_70_quad_r', 15)"
    #     ]))
    # run_processes(np.array([
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 0, '2D_70_quad_r', 0)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 1, '2D_70_quad_r', 1)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 2, '2D_70_quad_r', 2)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 3, '2D_70_quad_r', 3)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 4, '2D_70_quad_r', 4)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 5, '2D_70_quad_r', 5)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 6, '2D_70_quad_r', 6)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 8, '2D_70_quad_r', 8)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 10, '2D_70_quad_r', 10)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 15, '2D_70_quad_r', 15)"
    #     ]))
    # run_processes(np.array([
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 0, '2D_70_linear_r', 0)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 1, '2D_70_linear_r', 1)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 2, '2D_70_linear_r', 2)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 3, '2D_70_linear_r', 3)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 4, '2D_70_linear_r', 4)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 5, '2D_70_linear_r', 5)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 6, '2D_70_linear_r', 6)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 8, '2D_70_linear_r', 8)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 10, '2D_70_linear_r', 10)",
    #     "validation_two('sy', 'TI33_25', 'TI33_25', 15, '2D_70_linear_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 0, '2D_70_linear_r', 0)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 1, '2D_70_linear_r', 1)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 2, '2D_70_linear_r', 2)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 3, '2D_70_linear_r', 3)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 4, '2D_70_linear_r', 4)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 5, '2D_70_linear_r', 5)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 6, '2D_70_linear_r', 6)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 8, '2D_70_linear_r', 8)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 10, '2D_70_linear_r', 10)",
    #     "validation_two('Er', 'TI33_25', 'TI33_25', 15, '2D_70_linear_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('sy', 'TI33_25', 'TI33_25', 2)",
    #     "validation_one('sy', 'TI33_25', 'TI33_25', 3)",
    #     "validation_one('sy', 'TI33_25', 'TI33_25', 4)",
    #     "validation_one('sy', 'TI33_25', 'TI33_25', 5)",
    #     "validation_one('sy', 'TI33_25', 'TI33_25', 6)",
    #     "validation_one('sy', 'TI33_25', 'TI33_25', 8)",
    #     "validation_one('sy', 'TI33_25', 'TI33_25', 10)",
    #     "validation_one('sy', 'TI33_25', 'TI33_25', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('Er', 'TI33_25', 'TI33_25', 2)",
    #     "validation_one('Er', 'TI33_25', 'TI33_25', 3)",
    #     "validation_one('Er', 'TI33_25', 'TI33_25', 4)",
    #     "validation_one('Er', 'TI33_25', 'TI33_25', 5)",
    #     "validation_one('Er', 'TI33_25', 'TI33_25', 6)",
    #     "validation_one('Er', 'TI33_25', 'TI33_25', 8)",
    #     "validation_one('Er', 'TI33_25', 'TI33_25', 10)",
    #     "validation_one('Er', 'TI33_25', 'TI33_25', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('sy', '3D_quad', '3D_quad', 2)",
    #     "validation_one('sy', '3D_quad', '3D_quad', 3)",
    #     "validation_one('sy', '3D_quad', '3D_quad', 4)",
    #     "validation_one('sy', '3D_quad', '3D_quad', 5)",
    #     "validation_one('sy', '3D_quad', '3D_quad', 6)",
    #     "validation_one('sy', '3D_quad', '3D_quad', 8)",
    #     "validation_one('sy', '3D_quad', '3D_quad', 10)",
    #     "validation_one('sy', '3D_quad', '3D_quad', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('Er', '3D_quad', '3D_quad', 2)",
    #     "validation_one('Er', '3D_quad', '3D_quad', 3)",
    #     "validation_one('Er', '3D_quad', '3D_quad', 4)",
    #     "validation_one('Er', '3D_quad', '3D_quad', 5)",
    #     "validation_one('Er', '3D_quad', '3D_quad', 6)",
    #     "validation_one('Er', '3D_quad', '3D_quad', 8)",
    #     "validation_one('Er', '3D_quad', '3D_quad', 10)",
    #     "validation_one('Er', '3D_quad', '3D_quad', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('sy', '3D_linear', '3D_linear', 2)",
    #     "validation_one('sy', '3D_linear', '3D_linear', 3)",
    #     "validation_one('sy', '3D_linear', '3D_linear', 4)",
    #     "validation_one('sy', '3D_linear', '3D_linear', 5)",
    #     "validation_one('sy', '3D_linear', '3D_linear', 6)",
    #     "validation_one('sy', '3D_linear', '3D_linear', 8)",
    #     "validation_one('sy', '3D_linear', '3D_linear', 10)",
    #     "validation_one('sy', '3D_linear', '3D_linear', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('Er', '3D_linear', '3D_linear', 2)",
    #     "validation_one('Er', '3D_linear', '3D_linear', 3)",
    #     "validation_one('Er', '3D_linear', '3D_linear', 4)",
    #     "validation_one('Er', '3D_linear', '3D_linear', 5)",
    #     "validation_one('Er', '3D_linear', '3D_linear', 6)",
    #     "validation_one('Er', '3D_linear', '3D_linear', 8)",
    #     "validation_one('Er', '3D_linear', '3D_linear', 10)",
    #     "validation_one('Er', '3D_linear', '3D_linear', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('sy', '3D_quad_r', '3D_quad_r', 2)",
    #     "validation_one('sy', '3D_quad_r', '3D_quad_r', 3)",
    #     "validation_one('sy', '3D_quad_r', '3D_quad_r', 4)",
    #     "validation_one('sy', '3D_quad_r', '3D_quad_r', 5)",
    #     "validation_one('sy', '3D_quad_r', '3D_quad_r', 6)",
    #     "validation_one('sy', '3D_quad_r', '3D_quad_r', 8)",
    #     "validation_one('sy', '3D_quad_r', '3D_quad_r', 10)",
    #     "validation_one('sy', '3D_quad_r', '3D_quad_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('Er', '3D_quad_r', '3D_quad_r', 2)",
    #     "validation_one('Er', '3D_quad_r', '3D_quad_r', 3)",
    #     "validation_one('Er', '3D_quad_r', '3D_quad_r', 4)",
    #     "validation_one('Er', '3D_quad_r', '3D_quad_r', 5)",
    #     "validation_one('Er', '3D_quad_r', '3D_quad_r', 6)",
    #     "validation_one('Er', '3D_quad_r', '3D_quad_r', 8)",
    #     "validation_one('Er', '3D_quad_r', '3D_quad_r', 10)",
    #     "validation_one('Er', '3D_quad_r', '3D_quad_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('sy', '3D_linear_r', '3D_linear_r', 2)",
    #     "validation_one('sy', '3D_linear_r', '3D_linear_r', 3)",
    #     "validation_one('sy', '3D_linear_r', '3D_linear_r', 4)",
    #     "validation_one('sy', '3D_linear_r', '3D_linear_r', 5)",
    #     "validation_one('sy', '3D_linear_r', '3D_linear_r', 6)",
    #     "validation_one('sy', '3D_linear_r', '3D_linear_r', 8)",
    #     "validation_one('sy', '3D_linear_r', '3D_linear_r', 10)",
    #     "validation_one('sy', '3D_linear_r', '3D_linear_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('Er', '3D_linear_r', '3D_linear_r', 2)",
    #     "validation_one('Er', '3D_linear_r', '3D_linear_r', 3)",
    #     "validation_one('Er', '3D_linear_r', '3D_linear_r', 4)",
    #     "validation_one('Er', '3D_linear_r', '3D_linear_r', 5)",
    #     "validation_one('Er', '3D_linear_r', '3D_linear_r', 6)",
    #     "validation_one('Er', '3D_linear_r', '3D_linear_r', 8)",
    #     "validation_one('Er', '3D_linear_r', '3D_linear_r', 10)",
    #     "validation_one('Er', '3D_linear_r', '3D_linear_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('sy', '2D_70_quad', '2D_70_quad', 2)",
    #     "validation_one('sy', '2D_70_quad', '2D_70_quad', 3)",
    #     "validation_one('sy', '2D_70_quad', '2D_70_quad', 4)",
    #     "validation_one('sy', '2D_70_quad', '2D_70_quad', 5)",
    #     "validation_one('sy', '2D_70_quad', '2D_70_quad', 6)",
    #     "validation_one('sy', '2D_70_quad', '2D_70_quad', 8)",
    #     "validation_one('sy', '2D_70_quad', '2D_70_quad', 10)",
    #     "validation_one('sy', '2D_70_quad', '2D_70_quad', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('Er', '2D_70_quad', '2D_70_quad', 2)",
    #     "validation_one('Er', '2D_70_quad', '2D_70_quad', 3)",
    #     "validation_one('Er', '2D_70_quad', '2D_70_quad', 4)",
    #     "validation_one('Er', '2D_70_quad', '2D_70_quad', 5)",
    #     "validation_one('Er', '2D_70_quad', '2D_70_quad', 6)",
    #     "validation_one('Er', '2D_70_quad', '2D_70_quad', 8)",
    #     "validation_one('Er', '2D_70_quad', '2D_70_quad', 10)",
    #     "validation_one('Er', '2D_70_quad', '2D_70_quad', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('sy', '2D_70_linear', '2D_70_linear', 2)",
    #     "validation_one('sy', '2D_70_linear', '2D_70_linear', 3)",
    #     "validation_one('sy', '2D_70_linear', '2D_70_linear', 4)",
    #     "validation_one('sy', '2D_70_linear', '2D_70_linear', 5)",
    #     "validation_one('sy', '2D_70_linear', '2D_70_linear', 6)",
    #     "validation_one('sy', '2D_70_linear', '2D_70_linear', 8)",
    #     "validation_one('sy', '2D_70_linear', '2D_70_linear', 10)",
    #     "validation_one('sy', '2D_70_linear', '2D_70_linear', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('Er', '2D_70_linear', '2D_70_linear', 2)",
    #     "validation_one('Er', '2D_70_linear', '2D_70_linear', 3)",
    #     "validation_one('Er', '2D_70_linear', '2D_70_linear', 4)",
    #     "validation_one('Er', '2D_70_linear', '2D_70_linear', 5)",
    #     "validation_one('Er', '2D_70_linear', '2D_70_linear', 6)",
    #     "validation_one('Er', '2D_70_linear', '2D_70_linear', 8)",
    #     "validation_one('Er', '2D_70_linear', '2D_70_linear', 10)",
    #     "validation_one('Er', '2D_70_linear', '2D_70_linear', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('sy', '2D_70_quad_r', '2D_70_quad_r', 2)",
    #     "validation_one('sy', '2D_70_quad_r', '2D_70_quad_r', 3)",
    #     "validation_one('sy', '2D_70_quad_r', '2D_70_quad_r', 4)",
    #     "validation_one('sy', '2D_70_quad_r', '2D_70_quad_r', 5)",
    #     "validation_one('sy', '2D_70_quad_r', '2D_70_quad_r', 6)",
    #     "validation_one('sy', '2D_70_quad_r', '2D_70_quad_r', 8)",
    #     "validation_one('sy', '2D_70_quad_r', '2D_70_quad_r', 10)",
    #     "validation_one('sy', '2D_70_quad_r', '2D_70_quad_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('Er', '2D_70_quad_r', '2D_70_quad_r', 2)",
    #     "validation_one('Er', '2D_70_quad_r', '2D_70_quad_r', 3)",
    #     "validation_one('Er', '2D_70_quad_r', '2D_70_quad_r', 4)",
    #     "validation_one('Er', '2D_70_quad_r', '2D_70_quad_r', 5)",
    #     "validation_one('Er', '2D_70_quad_r', '2D_70_quad_r', 6)",
    #     "validation_one('Er', '2D_70_quad_r', '2D_70_quad_r', 8)",
    #     "validation_one('Er', '2D_70_quad_r', '2D_70_quad_r', 10)",
    #     "validation_one('Er', '2D_70_quad_r', '2D_70_quad_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('sy', '2D_70_linear_r', '2D_70_linear_r', 2)",
    #     "validation_one('sy', '2D_70_linear_r', '2D_70_linear_r', 3)",
    #     "validation_one('sy', '2D_70_linear_r', '2D_70_linear_r', 4)",
    #     "validation_one('sy', '2D_70_linear_r', '2D_70_linear_r', 5)",
    #     "validation_one('sy', '2D_70_linear_r', '2D_70_linear_r', 6)",
    #     "validation_one('sy', '2D_70_linear_r', '2D_70_linear_r', 8)",
    #     "validation_one('sy', '2D_70_linear_r', '2D_70_linear_r', 10)",
    #     "validation_one('sy', '2D_70_linear_r', '2D_70_linear_r', 15)"
    # ]))
    # run_processes(np.array([
    #     "validation_one('Er', '2D_70_linear_r', '2D_70_linear_r', 2)",
    #     "validation_one('Er', '2D_70_linear_r', '2D_70_linear_r', 3)",
    #     "validation_one('Er', '2D_70_linear_r', '2D_70_linear_r', 4)",
    #     "validation_one('Er', '2D_70_linear_r', '2D_70_linear_r', 5)",
    #     "validation_one('Er', '2D_70_linear_r', '2D_70_linear_r', 6)",
    #     "validation_one('Er', '2D_70_linear_r', '2D_70_linear_r', 8)",
    #     "validation_one('Er', '2D_70_linear_r', '2D_70_linear_r', 10)",
    #     "validation_one('Er', '2D_70_linear_r', '2D_70_linear_r', 15)"
    # ]))