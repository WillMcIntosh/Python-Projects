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


# connect to db and create books table if it does not already exist
def connect():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, \
            title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

# create an entry
def insert(title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year,
        isbn))
    conn.commit()
    conn.close()

# view all entries
def view():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

# search for an entry (pass empty params so user can choose which to search)
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR \
            isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# update an entry
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE \
            id=?", (title, author, year, isbn,id))
    conn.commit()
    conn.close()

# delete an entry
def delete(id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()


connect()
# insert("Hamlet", "Billy Shakespeare", 1600, 123123123)
# print(view())
# update(2, "All About Me", "Will McIntosh", 2018, 10000001)
# print(search(author="John Smith"))
# delete(5)
# print(view())


