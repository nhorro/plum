# [project_name]

[project_summary]

## Instructions

This project assumes conda 'build' environment is used for C++ development.
To use this project in Eclipse CDT, select Project->Import and then Build.
Run as local C/C++ application (binaries/[project_name]).

### Build with CMake in conda environment

´´´
cmake -E remove_directory build
cmake -E make_directory build
cd build
cmake .. -G"$CMAKE_GENERATOR" \
         -DCMAKE_BUILD_TYPE=Release \
		 -DCMAKE_PREFIX_PATH=$CONDA_PREFIX \
		 -DCMAKE_INSTALL_PREFIX=$PREFIX \
		 -DCMAKE_AR=${AR} \
		 -DCMAKE_RANLIB=${RANLIB} \
		 -DCMAKE_MAKE_PROGRAM=${CONDA_PREFIX}/bin/make
cmake --build . --config Release --target all
cmake --build . --config Release --target install
´´´

### Build conda package

´´´
conda-build -c conda-forge conda-recipe
´´´

### Publish conda package

TODO
