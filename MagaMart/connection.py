import mysql.connector
from mysql.connector import Error


def connect_db():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='mma',
                                             user='root',
                                             password='')
        return connection
    except Error as e:
        print('connection failed', e)


def close_con(con, cur):
    cur.close()
    con.close()
