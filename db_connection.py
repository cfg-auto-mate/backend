from mysql.connector import connect


def db_connection():
    connection = connect(
        host='localhost',
        user='root',
        password='Husksql91',
        database='charge_and_go')
    return connection

