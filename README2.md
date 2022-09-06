
<h1 align="center">
  <br>
  <a href=https://drive.google.com/uc?id=1srvPCYxHFTynlTJ6_zq8-sPWPYvnUqgR"><img src="https://drive.google.com/uc?id=1srvPCYxHFTynlTJ6_zq8-sPWPYvnUqgR" alt="CMJ_RED" width="200"></a>
  <br>
  <br>
</h1>


<p align="center">
  <a href="#code-structure">Code</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#docker">Docker</a> •
  <a href="#PythonEnv">PythonEnv</a> •
  <a href="#Databricks">Databricks</a> •

[comment]: <> (  <a href="#notebook">Notebook </a> •)
</p>

## Code design
* We recommend using Docker for dev and production. Therefore we encourage its usage all other the repo.
* We have `vanilla` and `sandbox` environment. 
  * `Vanilla` refers to a prebuilt docker image that already contains system dependencies.
  * `Sandbox` referes a predbuilt docker image that contains the code of this repo.
* Semantic versioning https://semver.org/ . We commit fix to `a.b.x`, features to `a.x.c` and stable release (master) to `x.b.c`. 
* PR are done to `dev` and reviewed for additional features. This should only be reviewed by the engineers in the team.
* PR are done to `master` for official (internal) release of the codes. This should be reviewed by the maximum number of engineers.   
* The ETL jobs are scatter accross sequential refinement of the data `landing/bronze/silver/gold` 
* Modules and scripts: Any piece of code that can of use for parent module modules should be moved at a higher level. 
  * eg: `functional.py` contains common funtions for `etl.bronze` and `etl.silver`
```
...
├── etl
│   ├── bronze
│   │   ├── __init__.py
│   │   └── __main__.py
│   ├── functional.py
│   ├── __init__.py
│   └── landing
│       ├── __init__.py
│       └── __main__.py
├── functional.py
├── __init__.py
...
```
* Modules should ideally contain a `__main__.py` that demo an exeution of the module
  * `etl/bronze/__main__.py` describes an etl job for the creation of the bronze parition
  * `trainer/__main__.py` describes the training pipeline



# Code structure
```python
from setuptools import setup
from cmj_red import __version__

setup(
    name="cmj_red",
    version=__version__,
    short_description="cmj_red",
    long_description="cmj_red",
    packages=[
        "cmj_red",
        "cmj_red.core",
        "cmj_red.dataset",
        "cmj_red.etl",
        "cmj_red.model",
    ],
    include_package_data=True,
    package_data={"": ["*.yml"]},
    url="https://catalinamarketing@dev.azure.com/catalinamarketing/jp-placeholder/_git/cmj-red",
    license="CMJ",
    author="CADIC Jean-Maximilien",
    python_requires=">=3.6",
    install_requires=[r.rsplit()[0] for r in open("requirements.txt")],
    author_email="cjean@catmktg.com",
    description="cmj_red",
    platforms="linux_debian_10_x86_64",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: CMJ License",
    ],
)
```

# How to use
To clone and run this application, you'll need [Git](https://git-scm.com) and [ https://docs.docker.com/docker-for-mac/install/]( https://docs.docker.com/docker-for-mac/install/) and Python installed on your computer. 
From your command line:

Install the cmj-red:
```bash
# Clone this repository and install the code
git clone git@ssh.dev.azure.com:v3/catalinamarketing/jp-placeholder/cmj-red

# Go into the repository
cd cmj-red
```
## Config file
By default the config file is added at the root of this package. You can set a different path by setting a global variable `CMJ_RED_CONFIG` to your custom yaml file.
```yaml
project: cmj_red
mlflow_catboost_promotions: "/Users/cjean@catmktg.com/cmj-red/model/experiments/catboost_promotions"
```

# Makefile
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
clean
build_msranker 
build_tfconverter
build_wheels
auto_branch 
databricks_replace
```
### PythonEnv (not recommended)
```
make install_wheels
``` 

### Docker (recommended)
```shell
make build
make docker_run_sandbox_cpu
```

## Ressources
* Vanilla:  https://en.wikipedia.org/wiki/Vanilla_software
* Sandbox: https://en.wikipedia.org/wiki/Sandbox_(software_development)
* All you need is docker: https://www.theregister.com/2014/05/23/google_containerization_two_billion/
* Dev in containers : https://code.visualstudio.com/docs/remote/containers
* Delta lake partitions: https://k21academy.com/microsoft-azure/data-engineer/delta-lake/