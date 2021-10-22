"""Snippet for querying a sqlite3 database."""
import sqlite3

"""This is the absolute or relative path to your sqlite file"""
PATH_TO_SQLITE_FILE = ''
"""The SQL query that you intend to run. Parameter placeholders are question marks (?)."""
SQL_QUERY = 'SELECT * FROM banned WHERE host = ?'
""" The value of parameters to the SQL query. This should be a tuple with the same number of elements as there are placeholders in the SQL"""
QUERY_PARAMS = ('123',)

# Create a connection to the db
with sqlite3.connect(PATH_TO_SQLITE_FILE) as con:
    try:
        # create cursor
        cur = con.cursor()
        # execute query and iterate over results
        for row in cur.execute(SQL_QUERY, QUERY_PARAMS):
            # row is an array where each element is a column from the query.
            print(row)
        cur.close()
    except sqlite3.Error as e:
        # Handle error
        pass
