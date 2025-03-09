#!/usr/bin/python3
"""
Lists all states from the database in argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Script for list states in database

    Keyword arguments:
    argument -- argument for username password and name of database
    Return: return the response of script
    """

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
