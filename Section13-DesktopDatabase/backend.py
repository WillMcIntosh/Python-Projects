"""
back end for a simple desktop database that stores book info:
    Title, Author
    Year, ISBN

User can:
    View all records
    search and entry
    add entry
    update entry
    delete entry
"""

import sqlite3

class Database:
    # connect to db and create books table if it does not already exist
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, \
                title text, author text, year integer, isbn integer)")
        self.conn.commit()

    # create an entry
    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year,
            isbn))
        self.conn.commit()

    # view all entries
    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    # search for an entry (pass empty params so user can choose which to search)
    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR \
                isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    # update an entry
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE \
                id=?", (title, author, year, isbn,id))
        self.conn.commit()

    # delete an entry
    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
