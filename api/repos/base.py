# Υλοποιεί τη διασύνδεση με τη βάση δεδομένων
import sqlite3

class BaseRepository:
    def __init__(self):
        self.apply_migrations()

    def apply_migrations(self, command: str):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
        connection.close()

    def get_connection(self):
        return sqlite3.connect('database.db')
