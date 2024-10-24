# Multi-fidelity neural network

## Description
My version of the [DeepXDE](https://doi.org/10.1137/19M1274067) neural network used to extract the mechanical of 33% TiAlTa from nanoindentation originally published by [Lu et al](https://doi.org/10.1073/pnas.1922210117). Lu et al.'s code is available in another [GitHub Repository](https://github.com/lululxvi/deep-learning-for-indentation) they maintain.

## Data
The data used in this work can be found in the [data](data) folder. The data was collected from 2D FEM simulations, 3D FEM simulations, and experimental nanoindentation tests performed on a sample of 33% TiAlTa. A compression test was used to find Poisson's ratio for the metal.

## Neural network
All code is contained in the [src](src) folder. A summary of each file is provided below:
- The code for the neural network and multi-fidelity neural networks is located in [nn.py](src/nn.py).
- The function used to read indentation data from a file and convert it to the program format when needed is found in [data.py](src/data.py).
- Multiple functions can be performed in parallel using [runmultiple.py](src/runmultiple.py) to speed up executaion.
- Fitting functions developed by [Chollacoop et al.](https://doi.org/10.1016/S1359-6454(03)00186-1) were used in [fitting.py](src/fitting.py) to find the alloy's mechanical properties. Yield and plastic stress files must be cleared before a new yield dataset can be calculated.
- If a different indenter geometry is desired, the required dimensions can be determined using [dimensions.py](src/dimensions.py).

Besides some Python packages listed in [requirements.txt](src/requirements.txt), the following packages are required to use the neural network.
- [DeepXDE](https://github.com/lululxvi/deepxde) `v1.11.1` with `tensorflow.compat.v1` set as its backend. Some DeepXDE functions may need to be modified if a different version is used.
- [Keras](https://keras.io/) `v2.15.0`. DeepXDE will not work with newer versions of Keras like v3.
- [TensorFlow](https://www.tensorflow.org/) `v2.15.0`, with `tensorflow-probability==0.23.0` (see this DeepXDE [Git issue](https://github.com/lululxvi/deepxde/issues/1682)).

## Finite element method
Finite element method (FEM) simulations were performed usinng the Multi-physics object oriented simulation environt ([MOOSE](https://mooseframework.inl.gov/)) with some specific configurations. Files used in these simulations can be found in the [moose](moose) folder.
- MOOSE was installed in a separate environment using the software's documented [installation instructions](https://mooseframework.inl.gov/releases/moose/2021-09-15/getting_started/installation/). 
- [Volumetric locking](https://mooseframework.inl.gov/modules/solid_mechanics/VolumetricLocking.html) correction is needed in the \[GlobalParams\] block for simulations with first-order shape functions and should be commented for second-order simulations.
- Contact problems like this can be executed using different executables, including custom executables, `combined-opt`, or `~/projects/moose/modules/contact/contact-opt`. For example, to execute `ind_2D_l.i` with custom values of 3 and 2 for the `ref` and `refi` refinement variables, run
```
mpiexec -n 4 ~/projects/moose/modules/contact/contact-opt -i ind_2D_l.i -input-params ref=3 refi=2
```
- To accurately integrate the $`\text{L}^2`$ error over quadratic meshes, modify the `framework/src/userobjects/SolutionUserObject.C` file in the MOOSE installation. For second-order meshes, MOOSE was recompiled with the variable orders on lines 314 and 335 of `SolutionUserObject.C` changed from `FIRST` to `SECOND`.

## Questions
For help using this code, please consult the issues section.