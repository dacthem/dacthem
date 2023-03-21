import mysql.connector


def connectDb():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="199001",
        database="task04"
    )