![gnutools Logo](imgs/gnutools-python.png)

--------------------------------------------------------------------------------

Gnutools is a Python package that provides a few perks:
- Up to 3x speedup processing the disk by using system commands instead of python libs.
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

## Benchmark
* Pathlib 10.1s to scan 856631 files
```
from pathlib import Path
results = [f for f in Path("/mnt/hdd/backup/ASR").glob("**/*.wav")]
```

* gnutools 3.7s to scan 856631 files
```
from gnutools.fs import listfiles
results = listfiles("/mnt/hdd/backup/ASR", [".wav"])
```


