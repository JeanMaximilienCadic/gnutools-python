<h1 align="center">
  <br>
  <a href=https://drive.google.com/uc?id=1vHpmRHChj0lPvytmGUJ3mExcLgIYLMJj"><img src="https://drive.google.com/uc?id=1vHpmRHChj0lPvytmGUJ3mExcLgIYLMJj"></a>
  <br>
  GNUTOOLS
  <br>
</h1>

<p align="center">
  <a href="#modules">Modules</a> •
  <a href="#code-structure">Code structure</a> •
  <a href="#installing-the-application">Installing the application</a> •
  <a href="#makefile-commands">Makefile commands</a> •
  <a href="#environments">Environments</a> •
  <a href="#running-the-application">Running the application</a>
  <a href="#ressources">Ressources</a>
</p>

![](
)

<p align="center">
        <img alt="Build" src="https://github.com/JeanMaximilienCadic/gnutools-python/actions/workflows/docker-image.yml/badge.svg?branch=master">
        <img alt="GitHub" src="https://img.shields.io/github/license/JeanMaximilienCadic/gnutools-python.svg?color=blue">
        <img alt="GitHub release" src="https://img.shields.io/github/release/JeanMaximilienCadic/gnutools-python.svg">
</p>


Gnutools is a Python package that provides a few perks:
- Up to 3x speedup processing the disk by using system commands instead of python libs.
- A simple interface with optimized command executed from the system.
- A list of functions to ease the file processing in python.

You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend ZakuroCache integration.


# Modules

At a granular level, Gnutools is a library that consists of the following components:

| Component | Description |
| ---- | --- |
| **gnutools** | Contains the implementation of Gnutools |
| **gnutools.audio** | Audio processsing |
| **gnutools.fs** | File system processing|
| **gnutools.concurrent** | Concurrent processing|
| **gnutools.grid** | Grid search|
| **gnutools.remote** | Download files from gdrive |
| **gnutools.tests** | Unit tests |
| **gnutools.utils** | Utilitaries |



# Code structure
```python
from setuptools import setup
from gnutools import __version__

setup(
    name="gnutools-python",
    version=__version__,
    packages=[
        "gnutools",
        "gnutools.audio",
        "gnutools.concurrent",
        "gnutools.fs",
        "gnutools.grid",
        "gnutools.remote",
        "gnutools.tests",
        "gnutools.utils",
    ],
    long_description="".join(open("README.md", "r").readlines()),
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/JeanMaximilienCadic/gnutools-python",
    license="MIT",
    author="Jean Maximilien Cadic",
    python_requires=">=3.6",
    install_requires=[r.rsplit()[0] for r in open("requirements.txt")],
    author_email="git@cadic.jp",
    description="GNU Tools for python",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
)

```

# Installing the application
To clone and run this application, you'll need the following installed on your computer:
- [Git](https://git-scm.com)
- Docker Desktop
   - [Install Docker Desktop on Mac](https://docs.docker.com/docker-for-mac/install/)
   - [Install Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows-install/)
   - [Install Docker Desktop on Linux](https://docs.docker.com/desktop/install/linux-install/)
- [Python](https://www.python.org/downloads/)

Install the package:
```bash
# Clone this repository and install the code
git clone https://github.com/JeanMaximilienCadic/gnutools-python

# Go into the repository
cd gnutools-python
```

# Makefile commands
Exhaustive list of make commands:
```
install_wheels
sandbox_cpu
sandbox_gpu
build_sandbox
push_environment
push_container_sandbox
push_container_vanilla
pull_container_vanilla
pull_container_sandbox
build_vanilla
build_wheels
auto_branch 
```
# Environments

## Docker

> **Note**
> 
> Running this application by using Docker is recommended.

To build and run the docker image
```
make build
make sandbox
```

## PythonEnv

> **Warning**
> 
> Running this application by using PythonEnv is possible but *not* recommended.
```
make install_wheels
```

# Running the application
* Pathlib `10.1s` to scan `856631` files
```python
from pathlib import Path
results = [f for f in Path("/mnt/hdd/backup/ASR").glob("**/*.wav")]
```

* gnutools `3.7s` to scan `856631` files
```python
from gnutools.fs import listfiles
results = listfiles("/mnt/hdd/backup/ASR", [".wav"])
```


# Ressources
* Vanilla:  https://en.wikipedia.org/wiki/Vanilla_software
* Sandbox: https://en.wikipedia.org/wiki/Sandbox_(software_development)
* All you need is docker: https://www.theregister.com/2014/05/23/google_containerization_two_billion/
* Dev in containers : https://code.visualstudio.com/docs/remote/containers
* Delta lake partitions: https://k21academy.com/microsoft-azure/data-engineer/delta-lake/




