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
