#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
from pymysql.cursors import DictCursor
import unittest


class mySQLrequests(object):
    def __init__(self):
        self.__connection = pymysql.connect(
            host='localhost',
            user='root',
            password='FhJ2mn3dweqgE##',
            db='library',
            charset='utf8mb4',
            cursorclass=DictCursor
        )

    def creature(self,name,number):
        with self.__connection.cursor() as cursor:
            sql = f"INSERT INTO library.library (name, number) values ('{name}', '{number}');"
            cursor.execute(sql)
            self.__connection.commit()

    def reading(self):
        with self.__connection.cursor() as cursor:
            sql = "SELECT * FROM `library`.`library`"
            cursor.execute(sql)
            for row in cursor:
                print(row)

    def update(self,id,name,number):
        with self.__connection.cursor() as cursor:
            sql = f"UPDATE library.library SET name= '{name}',number='{number}' WHERE id={id}"
            cursor.execute(sql)
            self.__connection.commit()

    def delete(self,id):
        with self.__connection.cursor() as cursor:
            sql = f"DELETE FROM `library`.`library` WHERE id={id}"
            cursor.execute(sql)
            self.__connection.commit()

    def search(self,sear):
        with self.__connection.cursor() as cursor:
            sql = f"SELECT * FROM `library`.`library` WHERE concat(name,number) LIKE '%{sear}%'"
            cursor.execute(sql)
            for row in cursor:
                print(row)

    def closet(self):
        self.__connection.close()







p = mySQLrequests()
p.creature("Nikita","716984365")
p.update(3,"Larisa","716984365")
p.reading()
p.delete(1)
p.search("Ali")
p.closet()

