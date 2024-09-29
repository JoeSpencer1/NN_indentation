# Multi-fidelity neural network

## Description
My version of the neural network published by Lu et al., used to model indentation of 33% TiAlTa.
Lu et al.'s paper can be found [here](https://www.pnas.org/content/early/2020/03/13/1922210117), and the code they used can be found [here](https://github.com/lululxvi/deep-learning-for-indentation).

## Data
The data used in this work can be found in the [data](data) folder. The data was collected from nanoindentation tests performed on samples of 33% TiAlTa at different temperatures.

## Code
All code is contained in the [src](src) folder. A summary of each file is provided below:
- The code for the neural network and multi-fidelity neural networks is found in 
the main project file, nn.py.
- The function used to read indentation data from a file and convert it to the program format when needed is found in data.py.
- Factors in dataedit.py need to be changed depending on which temperature data is being adjusted. These are temperature, method, and n. This file is used to produce the neural network's input data.
- Figures used in presentations were created using figures.py.
- Multiple functions can be performed in parallel with runmultiple.py to speed up processing time.
- Fitting functions were used in model.py. The yield stress and elastic stress files must be cleared before a new yield stress dataset can be created for a material and model.py can be used.

## Finite element method simulations
- Finite element simulations were 
- MOOSE was configured using a different derivative size. The input files and mesh generation files are located in the [moose](moose) folder.
- Contact problems like this one can be executed in the `~/projects/moose/modules/contact/` folder using 4 parallel threads with the commands,
```
mpiexec -n 4 ~/projects/moose/modules/contact/contact-opt -i ind_2D.i
```

Besides conventional Python packages, the following package by Lu Lu is required to run the programs.
- [DeepXDE](https://github.com/lululxvi/deepxde) `v1.11.1` is used, with `tensorflow.compat.v1` set as its backend. Some DeepXDE functions may need to be modified if a different version is used.
- [Keras](https://keras.io/) `v2.15.0` is used. DeepXDE will not work with newer versions of Keras like v3.
- [TensorFlow](https://www.tensorflow.org/) `v2.15.0`, with `tensorflow-probability==0.23.0` (see this DeepXDE [Git issue](https://github.com/lululxvi/deepxde/issues/1682)).
-[MOOSE](https://mooseframework.inl.gov/releases/moose/2021-09-15/getting_started/installation/) was installed in a separate environment using the program's documented installation instructions. The derivative size was also set to 300
```
./configure --with-derivative-size=300
```

## Questions
For help using this code, please see the issues section or open a new issue.
