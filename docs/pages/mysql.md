
# MYSQL

## Overview

This section covers how to perform mysql database operations using MySQL in Python.

## References

* [Tutorial](https://www3.ntu.edu.sg/home/ehchua/programming/sql/MySQL_Beginner.html)
* [Official Tutorial](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/)
* [Example Data](https://electrictoolbox.com/mysql-example-table/)
* [example database](https://www.mysqltutorial.org/mysql-sample-database.aspx)
* [Example database 2](https://dev.mysql.com/doc/employee/en/)
* [Example database 3](https://www3.ntu.edu.sg/home/ehchua/programming/sql/SampleDatabases.html)
* [Remote access](https://www.digitalocean.com/community/tutorials/how-to-allow-remote-access-to-mysql)
* [Example database 4](https://www.sqlservertutorial.net/sql-server-sample-database/)
* [Intro Session](https://realpython.com/python-mysql/)
* [MySQL example database code](https://github.com/datacharmer/test_db.git)
* [MySQL example database docs](https://dev.mysql.com/doc/employee/en/)

## Learning Sites

* **SQLZoo**: [SQLZoo](https://sqlzoo.net/wiki/SQL_Tutorial) is a popular site for learning SQL. It offers a range of tutorials and exercises to help you understand the fundamentals and more advanced aspects of SQL. The interactive tutorials cover various topics, from basic SELECT statements to complex JOIN operations. Each tutorial includes practical exercises that you can complete directly in your browser, making it easy to apply what you’ve learned.
* **W3Schools SQL Tutorial**:  [W3Schools](https://www.w3schools.com/sql/) is a well-known educational website that provides tutorials on various programming languages and technologies. Their SQL tutorial is comprehensive and user-friendly, suitable for beginners and those looking to refresh their skills. The site includes explanations of SQL syntax, examples, and exercises that you can try out in the interactive SQL editor.
* **SQLFiddle**: [SQLFiddle](https://sqlfiddle.com/) is a fantastic tool for testing and sharing SQL queries. It allows you to create schemas, run queries, and share your SQL work with others. This makes it an excellent resource for experimenting with different SQL queries and seeing how they work in real-time.
* **SQL Pad**: [SQL Pad](https://sqlpad.io/playground/mysql/) offers a playground where you can write and run SQL queries against a live database. It’s a great way to practice writing SQL queries in a real-world environment. The site also includes sample databases and queries to help you get started. Whether you’re a beginner or an advanced user, SQL Pad provides a practical way to improve your SQL skills.
* **LeetCode**: [LeetCode](https://leetcode.com/problemset/database/) is widely known for its coding challenges, but it also offers a dedicated section for database problems. The SQL problems on LeetCode range from easy to hard, providing a broad spectrum of challenges to test your skills.

## Data Sources

* **[NASA](https://data.nasa.gov/)**:  **Type of data**: Space **Access**: Mostly free, no registration required
* **[Data.gov](https://data.gov/)**: **Type of data**: Government **Access**: Free, no registration required
* **[Datahub.io](https://datahub.io/)**: **Type of data**: Business and finance **Access**: Mostly free, no registration required
* **[Google Dataset Search](https://datasetsearch.research.google.com/)**: **Type of data**: Miscellaneous **Access**: Free to search, some results may require a fee
* **[Amazon Registry of Open Data](https://registry.opendata.aws/)**: **Type of data**: Miscellaneous **Access**: Mostly free, no registration required
* **[Global Health Observatory Data Repository](https://www.who.int/data)**: **Type of data**: Health **Access**: Mostly free, no registration required

## Code

### Admin Stuff

* `use mysql;`
* `select user ,grant_priv from user ;`
* `update user set host ='%' where user = 'root';`
* `flush privileges;`
* `grant all privileges on *.* to 'root'@'%' ;`

### Create database

* `create database testdb;`
* `create database test;`

### Create Users

* `create user 'jackmanimation'@'localhost' identified by 'password';`
* `create user 'jackmanimation'@'Denis-PC.lan' identified by 'password';`
* `create user 'jackmanimation'@'Gerialt.lan' identified by 'password'`
* `create user 'jackmanimation'@'%' identified by 'password';`

### Basics

* `use testdb;`
* `use test;`

### Privileges

* `grant select, insert, update on testdb.* to 'jackmanimation'@'localhost' with grant option;`
* `grant select, insert, update on testdb.* to 'jackmanimation'@'Denis-PC.lan' with grant option;`
* `grant select, insert, update on testdb.* to 'jackmanimation'@'Gerialt.lan' with grant option;`
* `grant select, insert, update on testdb.* to 'jackmanimation'@'%' with grant option;`

* `grant select, insert, update on test.* to 'jackmanimation'@'localhost' with grant option;`
* `grant select, insert, update on test.* to 'jackmanimation'@'Denis-PC.lan' with grant option;`
* `grant select, insert, update on test.* to 'jackmanimation'@'Gerialtgrant select, insert, update on test.* to 'jackmanimation'@'%' with grant option;.lan' with grant option;`

* `grant select, insert, update on employees.* to 'jackmanimation'@'localhost' with grant option;`
* `grant select, insert, update on employees.* to 'jackmanimation'@'Denis-PC.lan' with grant option;`
* `grant select, insert, update on employees.* to 'jackmanimation'@'Gerialt.lan' with grant option;`
* `grant select, insert, update on employees.* to 'jackmanimation'@'%' with grant option;`

* `grant select, insert, update on classicmodels.* to 'jackmanimation'@'localhost' with grant option;`
* `grant select, insert, update on classicmodels.* to 'jackmanimation'@'Denis-PC.lan' with grant option;`
* `grant select, insert, update on classicmodels.* to 'jackmanimation'@'Gerialt.lan' with grant option;`
* `grant select, insert, update on classicmodels.* to 'jackmanimation'@'%' with grant option;`

* `grant select, insert, update on meerkatbot.* to 'jackmanimation'@'localhost' with grant option;`
* `grant select, insert, update on meerkatbot.* to 'jackmanimation'@'Denis-PC.lan' with grant option;`
* `grant select, insert, update on meerkatbot.* to 'jackmanimation'@'Gerialt.lan' with grant option;`
* `grant select, insert, update on meerkatbot.* to 'jackmanimation'@'%' with grant option;`

### Test databases

`CREATE TABLE IF NOT EXISTS 'fruit' (`
`'fruit_id' int(10) unsigned NOT NULL auto_increment,`
`'name' varchar(50) NOT NULL,`
`'variety' varchar(50) NOT NULL,`
`PRIMARY KEY  ('fruit_id')`
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

`CREATE TABLE 'meerkatbot'.'posts' ( 'username' TEXT NOT NULL , 'postdate' DATE NOT NULL) ENGINE = InnoDB;`
