# pyproject

## Introduction

This is a personal python project. It is designed to get me back into
development work. It is also about developing my GitHub profile a bit more.
So with that in mind. You are ensourgaged to Fork , Pull , copy and use this
as you see fit. I will document the work and how to set it up.

## Installation

use standard git clone command to get the project.
use standard python3 command to run the project.

## Usage

look at the code for examples

## Hints

when doing a change it is a good idea to lint it using *flake8* and *pylint*.

* `pylint CODE.py`
* `flake8 CODE.py`

if these throw up any issues then it needs to be addressed before commiting.
before running the code ensure that the virtual environment is set up.
and the python path is set to the virtual environment.

``export PYTHONPATH=$PYTHONPATH:`pwd` ``

finally do a test run of the code 

`python3 CODE.py`

## Utility

These command precheck the complete code repository locally prior to commiting it to the repository.

` flake8 $(git ls-files | grep .py$) > ./mnt/y/store/flake8.txt `

` pylint $(git ls-files | grep .py$) > ./mnt/y/store/pylint.txt `
