from mysql.connector import connect, Error
from getpass import getpass

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


##inst_query = "Select * FROM instructor"
##with conn.cursor() as cursor:
##    cursor.execute(inst_query)
##    result = cursor.fetchall()
##    for row in result:
##        print(row)

table_schemas = {"customer" : "customer_id: int | name: varchar(20) | email: varchar(30) | username: varchar(30) | password: varchar(20) | credit_card: int",
                 "actors" : "a_id: int | name: varchar(20) | ranks: int",
                 "directors" : "d_id: int | name: varchar(20) | ranks: int",
                 "media" : "m_id: int | d_id: int | a_id: int | title: varchar(20) | type: varchar(20) | g_id: int",
                 "rating" : "m_id: int | rating: decimal(2, 1)",
                 "genre" : "g_id: int | genre_name: varchar(10)",
                 "subscription_plan" : "s_type: varchar(20) | price: decimal(4, 2)",
                 "subscription" : "s_id: int | start_sub: date | end_sub: date | customer_id: int | s_type: varchar(20)",
                 "trending_list" : "ranks: int | m_id: int",
                 "soundtracks" : "st_id: int | composer: varchar(20) | title varchar(40) | m_id: int",
                 "recently_added" : "m_id: int | add_date: date",
                 "leaving_soon" : "m_id: int | removal_date: date",
                 "production_company" : "p_id: int | name: varchar(40) | m_id: int",
                 "contract" : "contract_id: int | p_id: int | amount: int",
                 "movies_watched" : "c_id: int | m_id: int"}

def function():
    query_type = input("Would like to insert, delete, update, or look at the database? ")

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

    if query_type == "insert":
        table_name = input("Enter table name: ")
        print("This is the schema for the \"", table_name, "\"")
        print(table_schemas[table_name])
        insert_attr = input("Please enter the attributes separated by commas: ")

        attrs = insert_attr.split(",")
        
        # attr_name = input("Enter attribute name: ")
        inst_query = """
            INSERT INTO %s
            VALUES (
        """
        for idx, attr in enumerate(attrs):
            inst_query += "%s"
            if idx != len(attrs) - 1:
                inst_query += ", "
            
        inst_query += ")"
        attrs = tuple([table_name] + attrs)
        print(inst_query)
        print(attrs)
##        val_tuple = (table_name, insert_attr)
        with conn.cursor() as cursor:
            cursor.execute(inst_query, attrs)
            conn.commit()
        
    if query_type == "delete":
        inst_query = """
            DELETE FROM customer
            VALUES (%s, %s, %s, %s, %s, %s)
        """
    else:
        return #query_type == "update":

function()
    
        
    
##inst_query = "Select * FROM media"
##with conn.cursor() as cursor:
##    cursor.execute(inst_query)
##    result = cursor.fetchall()
##    for row in result:
##        print(row)
