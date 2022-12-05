from mysql.connector import connect, Error
from getpass import getpass
import pandas as pd

from utils.update_utils import create_update_query
from utils.insert_utils import create_insert_query
from utils.delete_utils import create_delete_query
from utils.table_utils import table_schemas, keys_for_deletion

# use pandas for result

try:
    conn = connect(
        host = "localhost",
        user = input("Enter username: "),
        password=getpass("Enter password: "),
        database = "streaming_service_db"
    )

except Error as e:
    print(e)

# hi
##inst_query = "Select * FROM instructor"
##with conn.cursor() as cursor:
##    cursor.execute(inst_query)
##    result = cursor.fetchall()
##    for row in result:
##        print(row)



def function():

##    if query_type == "look": # account of case
##        table_name = input("Enter table name: ")
##        attr_name = input("Enter attribute name: ")
##        inst_query = """
##            Select %s FROM %s"""
##        val_tuple = (attr_name, table_name)
##        with conn.cursor() as cursor:
##            cursor.execute(inst_query, val_tuple)
##            conn.commit()
##            #result = cursor.fetchall()
##            #for row in result:
##                #print(row)

    is_running = True

    while is_running:
        query_type = input("Would like to insert, delete, update, or look at the database? ")

        if query_type.lower() == "insert":
            table_name = input("Enter table name: ")
            print("This is the schema for the \"", table_name, "\"")
            print(table_schemas[table_name])
            insert_attr = input("Please enter the attributes separated by commas: ")

            attrs = insert_attr.split(",")
            
            inst_query, attrs = create_insert_query(table_name, attrs)
            attrs = tuple(attrs)
            print(inst_query)
            print(attrs)

            
            with conn.cursor() as cursor:
                cursor.execute(inst_query, attrs)
                conn.commit()
            
        elif query_type.lower() == "delete":
            table_name = input("Enter table name: ")
            print("These are the keys you must specify for delete in \"", table_name, "\"")
            print(keys_for_deletion[table_name])
            user_input = input("Please enter the keys separated by commas: ")

            keys = user_input.split(",")
            
            del_query, keys = create_delete_query(table_name, keys)
            keys = tuple(keys)
            print(del_query)
            print(keys)
            
            with conn.cursor() as cursor:
                cursor.execute(del_query, keys)
                conn.commit()

        
        elif query_type.lower() == "update":
            table_name = input("Enter table name: ")
            if table_name == "watched":
                print("Watch history cannot be changed!")
                continue

            print("This is the schema for the \"", table_name, "\"")
            print(table_schemas[table_name])
            user_input = input("Please enter the attributes separated by commas: ")

            update_params = user_input.split(",")
            
            update_query, update_params = create_update_query(table_name, update_params)
            update_params = tuple(update_params)
            print(update_query)
            print(update_params)

            
            with conn.cursor() as cursor:
                cursor.execute(update_query, update_params)
                conn.commit()

        elif query_type.lower() == "viewership":
            query = """
                SELECT *
                FROM watched w, customer c, media m
                WHERE w.c_id = c.customer_id AND
                      w.m_id = m.m_id
            """

            with conn.cursor() as cursor:
               cursor.execute(query)
               rows = cursor.fetchall()
               df = pd.DataFrame(rows)
               print(df)

        elif query_type.lower() == "look":
            table_name = input("Enter table name: ")
            if table_name not in table_schemas:
                # This if statement will guard against SQL injection
                print("There is no table called \"", table_name, "\" in the database.")
                continue

            look_query = """
               SELECT * FROM
            """
            look_query += table_name
            with conn.cursor() as cursor:
               cursor.execute(look_query)
               rows = cursor.fetchall()
               df = pd.DataFrame(rows)
               print(df)



        elif query_type.lower() == "exit":
            print("Exiting database app...")
            is_running = False

        else:
            print("Unkown command!")

function()
    
        
    
##inst_query = "Select * FROM media"
##with conn.cursor() as cursor:
##    cursor.execute(inst_query)
##    result = cursor.fetchall()
##    for row in result:
##        print(row)
