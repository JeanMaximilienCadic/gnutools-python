![gnutools Logo](imgs/gnutools-python.png)

--------------------------------------------------------------------------------

Gnutools is a Python package that provides two high-level features:
- A simple interface with optimized command executed from the system.
- A list of functions to ease the file processing in python.

You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend ZakuroCache integration.


## Gnutools modules

At a granular level, Gnutools is a library that consists of the following components:

| Component | Description |
| ---- | --- |
| **gnutools** | Contains the implementation of Gnutools |
| **gnutools.audio** | Audio processsing |
| **gnutools.fs** | File system processing|
| **gnutools.test** | Test units |
| **gnutools.utils** | Utilitaries |


## Installation

### Docker
To build the image with docker-compose
```
make build
make docker_run_sandbox_cpu
```

### Local
```
make install_wheels
```
