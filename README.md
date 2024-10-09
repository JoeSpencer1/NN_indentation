# Multi-fidelity neural network

## Description
My version of the neural network published by Lu et al., used to extract the mechanical of 33% TiAlTa from nanoindentation.
Lu et al.'s paper can be found [here](https://doi.org/10.1073/pnas.1922210117), and their code is available on another [GitHub Repository](https://github.com/lululxvi/deep-learning-for-indentation).

## Data
The data used in this work can be found in the [data](data) folder. The data was collected from nanoindentation tests performed on samples of 33% TiAlTa.

## Neural network
All code is contained in the [src](src) folder. A summary of each file is provided below:
- The code for the neural network and multi-fidelity neural networks is located in [nn.py](src/nn.py).
- The function used to read indentation data from a file and convert it to the program format when needed is found in [data.py](src/data.py).
- Multiple functions can be performed in parallel with [runmultiple.py](src/runmultiple.py) to speed up processing time.
- Fitting functions developed by [Chollacoop et al.](https://doi.org/10.1016/S1359-6454(03)00186-1) were used in [fitting.py](src/fitting.py). The yield stress and elastic stress files must be cleared before a new yield stress dataset can be created for a material and model.py can be used.
- If a different indenter geometry is desired, the required dimensions can be determined using [dimensions.py](src/dimensions.py).

Besides some Python packages discussed in [requirements.txt](src/requirements.txt), the following packages are required to use the neural network.
- [DeepXDE](https://github.com/lululxvi/deepxde) `v1.11.1` is used, with `tensorflow.compat.v1` set as its backend. Some DeepXDE functions may need to be modified if a different version is used.
- [Keras](https://keras.io/) `v2.15.0` is used. DeepXDE will not work with newer versions of Keras like v3.
- [TensorFlow](https://www.tensorflow.org/) `v2.15.0`, with `tensorflow-probability==0.23.0` (see this DeepXDE [Git issue](https://github.com/lululxvi/deepxde/issues/1682)).

## Finite element models
Finite element method (FEM) simulations were performed usinng the Multi-physics object oriented simulation environt ([MOOSE](https://mooseframework.inl.gov/)), with some specific configurations. Input files used for the FEM simulations are located in the [moose](moose) folder.
- MOOSE was installed in a separate environment using the program's documented [installation instructions](https://mooseframework.inl.gov/releases/moose/2021-09-15/getting_started/installation/). 
- Volumetric locking correction is only needed in the \[GlobalParams\] block for simulations with first-order elements
- The derivative size should be increased to 300 in the MOOSE installation's root directory to allow automatic differentiation ([AD](https://mooseframework.inl.gov/automatic_differentiation/)) functions to be used with refined quadratic meshes in `ind_3D_AD.i`.
```
./configure --with-derivative-size=300
```
- If the derivative size cannot be adjusted, use `ind_3D.i` to perform 3D simulations . 
- Contact problems like this can be executed in the `~/projects/moose/modules/contact/` folder. For example, to execute `ind_2D.i` with 4 parallel threads using the message passing interface installed with MOOSE, use
```
mpiexec -n 4 ~/projects/moose/modules/contact/contact-opt -i ind_2D.i
```
- To accurately integrate the L$`^2`$ error over quadratic meshes, modify the `framework/src/userobjects/SolutionUserObject.C` file in the MOOSE installation. For second-order meshes, MOOSE was recompiled with the variable orders on lines 314 and 335 of `SolutionUserObject.C` changed from `FIRST` to `SECOND`.

## Questions
For help using this code, please consult the issues section.