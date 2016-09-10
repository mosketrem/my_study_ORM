# my_study_ORM
Study project with ORM object for working in Python with MySQL DB

!!! Change parameters in config.py !!!

Preparations:

Install MySQL
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install mysql-server mysql-client
$ sudo mysql_secure_installation
$ mysql -u root -p

Set the MySQL
CREATE DATABASE <DATABASE-NAME-HERE>;
CREATE USER '<user:string>'@'localhost' IDENTIFIED BY '<password:string>';
GRANT ALL ON <DATABASE-NAME-HERE>.* TO '<user:string>'@'localhost';
QUIT;

Install MySQL-python
Eigher 
sudo apt-get install python-mysqldb
or
sudo apt-get install build-essential python-dev libmysqlclient-dev
pip install MySQL-python

