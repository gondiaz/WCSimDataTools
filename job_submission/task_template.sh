#!/bin/bash

source $HOME/.bashrc
setup_root
root-to-hdf5 -v --wcsimlib $HOME/Software/WCSim/install-Linux_x86_64-gcc_13.2.0-python_3.10.13/lib input_files -o out_dir
