"""Snippets for interacting with a MySQL database"""

import pymysql #tested with PyMySQL==0.6.7

"""MySQL host"""
HOST = ''
"""The port that MySQL is listening on"""
PORT = 3306
"""The database user to connect as"""
USER = ''
"""The password of the database user"""
PASSWD = ''
"""The MySQL database to query"""
DB = ''

# Connect to the database.
conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB)

# Acquire a cursor.
with conn.cursor() as cursor:
    # The sql query to executed against the MySQL database.
    sql = ''
    # Execute sql. The second parameter can be a tuple to substitute into the placeholders in 'sql'.
    cursor.execute(sql, ())

    # (Only if selecting) Iterate over the results
    for row in cursor.fetchall():
        # row is a list of column values in the current database row
        print(row)
    
    
