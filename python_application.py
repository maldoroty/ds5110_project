from mysql.connector import connect, Error
from getpass import getpass

try:
    conn = connect(
        host = 'localhost',
        user = input("Enter username: "),
        password = getpass("Enter Password: "),
        database = "new_schema"
    )
except Error as e:
    print(e)

with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM media")
    result = cursor.fetchall()
    for row in result:
        print(row)