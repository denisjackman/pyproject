
# MYSQL

## Overview

This section covers how to perform mysql database operations using MySQL in Python.

## References
* [tutorial](https://www3.ntu.edu.sg/home/ehchua/programming/sql/MySQL_Beginner.html)
* [Official Tutorial](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/)
* [Example Data](https://electrictoolbox.com/mysql-example-table/)
* [example database](https://www.mysqltutorial.org/mysql-sample-database.aspx)
* [Example database 2](https://dev.mysql.com/doc/employee/en/)
* [Example database 3](https://www3.ntu.edu.sg/home/ehchua/programming/sql/SampleDatabases.html)
* [Remote access](https://www.digitalocean.com/community/tutorials/how-to-allow-remote-access-to-mysql)
* [example database 4](https://www.sqlservertutorial.net/sql-server-sample-database/)
* [Intro Session](https://realpython.com/python-mysql/)
* [MySQL example database code](https://github.com/datacharmer/test_db.git)
* [MySQL example database docs](https://dev.mysql.com/doc/employee/en/)

## Code
### Admin Stuff

`use mysql;`
`select user ,grant_priv from user ;`
`update user set host ='%' where user = 'root';`
`flush privileges;`
`grant all privileges on *.* to 'root'@'%' ;`

### Create database
`create database testdb;`
`create database test;`

### Create Users
`create user 'jackmanimation'@'localhost' identified by 'password';`
`create user 'jackmanimation'@'Denis-PC.lan' identified by 'password';`
`create user 'jackmanimation'@'Gerialt.lan' identified by 'password'`
`create user 'jackmanimation'@'%' identified by 'password';`

### Basics
`use testdb;`
`use test;`

### Privileges
`grant select, insert, update on testdb.* to 'jackmanimation'@'localhost' with grant option;`
`grant select, insert, update on testdb.* to 'jackmanimation'@'Denis-PC.lan' with grant option;`
`grant select, insert, update on testdb.* to 'jackmanimation'@'Gerialt.lan' with grant option;`
`grant select, insert, update on testdb.* to 'jackmanimation'@'%' with grant option;`

`grant select, insert, update on test.* to 'jackmanimation'@'localhost' with grant option;`
`grant select, insert, update on test.* to 'jackmanimation'@'Denis-PC.lan' with grant option;`
`grant select, insert, update on test.* to 'jackmanimation'@'Gerialt.lan' with grant option;`
`grant select, insert, update on test.* to 'jackmanimation'@'%' with grant option;`

`grant select, insert, update on employees.* to 'jackmanimation'@'localhost' with grant option;`
`grant select, insert, update on employees.* to 'jackmanimation'@'Denis-PC.lan' with grant option;`
`grant select, insert, update on employees.* to 'jackmanimation'@'Gerialt.lan' with grant option;`
`grant select, insert, update on employees.* to 'jackmanimation'@'%' with grant option;`

`grant select, insert, update on classicmodels.* to 'jackmanimation'@'localhost' with grant option;`
`grant select, insert, update on classicmodels.* to 'jackmanimation'@'Denis-PC.lan' with grant option;`
`grant select, insert, update on classicmodels.* to 'jackmanimation'@'Gerialt.lan' with grant option;`
`grant select, insert, update on classicmodels.* to 'jackmanimation'@'%' with grant option;`

`grant select, insert, update on meerkatbot.* to 'jackmanimation'@'localhost' with grant option;`
`grant select, insert, update on meerkatbot.* to 'jackmanimation'@'Denis-PC.lan' with grant option;`
`grant select, insert, update on meerkatbot.* to 'jackmanimation'@'Gerialt.lan' with grant option;`
`grant select, insert, update on meerkatbot.* to 'jackmanimation'@'%' with grant option;`

### Test databases
`CREATE TABLE IF NOT EXISTS 'fruit' (`
`  'fruit_id' int(10) unsigned NOT NULL auto_increment,`
`  'name' varchar(50) NOT NULL,`
`  'variety' varchar(50) NOT NULL,`
`  PRIMARY KEY  ('fruit_id')`
`);`

`INSERT INTO 'fruit' ('fruit_id', 'name', 'variety') VALUES`
`(1, 'Apple', 'Red Delicious'),`
`(2, 'Pear', 'Comice'),`
`(3, 'Orange', 'Navel'),`
`(4, 'Pear', 'Bartlett'),`
`(5, 'Orange', 'Blood'),`
`(6, 'Apple', 'Cox''s Orange Pippin'),`
`(7, 'Apple', 'Granny Smith'),`
`(8, 'Pear', 'Anjou'),`
`(9, 'Orange', 'Valencia'),`
`(10, 'Banana', 'Plantain'),`
`(11, 'Banana', 'Burro'),`
`(12, 'Banana', 'Cavendish');`


CREATE TABLE `meerkatbot`.`posts` ( `username` TEXT NOT NULL , `postdate` DATE NOT NULL) ENGINE = InnoDB;