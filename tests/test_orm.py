#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import MySQLdb
from DBModel import DBObject
from config import config_dict
DB_NAME = 'TEST'

class DBObjectTest(unittest.TestCase):

    def setUp(self):
        db = MySQLdb.connect(**config_dict)
        cursor = db.cursor()
        cursor.execute('CREATE DATABASE %s' % DB_NAME)
        db.commit()
        db.close()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()