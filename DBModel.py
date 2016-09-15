#!/usr/bin/python
# -*- coding: utf-8 -*-
"""docstring!!!"""

import MySQLdb
from config import config_dict as cfg


class DBObject(object):
    """docstring for DBObject"""

    def __init__(self):
        super(DBObject, self).__init__()
        self.db = MySQLdb.connect(**cfg)

    def create_table(self, table_name, columns_list):
        """docstring!!!"""

        cursor = self.db.cursor()
        columns = ', '.join(columns_list)
        try:
            cursor.execute("create table %s ( %s )" % (table_name, columns))
            self.db.commit()
        except Exception, e:
            self.db.rollback()
            print e

    def insert(self, table_name, columns_list, values_list):
        """docstring!!!"""

        cursor = self.db.cursor()
        columns = ', '.join(columns_list)
        values = self._strfy_tuple(values_list)
        # print values
        try:
            cursor.execute("insert into %s (%s) values %s" %
                           (table_name, columns, values))
            self.db.commit()
            return cursor.lastrowid
        except Exception, e:
            self.db.rollback()
            print e

    def select(self, colums_str, tableS_nameS_str, condition_str):
        """docstring!!!"""

        cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        if condition_str:
            condition_str = 'where %s' % condition_str
        try:
            cursor.execute("select %s from %s %s" %
                           (colums_str, tableS_nameS_str, condition_str))
            return cursor.fetchall()
        except Exception, e:
            print e

    def all(self, table_str, condition=''):
        """docstring!!!"""

        return self.select('*', table_str, condition)

    def update(self, table_name, values_str, condition_str=None):
        """docstring!!!"""

        cursor = self.db.cursor()
        # print values_str
        values_str = values_str.replace('None', 'NULL')
        # print values_str
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
        """docstring!!!"""

        cursor = self.db.cursor()
        try:
            cursor.execute("delete from %s where %s" %
                           (table_name, condition_str))
            self.db.commit()
        except Exception, e:
            self.db.rollback()
            print e

    def _strfy_tuple(self, vals):
        """(self, tuple) -> string

        Return the string presentation of tuple
        for our sql query.
        """

        # add quotes around string values
        vals = ('"%s"' % x if isinstance(x, str) else x for x in vals)
        # make all elements strings (for using the new list
        # of string in ', '.join() expression)
        vals = [str(x) for x in vals]
        # replace None with NULL
        vals = [x if x != 'None' else 'NULL' for x in vals]
        # make one string with coma separation
        vals = ', '.join(vals)
        # add brackets around it and return
        return '(%s)' % vals

    def __del__(self):
        self.db.close()


if __name__ == '__main__':
    testdb = DBObject()

    # import utils
    # utils.create_roles_table(testdb)
    # utils.drop_users_table(testdb)

    # utils.create_users_table(testdb)
    # utils.fill_users_table(testdb)

    # print 'Oleksiy is ', testdb.select('AGE', 'USERS',
    #                                 'FIRST_NAME = "Oleksiy"')

    # testdb.update('USERS', 'AGE = 26', 'FIRST_NAME = "Oleksiy"')
    # print 'Oleksiy is ', testdb.select('AGE', 'USERS',
    #                                 'FIRST_NAME = "Oleksiy"')

    # testdb.delete('USERS', 'FIRST_NAME = "Oleksiy"')
    # print 'Oleksiy is ', testdb.select('AGE', 'USERS',
    #                                 'FIRST_NAME = "Oleksiy"')

    # print 'All users '
    # for one in testdb.all('USERS ORDER BY ID'):
    #   print one, '\n'

    print 'Disconnected from database'
