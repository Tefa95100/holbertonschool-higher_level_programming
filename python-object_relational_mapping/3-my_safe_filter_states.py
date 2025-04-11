#!/usr/bin/python3
"""
Safe script to filter states by name using parameterized
queries to prevent SQL injection.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Search a states

    Keyword arguments:
    argument -- argument for username password and name of database
    and states search
    Return: return the response of script
    """

    username, password, database, state = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
