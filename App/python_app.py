from mysql.connector import connect, Error
from getpass import getpass
from tabulate import tabulate

from utils.update_utils import create_update_query
from utils.insert_utils import create_insert_query
from utils.delete_utils import create_delete_query
from utils.table_utils import table_schemas, keys_for_deletion, views, sub_types

# use pandas for result



def main(conn):

    is_running = True

    while is_running:
        print("")
        query_type = input("Please enter a command, or enter 'help' to see list of available commands.\n> ")
        query = ""
        params = tuple()
        print_result = False
        should_commit = True

        if query_type.lower() == "help":
            print("Available Commands:")
            print("-------------------")
            print("     insert  :  insert data into a table")
            print("     delete  :  remove data from a table")
            print("     update  :  modify existing data in a table")
            print("     viewership  :  view information about users and the media they have recently consumed")
            print("     contract eval : view information about contract success")
            print("     customer usage : view information about customer activity")
            print("     look  :   get all data from a certain table")
            print("     get_money   :   gets the total amount money earned by a production company")
            print("     count_of_media   :   counts the amount of movies or TV shows")
            print("     count_of_subscription   :   returns the number of subscriptions with the given subscription type")
            print("     exit  :   logout of this app")

        elif query_type.lower() == "insert":
            table_name = input("Enter table name: ")
            if table_name not in table_schemas:
                print("There is no table called \"", table_name, "\" in the database.")
                continue
            print("This is the schema for the \"", table_name, "\"")
            print(table_schemas[table_name])

            insert_attr = input("Please enter the attributes separated by commas: ")
            attrs = insert_attr.split(",")
            query, attrs = create_insert_query(table_name, attrs)
            params = tuple(attrs)

            
        elif query_type.lower() == "delete":
            table_name = input("Enter table name: ")
            if table_name not in table_schemas:
                print("There is no table called \"", table_name, "\" in the database.")
                continue
            print("These are the keys you must specify for delete in \"", table_name, "\"")
            print(keys_for_deletion[table_name])

            user_input = input("Please enter the keys separated by commas: ")
            keys = user_input.split(",")
            query, keys = create_delete_query(table_name, keys)
            params = tuple(keys)

        
        elif query_type.lower() == "update":
            table_name = input("Enter table name: ")
            if table_name not in table_schemas:
                # This if statement will guard against SQL injection
                print("There is no table called \"", table_name, "\" in the database.")
                continue
            elif table_name == "watched":
                print("Watch history cannot be changed!")
                continue

            print("This is the schema for the \"", table_name, "\"")
            print(table_schemas[table_name])
            user_input = input("Please enter the attributes separated by commas: ")
            update_params = user_input.split(",")
            query, update_params = create_update_query(table_name, update_params)
            params = tuple(update_params)


        elif query_type.lower() == "viewership":
            query = """
                SELECT c.customer_id, c.name, c.email, c.username, m.title, a.name AS actor, d.name AS director, m.type, g.genre_name AS genre
                FROM watched w, customer c, media m, actors a, directors d, genre g
                WHERE w.c_id = c.customer_id AND w.m_id = m.m_id AND m.a_id = a.a_id AND m.d_id = d.d_id and m.g_id = g.g_id
            """
            print_result = True
            should_commit = False
           
        elif query_type.lower() == "contract eval":
            query = """
                SELECT p.name as production_company, m.title as media_title, c.amount as $, count(w.m_id) as watch_count
                FROM contract c, production_company p, media m
                LEFT OUTER JOIN watched w 
                ON w.m_id = m.m_id
                WHERE c.p_id = p.p_id AND m.m_id = p.m_id
                GROUP BY production_company, media_title, $
            """
            print_result = True
            should_commit = False
          
        elif query_type.lower() == "customer usage":
            query = """
                SELECT c.name, c.email, c.credit_card, s.start_sub, s.end_sub, s.s_type as sub_type, p.price, count(w.m_id) as media_watched
                FROM subscription s, subscription_plan p, customer c
                lEFT OUTER JOIN watched w
                ON w.c_id = c.customer_id
                WHERE s.s_type = p.s_type AND s.customer_id = c.customer_id
                GROUP BY c.name, c.email, c.credit_card, s.start_sub, s.end_sub, sub_type, p.price
            """
            print_result = True
            should_commit = False

        elif query_type.lower() == "look":
            name = input("Enter table name: ")
            if name not in table_schemas and name not in views:
                # This if statement will guard against SQL injection
                print("There is no table or view called \"", name, "\" in the database.")
                continue

            query = """
               SELECT * 
               FROM
            """
            query += name
            print_result = True
            should_commit = False

        elif query_type.lower() == "get_money":
            prod_company = input("Please enter a name of a production company: ")
            query = """
                SELECT get_money(%s);
            """
            params = (prod_company, )
            print_result = True
            should_commit = False


        elif query_type.lower() == "count_of_media":
            media_type = input("Please enter a media type (\"Movie\" or \"TV Show\"): ")
            query = """
                SELECT count_of_media(%s);
            """
            params = (media_type,)
            print_result = True
            should_commit = False

        elif query_type.lower() == "count_of_subscription":
            prompt = "Please enter one of the following subscription types:\n" + ", ".join(sub_types) + "\n"
            sub_type = input(prompt)
            query = """
                SELECT count_of_subscription(%s);
            """
            params = (sub_type,)
            print_result = True
            should_commit = False


        elif query_type.lower() == "count_of_subscription":
            prompt = "Please enter a genre"
            sub_type = input(prompt)
            query = """
                SELECT count_of_subscription(%s);
            """
            params = (sub_type,)
            print_result = True
            should_commit = False
            
        elif query_type.lower() == "get media":
            prompt = "Please enter a genre"
            genre = input(prompt)
            with conn.cursor as cursor:
                cursor.callproc("GetMedia", (genre,))
                results = cursor.stored_results
                for result in results:
                    for title in results.fetchall():
                        print(title)

        elif query_type.lower() == "exit":
            print("Exiting database app...")
            is_running = False

        else:
            print("Unkown command!")

        if query != "":
            try:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    if should_commit:
                        conn.commit()
                        print("Number of rows affected: ", cursor.rowcount)
                    print("Command was successful!")
                    if print_result:
                        rows = cursor.fetchall()
                        print(tabulate(rows, headers = cursor.column_names))
            except Error as e:
                print(e)
                


if __name__ == "__main__":
    login_attempts = 5
    logged_in = False
    print("Please enter your credentials.")
    conn = None
    while not logged_in and login_attempts >= 0:
        try:
            conn = connect(
                host = "localhost",
                user = input("Enter username: "),
                password=getpass("Enter password: "),
                database = "streaming_service_db"
            )
            logged_in = True

        except Error as e:
            print(e)
            login_attempts -= 1

            if login_attempts == 0:
                print("No more attempts left, exiting app")
                break
            else:
                print(f"Wrong login information! Please re-enter your credentials. You have {login_attempts} retries remaining.")

    main(conn)

  

    
  
