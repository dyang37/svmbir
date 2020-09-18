# svmbir


### Python code for fast parallel-beam MBIR (Model Based Iterative Reconstruction) 
#### This is a python wrapper around the c super-voxel code: https://github.com/HPImaging/sv-mbirct

#### System Requirements
1. GCC compiler version 4.8.5 or above
2. OpenMP API
3. Python>=3.6
(Python dependencies are automatically installed upon installation of svmbir)


#### Optional System Requirements for faster reconstruction
1. Intel-based CPU(s)
2. Intel "icc" compiler (included in "Parallel Studio XE", available from Intel for Linux, macOS)

It is highly recommended that you install svmbir in an anaconda evironment.
Details on conda environments can be found here: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment



### Installation
Go to a directory of your choice and run the following commands to install from source.
**These commands need to be run EXACTLY.**
##### 1. ```git clone --recursive https://github.com/cabouman/svmbir.git```

This recursively clones the svmbir python code and the submodule with C code into a folder in the currect directory.

##### 2. (Optional) ```conda env create -f environment.yml```
This creates a conda environment with the required dependencies.

##### 3. (Optional) ```conda activate svmbir```
This activates the conda environment.


##### 4. ```cd svmbir```

This changes into the root directory of the repository.

##### 5. ```make -C svmbir/sv-mbirct/src/ -f Makefile.gcc```

This builds the binary executable from the C source code using GCC.
If Intel ICC compiler is present, then faster reconstruction can be achieved by building with ICC:
```make -C svmbir/sv-mbirct/src/```

##### 6. ```pip install .```

This installs svmbir and its dependencies as a python package.
To make sure that svmbir has been installed run ```pip list``` to see the list of installed python packages.

After svmbir is installed in the system and can be used in any python script in any directory using the command ```import svmbir```

To update the package, just run the installation process again.


### Execution
```demo.py``` contains a short demo that demonstrates how to use the svmbir package for performing reconstructions.

The file ```demo.py``` and the ```data``` directory can be copied together to any directory and it should still run if the installation is successful.

To reconstruct your own data, use the interface demonstrated in ```demo.py```. 
It Should work from any directory once the svmbir installation is successful.


