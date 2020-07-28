#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
from pymysql.cursors import DictCursor
import unittest
class TestCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.__connection = pymysql.connect(
            host='localhost',
            user='root',
            password='FhJ2mn3dweqgE##',
            db='library',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        self.name = "Alan"
        self.number = "716984365"

    def test_creature(self):
        with self.__connection.cursor() as cursor:
            sql = f"INSERT INTO library.library (name, number) values ('{self.name}', '{self.number}');"
            cursor.execute(sql)
            self.__connection.commit()

    def test_reading(self):
        with self.__connection.cursor() as cursor:
            sql = "SELECT * FROM `library`.`library`"
            cursor.execute(sql)
            for row in cursor:
                print(row)

    def test_update(self):
        id = 2
        with self.__connection.cursor() as cursor:
            sql = f"UPDATE library.library SET name= '{self.name}',number='{self.number}' WHERE id={id}"
            cursor.execute(sql)
            self.__connection.commit()

    def test_delete(self):
        with self.__connection.cursor() as cursor:
            sql = "SELECT * FROM `library`.`library`"
            cursor.execute(sql)
            id = cursor.rowcount
            sql = f"DELETE FROM `library`.`library` WHERE id={id}"
            cursor.execute(sql)
            self.__connection.commit()

    def search(self):
        sear = "Lar"
        with self.__connection.cursor() as cursor:
            sql = f"SELECT * FROM `library`.`library` WHERE concat(name,number) LIKE '%{sear}%'"
            cursor.execute(sql)
            for row in cursor:
                print(row)

    @classmethod
    def tearDownClass(self):
        self.__connection.close()


if __name__ == '__main__':
    unittest.main()