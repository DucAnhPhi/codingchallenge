import sqlite3
from sqlite3 import Error

class Database(object):
    def __init__(self, db_file):
        # create a database connection to a SQLite database
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
    
    def create_palindrome_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE palindromes
        (num integer, palindrome integer, cycles integer) 
        ''')
        self.conn.commit()
    
    def add_palindrome(self, num, palindrome, cycles):
        c = self.conn.cursor()
        c.execute('''INSERT INTO palindromes VALUES
        ({}, {}, {})
        '''.format(num, palindrome, cycles))
        self.conn.commit()
    
    def show_all(self):
        c = self.conn.cursor()
        c.execute('''SELECT * FROM palindromes
        ''')
        print(c.fetchall())