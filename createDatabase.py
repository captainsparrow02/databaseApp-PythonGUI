#!/usr/bin/env python3

import sqlite3 # Importing sqlite3 built-in package.

# Create a database or connect to one.
conn = sqlite3.connect('address_book.db') # Passing the name of the database that needs to be created.

# Create a cursor which will help us interract with our database.
c = conn.cursor()

# Creating a table.
c.execute('''CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)
''')

# Commit changes made in database.
conn.commit()

# Closing connection.
conn.close()
