# NeoGaPP

Based on [_GaPP_](https://github.com/carlosandrepaes/GaPP), this fork aims to provide native execution of the library in _Python 3_ environments. Its utility lies in the incompatibilities of the original due to API changes in dependencies like _NumPy_, and the emergence of new platforms like `aarch64-apple-darwin` which are not natively supported by _Python 2_.

## Installation

To install _NeoGaPP_, simply clone this repository into a local directory, and install it by running `pip install .` in the root of the same directory.

> The `examples` folder contains some sample programs to demonstrate the capabilities of the library.

## Information

_GaPP_, meaning _Gaussian Processes in Python_, is a library that facilitates the use of Gaussian processes, which can be used to reconstruct a function from a sample of data without assuming a parameterization of it. It handles individual error bars on the data and can be used to determine the derivatives of the reconstructed function.

## Original Authors

Credit is given to the original authors of _GaPP_ which was written by Marina Seikel, Chris Clarkson, and Mathew Smith, and used in their paper [_Reconstruction of dark energy and expansion dynamics using Gaussian processes_](https://arxiv.org/abs/1204.2832).
