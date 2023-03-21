import mysql.connector


def connectDb():
    return mysql.connector.Connect(
        host="localhost",
        user="root",
        passwd="199001",
        database="task03"
    )