#!/usr/bin/python
# -*- coding: utf-8 -*-

def create_roles_table(testdb):
    table_name = 'IF NOT EXISTS ROLES'
    column0 = 'ID INT NOT NULL PRIMARY KEY'
    column1 = 'ROLE  CHAR(20) NOT NULL'
    columns = (column0, column1)
    testdb.create_table(table_name, columns)
    testdb.insert('ROLES', ('ID', 'ROLE'), (0, 'user'))
    testdb.insert('ROLES', ('ID', 'ROLE'), (1, 'admin'))

def create_users_table(testdb):
    table_name = 'USERS'
    column0 = 'ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY'
    column1 = 'FIRST_NAME CHAR(20) NOT NULL'
    column2 = 'LAST_NAME CHAR(20)'
    column3 = 'AGE INT'
    column4 = 'EMAIL CHAR(50) NOT NULL UNIQUE'
    column5 = 'PASSWORD CHAR(50) NOT NULL'
    column6 = 'AVATAR BLOB'
    column7 = 'ISACTIVE INT'
    column8 = 'role_id INT NOT NULL DEFAULT 0, FOREIGN KEY (role_id) REFERENCES ROLES(ID)'
    columns = (column0, column1, column2,
                column3, column4, column5,
                column6, column7, column8)
    testdb.create_table(table_name, columns)

def fill_users_table(testdb):
    testdb.insert('USERS',
        ('FIRST_NAME', 'LAST_NAME', 'AGE', 'EMAIL', 'PASSWORD'),
        ('Oleksiy', 'Shevchenko', 25, 'test1@email.com', 'test1'))

    testdb.insert('USERS',
        ('FIRST_NAME', 'LAST_NAME', 'AGE', 'EMAIL', 'PASSWORD'),
        ('Mykola', 'Sklyar', 24, 'test2@email.com', 'test2'))

    testdb.insert('USERS',
        ('FIRST_NAME', 'LAST_NAME', 'AGE', 'EMAIL', 'PASSWORD'),
        ('John', "O'Harah", 24, 'test3@email.com', 'test3'))

    testdb.insert('USERS',
        ('FIRST_NAME', 'LAST_NAME', 'AGE', 'EMAIL', 'PASSWORD'),
        ('Vivdya', "Hrinchenko", 23, 'test4@email.com', 'test4'))

    testdb.insert('USERS',
        ('FIRST_NAME', 'LAST_NAME', 'AGE', 'EMAIL', 'PASSWORD'),
        ('Olena', "Samijlenko", 26, 'test5@email.com', 'test5'))

def drop_users_table(testdb):
    cursor = testdb.db.cursor()
    cursor.execute("DROP TABLE IF EXISTS USERS")
    # del(testdb)