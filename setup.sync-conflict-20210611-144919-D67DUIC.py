from setuptools import setup

setup(
    name='gnutools-python',
    version="2.0a1",
    long_description="",
    packages=[
        "gnutools.audio",
        "gnutools.fs",
        "gnutools.test",
        "gnutools.utils",
    ],
    include_package_data=True,
    url='https://github.com/JeanMaximilienCadic/gnutools-python',
    license='MIT',
    author='Jean Maximilien Cadic',
    python_requires='>=3.6',
    install_requires=[r.rsplit()[0] for r in open("requirements.txt")],
    author_email='git@cadic.jp',
    description='GNU Tools for python',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ]
)

