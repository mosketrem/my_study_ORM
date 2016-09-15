#!/usr/bin/python
# -*- coding: utf-8 -*-
"""docstring!!!"""

from DBModel import DBObject

TABLE = 'USERS'

class UserModel(object):
    """docstring for UserModel"""

    @staticmethod
    def all():
        """docstring!!!"""

        try:
            table_str = '%s ORDER BY ID' % TABLE
            return UserModel.list_to_users(DBObject().all(table_str))
        except Exception, e:
            print e

    @staticmethod
    def list_to_users(users_list):
        """Makes list of Users objects from list of dicts from MySQL"""

        users = []

        for line in users_list:
            user_id = line['ID']
            f_name = line['FIRST_NAME']
            l_name = line['LAST_NAME']
            age = line['AGE']
            email = line['EMAIL']
            passwrd = line['PASSWORD']
            avatar = line['AVATAR']
            is_active = line['ISACTIVE']
            role_id = line['role_id']

            user = UserModel(user_id, f_name, l_name, age,
                             email, passwrd, avatar, is_active,
                             role_id)
            users.append(user)

        return users

    def __init__(self, user_id=None, f_name=None, l_name=None,
                 age=None, email=None, passwrd=None,
                 avatar=None, is_active=1, role_id=0, ):
        super(UserModel, self).__init__()
        if f_name and email and passwrd:
            params = {'ID': user_id, 'FIRST_NAME': f_name,
                      'LAST_NAME': l_name, 'AGE': age,
                      'EMAIL': email, 'PASSWORD': passwrd,
                      'AVATAR': avatar, 'ISACTIVE': is_active,
                      'role_id': role_id}
            self.fill_fileds(params)
        elif user_id is not None:
            user_dict = {}
            users_tuple = self.get_user_by_id(user_id)
            if users_tuple:
                user_dict = users_tuple[0]
            # print user_dict
            self.fill_fileds(user_dict)

    def fill_fileds(self, user_dict):
        """docstring!!!"""

        self.id = user_dict.get('ID')
        self.f_name = user_dict.get('FIRST_NAME')
        self.l_name = user_dict.get('LAST_NAME')
        self.email = user_dict.get('EMAIL')
        self.passwrd = user_dict.get('PASSWORD')
        self.avatar = user_dict.get('AVATAR')
        self.is_active = user_dict.get('ISACTIVE', 1)
        self.role_id = user_dict.get('role_id', 0)
        self.age = user_dict.get('AGE')

    def get_user_by_id(self, user_id):
        """docstring!!!"""

        return self.get_users('ID=%s' % user_id)

    def _db(self):
        """docstring!!!"""

        return DBObject()

    def get_users(self, condition_string):
        """docstring!!!"""

        return self._db().select('*', TABLE, condition_string)

    def fields_for_sql(self):
        """docstring!!!"""

        l1 = 'FIRST_NAME="%s"' % self.f_name
        l2 = 'LAST_NAME="%s"' % self.l_name
        l3 = 'EMAIL="%s"' % self.email
        l4 = 'PASSWORD="%s"' % self.passwrd
        l5 = 'AVATAR=%s' % self.avatar
        l6 = 'ISACTIVE=%s' % self.is_active
        l7 = 'role_id=%s' % self.role_id
        l8 = 'AGE=%s' % self.age
        new_values = ', '.join((l1, l2, l3, l4, l5, l6, l7, l8))
        return new_values

    def save(self):
        """docstring!!!"""

        # update
        if self.id is not None:
            new_values = self.fields_for_sql()
            self._db().update(TABLE, new_values, 'ID=%s' % self.id)
        # create new
        else:
            columns = ('FIRST_NAME', 'LAST_NAME', 'AGE',
                       'EMAIL', 'PASSWORD', 'AVATAR',
                       'ISACTIVE', 'role_id')
            values = (self.f_name, self.l_name, self.age,
                      self.email, self.passwrd, self.avatar,
                      self.is_active, self.role_id)
            # print values
            self._db().insert(TABLE, columns, values)

    def show_fileds(self):
        """docstring!!!"""

        fields = self.fields_for_sql()
        return 'ID=%s %s' % (self.id, fields)

    def delete(self):
        """docstring!!!"""

        self.is_active = 0
        self.save()

    def __str__(self):
        return '%s %s, %s years old.' % (self.f_name, self.l_name,
                                         self.age)


if __name__ == '__main__':
    # for u in UserModel.all():
    #     print u.show_fileds()
    print UserModel(5).show_fileds()
    # print UserModel(f_name='Motrya', l_name='Kochubej',
    #               age=16, email='test6@email.com', passwrd='test6').save()
    # a = UserModel(5)
    # a.age = 30
    # a.save()
    # print a
