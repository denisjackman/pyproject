# Installation Instructions

## Environment

1. Install [Python](https://www.python.org/)
2. Install [MySql](https://dev.mysql.com/)
3. Install [Git](https://git-scm.com/) locally
4. Install and IDE or Editor of choice (I use [Visual Studio Code](https://code.visualstudio.com/))
5. Make sure you have a [GitHub](https://github.com) presence

## MySql Specific Items

* Create a database `CREATE DATABASE databasename;`
* Create a user `CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';`
* Grant permissions to the user `GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT  on *.* TO 'username'@'hostname' WITH GRANT OPTION;`

## Environment Specific Items

This sequence will allow you to access anything that needs privileges. And should protect your details at the same time.

* Copy `credentials-template.json` to 'secrets.json'
* Update the details inside as required
* set up `.gitignore` file. Make sure `secrets.json` is in there.

## Python Specific Items

* set up a virtual environment 
* activate the virtual environment
* install everything on the `requirements.txt`

for Windows

* `python -m venv name-env`
* `name-env\Scripts\activate.bat`
* `pip install -r requirements.txt`
