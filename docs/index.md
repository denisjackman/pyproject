# PyProject by Jackmanimation

## Overview

This personal project stores various Python snippets that I am working on. It utilizes several GitHub actions and will be continuously updated. It is designed to get me back into
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

## Snippets

- **Discord**: A simple bot that responds to server activities.
- **Excel**: Read and write operations on MS Excel spreadsheets.
- **Slack**: A bot to broadcast messages to multiple channels.
- **Spotify**: Using the web API to control Spotify.
- **YAML**: YAML file operations.
- **Trello**: Interaction with Trello using Python.
- **MySQL**: Database operations with MySQL.
- **PyGame**: Creating a scrolling background.
- **Pandas**: handling and management of large data
- **Matplotlib**: visualising data sets

## GitHub Actions

### code_linting

Code is checked with PyLint and Flake8 upon commit to ensure quality.

### pages-build-deployment

This action builds and deploys the GitHub Pages site upon each commit.

## Tools

- Pathmaker : Pathmaker is a tool I have developed to help me with my building paths for python games
- SpriteChecker: SpriteChecker is a tool I have developed to help with looking at sprites
- SpriteSheet: SpriteSheet is a tool I have developed to help with unpacking SpriteSheets into individual sprites

## Current Project Status

- [![Linting (Pylint & Flake8)](https://github.com/denisjackman/pyproject/actions/workflows/code_linting.yml/badge.svg)](https://github.com/denisjackman/pyproject/actions/workflows/code_linting.yml)
- [![pages-build-deployment](https://github.com/denisjackman/pyproject/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/denisjackman/pyproject/actions/workflows/jekyll-gh-pages.yml)

