from setuptools import setup
import os
from gnutools.utils import parent, listfiles
import numpy as np
from gnutools import __version__

CURRENT_DIR = os.path.curdir

def get_requirements(txt_file):
    """
    Get the list of requirements for setup_requires in setup.py

    :param txt_file:
    :return list:
    """
    def is_req(req):
        return (not (req[0]=="#")) if len(req)>0 else False
    lines = [line.split("\n")[0] for line in open(txt_file,"r").readlines()]
    return [line for line in lines if is_req(line)]

def get_packages(root):
    """
    Get the list of packages availables in a root

    :param root: package root
    :return list:
    """
    root = os.path.realpath(root)
    proot = parent(root) + "/"
    py_files = [file.rsplit(proot)[1] for file in listfiles(root, patterns=[".py"]) if ((os.stat(file).st_size>0) &
                                                                                        (not file.__contains__(".pyc")))]
    packages = list(np.unique([parent(file).replace("/", ".") for file in py_files]))
    # packages = [p.split("gnutools-python.")[1] for p in packages if len(p.split("gnutools-python."))>1]
    return packages

setup(
    name='gnutools-python',
    version=__version__,
    long_description="",
    packages=get_packages("gnutools"),
    include_package_data=True,
    url='https://github.com/JeanMaximilienCadic',
    license='MIT',
    author='Jean Maximilien Cadic',
    python_requires='>=3.6',
    install_requires=["h5py","tqdm", "numpy", "configparser", "jsonschema", "pyyaml"],
    author_email='j.cadic@pm.me',
    description='GNU Tools for python',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ]
)

