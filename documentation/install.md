# Installation Instructions

## Environment
1. Install [Python](https://www.python.org/)
2. Install [MySql](https://dev.mysql.com/)
3. Install [Git](https://git-scm.com/) locally
4. Install and IDE or Editor of choice (I use [ATOM](https://atom.io/))
5. Make sure you have a [GitHub](https://github.com) presence

## MySql Specific Items
1. Create a database
`CREATE DATABASE databasename;`
2. Create a user
`CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';`
3. Grant permissions to the user
`GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT  on *.* TO 'username'@'hostname' WITH GRANT OPTION;`

## Environment Specific Items
This sequence will allow you to access anything that needs privileges. And should protect your details at the same time.

1. Copy `credentials-template.json` to 'credentials.json'
2. Update the details inside as required
3. Set up `.gitignore` file. Make sure `credentials.json` is in there.

## Python Specific Items
1. Install MySql Module (`pip install mysql-connector-python`)
