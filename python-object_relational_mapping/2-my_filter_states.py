#!/usr/bin/python3
"""
search a state in database
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

    username, password, database = sys.argv[1], sys.argv[2],
    sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
