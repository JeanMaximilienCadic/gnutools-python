![Iyo Logo](img/iyo_banner.png)

--------------------------------------------------------------------------------

Iyo is a Python package that provides two high-level features:
- A simplified framework combining in backend end PyTorch, Chainer and Tensorflow
- A list of utilities to do multi-modal analysis easily


You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend Iyo when needed.

We are in an early-release beta. Expect some adventures and rough edges.

- [Iyo modules](#iyo-modules)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Documentation](#documentation)
- [Previous Versions](#previous-versions)
- [Docker Image](#docker-image)



## Iyo modules

At a granular level, Iyo is a library that consists of the following components:

| Component | Description |
| ---- | --- |
| **iyo.audio** | audio processing (bss, noise canceling..)|
| **iyo.biomech.pose2d**| biomechanical module (2d pose estimation)|
| **iyo.biomech.pose3d**| biomechanical module (3d pose estimation)|
| **iyo.bot** | iyoBot control module|
| **iyo.cad**| 3d mesh operations|
| **iyo.core** | iyo core modules|
| **iyo.core.db** | iyo database modules (pyMongo)|
| **iyo.core.dist** | iyo distributed module (workers, kokoro, multiprocessing...)|
| **iyo.core.nn**| deep neural network module|
| **iyo.core.nn.modules**| pytorch binding|
| **iyo.core.nn.layers**| keras binding|
| **iyo.core.nn.chains**| chainer binding|
| **iyo.core.nn.generic**| generic task (classifier2d, generator3d, speech recognition...) |
| **iyo.core.nn.models**| deep neural network models|
| **iyo.core.nn.utils.data**| deep neural network data utils|
| **iyo.core.nn.utils.data.balancers**| to balance datasets|
| **iyo.core.nn.utils.data.decoders**| to decode tensors|
| **iyo.core.nn.utils.data.generators**| to load tensors dynamically|
| **iyo.core.nn.utils.data.manifest**| to build manifests|
| **iyo.core.nn.utils.data.parsers**| to parse data|
| **iyo.core.nn.utils.data.preparators**| to prepare datasets|
| **iyo.core.nn.utils.data.sample**| to load samples during traning|
| **iyo.core.nn.utils.data.splitters**| to split datasets|
| **iyo.cv** | computer vision processing |
| **iyo.genetics** | genetic algorithms|
| **iyo.nlp**| nlp module|
| **iyo.www** | web processings (Youtube) |

## Installation

#### Install IYO required dependencies

```
# System dependencies
sudo apt-get install g++-5 gcc-5 git sox libsox-dev libsox-fmt-all meshlab python3 python3-pip cmake
```

```
# Create iyo env (only if it doesn't exist)
sudo bash iyo_conda.sh
```

```
# Conda  dependencies
conda install -c acellera cuda-runtime
conda install -c anaconda cupy
conda install pyaudio
```

```
# Install python requirements
pip install -r req_setup.txt
```

```
# Compile iyo dependencies
sudo bash compile.sh
```

#### Install Iyo
```
pip3 install iyo-python
```

## Getting-started
A list of examples can be found on Git:
[https://github.com/9dwLab](https://github.com/9dwLab)

## Documentation
All the API to use IYO is available here:
[http://iyo.ai](http://iyo.ai)

## Previous versions
Previous versions can be found here:
[https://pypi.org/project/iyo-python/](https://pypi.org/project/iyo-python/)

## Docker image
Build as usual
```
docker pull 9dwlab/iyo
```

You can also pull a pre-built docker image from Docker Hub and run with nvidia-docker,
but this is not currently maintained so you should update the iyo-python package.
```
iyo-docker 9dwlab/iyo:latest
```

Iyo is 9dw licensed, all rights are reserved.
