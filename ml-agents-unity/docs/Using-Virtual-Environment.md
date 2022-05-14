# Using Virtual Environment

## What is a Virtual Environment?

A Virtual Environment is a self contained directory tree that contains a Python
installation for a particular version of Python, plus a number of additional
packages. To learn more about Virtual Environments see
[here](https://docs.python.org/3/library/venv.html).

## Why should I use a Virtual Environment?

A Virtual Environment keeps all dependencies for the Python project separate
from dependencies of other projects. This has a few advantages:

1. It makes dependency management for the project easy.
1. It enables using and testing of different library versions by quickly
   spinning up a new environment and verifying the compatibility of the code
   with the different version.

## Python Version Requirement (Required)

This guide has been tested with Python 3.6 through Python 3.8. Newer versions might not
have support for the dependent libraries, so are not recommended.

## Installing Pip (Required)

1. Download the `get-pip.py` file using the command
   `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
1. Run the following `python3 get-pip.py`
1. Check pip version using `pip3 -V`

Note (for Ubuntu users): If the
`ModuleNotFoundError: No module named 'distutils.util'` error is encountered,
then python3-distutils needs to be installed. Install python3-distutils using
`sudo apt-get install python3-distutils`

## Mac OS X Setup

1. Create a folder where the virtual environments will reside
   `$ mkdir ~/python-envs`
1. To create a new environment named `sample-env` execute
   `$ python3 -m venv ~/python-envs/sample-env`
1. To activate the environment execute
   `$ source ~/python-envs/sample-env/bin/activate`
1. Upgrade to the latest pip version using `$ pip3 install --upgrade pip`
1. Upgrade to the latest setuptools version using
   `$ pip3 install --upgrade setuptools`
1. To deactivate the environment execute `$ deactivate` (you can reactivate the
   environment using the same `activate` command listed above)

## Ubuntu Setup

1. Install the python3-venv package using `$ sudo apt-get install python3-venv`
1. Follow the steps in the Mac OS X installation.

## Windows Setup

1. Create a folder where the virtual environments will reside `md python-envs`
1. To create a new environment named `sample-env` execute
   `python -m venv python-envs\sample-env`
1. To activate the environment execute `python-envs\sample-env\Scripts\activate`
1. Upgrade to the latest pip version using `pip install --upgrade pip`
1. To deactivate the environment execute `deactivate` (you can reactivate the
   environment using the same `activate` command listed above)

Note:

- Verify that you are using Python 3.6 or Python 3.7. Launch a command prompt
  using `cmd` and execute `python --version` to verify the version.
- Python3 installation may require admin privileges on Windows.
- This guide is for Windows 10 using a 64-bit architecture only.
