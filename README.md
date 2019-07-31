# Plum!

Simple program in python to generate a project skeleton from templates in the spirit of [Yeoman](https://yeoman.io/), [CookieCutter](https://cookiecutter.readthedocs.io) and [others](https://en.wikipedia.org/wiki/Scaffold_(programming)).

## Project templates

| Template                    | Description                                               |
| --------------------------- | --------------------------------------------------------- |
| cpp_cmake_eclipse_conda_exe | C++ executable CMake Eclipse Project to build with conda. |
| cpp_cmake                   | Simple C++ executable                                     |

## Instructions

### Build source distribution

```bash
python3 setup.py sdist
```

### Usage

Install plum-x.y.z.tar.gz and run from folder:

```bash
python plum.py
```

