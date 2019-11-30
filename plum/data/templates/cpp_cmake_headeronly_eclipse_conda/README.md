# [project_name]

Header only C++17 library template.

## Instructions

### Building with CMake

´´´
mkdir build
cd build
cmake ..
make -j2
sudo make install
´´´

### conda package generation

´´´
conda-build -c defaults -c conda-forge conda-recipe
´´´

### Usage (CMake)

´´´
project(my-project-that-uses-[project_name])

find_package([project_name] REQUIRED)

add_executable(${PROJECT} main.cpp)
target_link_libraries(${PROJECT} [project_name])
´´´