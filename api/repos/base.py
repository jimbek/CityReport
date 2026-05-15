# Υλοποιεί τη διασύνδεση με τη βάση δεδομένων
import sqlite3

class BaseRepository:
    def __init__(self):
        pass
    
    def apply_migrations(self, command: str):
        self.sql_command(command)
    
    def seed_db(self, command: str):
        commands = command.split(';')

        for command in commands:
            self.sql_command(command)

    def __get_connection__(self):
        return sqlite3.connect('database.db')

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