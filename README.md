# WCSim Python DataTools

This repository is a Python Package containing tools to process and read the simulation data for the [WCTE experiment](https://wcte.hyperk.ca/).

## Dependencies
 - python
 - [ROOT](https://root.cern.ch/)
 - [WCSim](https://github.com/WCTE/WCSim) \
        Same ROOT version **must** be used for the compilation of WCSim and the tools provided for this package.
        The WCSim .root simulation files must have been produced with this particular version.\
        Technically one just needs the [WCSimRoot](https://github.com/WCSim/WCSim?tab=readme-ov-file#wcsim-cmake-build-options) library from WCSim to read the data files. 

This package is known to work in the following platforms/software versions:
- MacOS Ventura 13.2.1
     - Python 3.10.10
     - ROOT 6.24/06
- Rocky Linux release 8.4 (Green Obsidian)
     - Python 3.7.8
     - ROOT 5.34/38
- CentOS Linux release 7.9.2009
     - Python 3.10.13
     - ROOT 6.28/07

## How To

### **install (recomended)**
1. Clone this repository (`git clone`)
2. Move to git directory `cd WCSimDataTools`
3. Use a conda environment: `conda activate env-name`
4. Setup ROOT such that you can `import ROOT`
5. Install the python package in editable mode `pip install --editable .`\
    Installing in editable mode will allow you to develop package features.
6. You can remove the package using `pip uninstall wcsim-hdf5`

### **.root to .hdf5 file conversion**
After the installation, you can simply run the `root-to-hdf5`. It requires to provide the path to the WCSim library containing `libWCSimRoot.dylib`

> `root-to-hdf5 --wcsimlib /path/to/WCSim-build/ /path/to/files/*.root [-o outpath]` 

### **reading .hdf5 files**

The `wcsimreader` package contains the tools to read the WCSim .hdf5 files. You can explore the data in the file by calling

```python 
from wcsimreader import utils
utils.explore_file(filename)
```

To read the files in a `pandas.DataFrame` instance you can use, for example for reading the table **wcsimT/Tracks**

```python 
from wcsimreader import utils
utils.read_table(filename, "wcsimT/Tracks")
```


## To Do
- [ ] Add Pi0 and NCapture data
- [ ] Add tests
- [ ] Implement `conda` package
- [ ] Implement event filtering readers
- [ ] Implement event filtering writers
