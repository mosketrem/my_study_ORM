#!/usr/bin/python
# -*- coding: utf-8 -*-

"""The help script for setting the DB if it's not created yet"""

if __name__ == '__main__':
    from DBModel import DBObject
    import utils

    testdb = DBObject()

    utils.create_roles_table(testdb)
    utils.create_users_table(testdb)
    utils.fill_users_table(testdb)

    print 'done!'
