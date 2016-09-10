#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from config import config_dict as cfg

class DBObject(object):
	"""docstring for DBObject"""
	def __init__(self):
		super(DBObject, self).__init__()
		self.db = MySQLdb.connect(**cfg)

	def create_table(self, table_name, columns):
		cursor = self.db.cursor()
		try:
			cursor.execute("create table %s ( %s )" % (table_name, columns))
			self.db.commit()
		except Exception, e:
			self.db.rollback()
			print e

	def insert(self, table_name, columns_string, values_string):
		cursor = self.db.cursor()
		try:
			cursor.execute("insert into %s (%s) values (%s)" % 
				(table_name, columns_string, values_string))
			self.db.commit()
			return cursor.lastrowid
		except Exception, e:
			self.db.rollback()
			print e

	def select(self, colums_str, tableS_nameS_str, condition_str):
		cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
		try:
			cursor.execute("select %s from %s where %s" % 
				(colums_str, tableS_nameS_str, condition_str))
			return cursor.fetchall()
		except Exception, e:
			print e

	def update(self, table_name, values_str, condition_str=None):
		cursor = self.db.cursor()

		if condition_str:
			condition_str = "where %s" % condition_str
		else:
			condition_str = ""

		try:
			cursor.execute("update %s set %s %s" % 
				(table_name, values_str, condition_str))
			self.db.commit()
		except Exception, e:
			self.db.rollback()
			print e

	def delete(self, table_name, condition_str):
		cursor = self.db.cursor()
		try:
			cursor.execute("delete from %s where %s" % 
				(table_name, condition_str))
			self.db.commit()
		except Exception, e:
			self.db.rollback()
			print e

	def __del__(self):
		self.db.close()

		

if __name__ == '__main__':
    testdb = DBObject()


    # cursor = testdb.db.cursor()
    # cursor.execute("DROP TABLE IF EXISTS USERS")

    # table_name = 'USERS'
    # column1 = 'FIRST_NAME  CHAR(20) NOT NULL'
    # column2 = 'LAST_NAME  CHAR(20)'
    # column3 = 'AGE INT'  
    # columns = ', '.join((column1, column2, column3))
    # testdb.create_table(table_name, columns)

    # print testdb.insert('USERS', 'FIRST_NAME, LAST_NAME, AGE',
    # 	"'Oleksiy', 'Shevchenko', 25")
    # print testdb.insert('USERS', 'FIRST_NAME, LAST_NAME, AGE',
    # 	"'Mykola', 'Sklyar', 24")

    # print 'Oleksiy is ', testdb.select('AGE', 'USERS', 
    # 								'FIRST_NAME = "Oleksiy"')

    # testdb.update('USERS', 'AGE = 26', 'FIRST_NAME = "Oleksiy"')
    # print 'Oleksiy is ', testdb.select('AGE', 'USERS', 
    # 								'FIRST_NAME = "Oleksiy"')

    # testdb.delete('USERS', 'FIRST_NAME = "Oleksiy"')
    # print 'Oleksiy is ', testdb.select('AGE', 'USERS', 
    # 								'FIRST_NAME = "Oleksiy"')

    print('Disconnected from database')