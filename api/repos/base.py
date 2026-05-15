# Υλοποιεί τη διασύνδεση με τη βάση δεδομένων
import sqlite3

class BaseRepository:
    def __init__(self):
        self.apply_migrations()

    def __get_connection__(self):
        return sqlite3.connect('database.db')

    def apply_migrations(self, command: str):
        self.sql_command(command)

    def sql_command(self, command: str):
        connection = self.__get_connection__()
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
        connection.close()
    
    def sql_get_one(self, command: str):
        connection = self.__get_connection__()
        cursor = connection.cursor()
        cursor.execute(command)
        data = cursor.fetchone()
        connection.close()

        return data
    
    def sql_get_all(self, command: str):
        connection = self.__get_connection__()
        cursor = connection.cursor()
        cursor.execute(command)
        data = cursor.fetchall()
        connection.close()

        return data