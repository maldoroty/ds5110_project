from mysql.connector import connect, Error
from getpass import getpass
from tabulate import tabulate

from utils.update_utils import create_update_query
from utils.insert_utils import create_insert_query
from utils.delete_utils import create_delete_query
from utils.table_utils import table_schemas, keys_for_deletion, views, sub_types, genre_types

"""
    Streaming Database App
    by Hajera Siddiqui and Michael Aldoroty

"""


def main(conn):

    """
        Starts our database app. Allows the user to run several commands
        that let the user modify and view the database.
    """

    # Main loop for our app
    is_running = True
    while is_running:
        print("")

        # Some state variables that get reset on every iteration of the loop
        query_type = input("Please enter a command, or enter 'help' to see list of available commands.\n> ")
        query = ""             # The query produced by one of the if conditions
        proc_name = ""         # The name of a stored procedure produced by a command
        params = tuple()       # The parameters to be used in either a query or stored procedure
        print_result = False   # Whether or not the result from the command should be printed out
        should_commit = True   # Whether or not the command should be committed to the DB (for queries)
        is_proc = False        # Whether or not the current command set by a user is a stored procedure


        if query_type.lower() == "help":
            # Help command for users who want to know how to use this program
            print("Available Commands:")
            print("-------------------")
            print("     insert  :  insert data into a table")
            print("     delete  :  remove data from a table")
            print("     update  :  modify existing data in a table")
            print("     viewership  :  view information about users and the media they have recently consumed")
            print("     stored_proc  :  view stored procedures regarding the database")
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
            # We let the user just enter the params with commas and then split it
            attrs = insert_attr.split(",")

            # Using the query and attributes from the function, we can just send it
            # to the database and get the result without have to do any other
            # formatting.
            query, attrs = create_insert_query(table_name, attrs)
            params = tuple(attrs)

            
        elif query_type.lower() == "delete":
            table_name = input("Enter table name: ")
            if table_name not in table_schemas:
                print("There is no table called \"", table_name, "\" in the database.")
                # Continue since the user has entered an invalid name
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
                # The "watched" can't be changed since it is just a pair
                # of media_id and customer_id, and changing it will likely
                # cause a duplicate entry in the table.
                continue

            # Lets print the schema for the table to help the user out
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
           
        elif query_type.lower() == "contract_eval":
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
          
        elif query_type.lower() == "customer_usage":
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
            # We have to append the name of the table/view to the end of the query because using
            # a string template with %s would enclose the table name around quotes, which causes
            # an error in MySQL
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

        elif query_type.lower() == "stored_proc":
            # Since we have 3 types of procs, we want to keep asking until the user gives us a valid choice
            valid_proc = False
            while not valid_proc:
                proc_name = input("\nPlease enter a stored procedure (\"GetMedia\" or \"UpdateRating\" or \"UpdatePassword\"): ")

                if proc_name == "GetMedia":
                    params = input("\nPlease enter one of the following genre types:\n" + ", ".join(genre_types) + "\n")
                    print_result = True
                    valid_proc = True
                
                elif proc_name == "UpdateRating":
                    params = input("\nPlease enter a media id (m_id) and new a rating seperated by a comma:\n")
                    valid_proc = True

                elif proc_name == "UpdatePassword":
                    params = input("\nPlease enter a username and the new password separated by a comma\n")
                    valid_proc = True
                
                else:
                    print("Please enter a valid stored procedure")
                    
            params = params.split(",")            
            is_proc = True
            

        elif query_type.lower() == "exit":
            print("Exiting database app...")
            is_running = False

        else:
            print("Unkown command!")
            continue

        
        try:
            # Keep this in a try catch so we can handle any database errors
            with conn.cursor() as cursor:
                # We have to check if the user's latest command is a query or a proc
                # since they are sent to the database using different functions and
                # trying to get the results from each one needs a different way of
                # retrieving them.
                if is_proc:
                    cursor.callproc(proc_name, params)
                    if print_result:
                        results = list(cursor.stored_results())

                        column_names = [desc_tuple[0] for desc_tuple in results[0].description]
                        rows = [row for result in results for row in result.fetchall()]
                        print("")
                        print(tabulate(rows, headers= column_names))
                    else:
                        print("Command was successful!")

                
                elif query != "":

                    cursor.execute(query, params)

                    if should_commit:
                        conn.commit()
                        print("Number of rows affected: ", cursor.rowcount)
                        print("Command was successful!")

                    if print_result:
                        rows = cursor.fetchall()
                        print("")
                        print(tabulate(rows, headers = cursor.column_names))
                

        except Error as e:
            print(e)
                


if __name__ == "__main__":
    # Give the users a few login attempts before exiting the app
    login_attempts = 5
    logged_in = False
    print("Please enter your credentials.")
    conn = None
    while not logged_in and login_attempts >= 0:
        try:
            conn = connect(
                host = "localhost",
                user = input("Enter username: "),
                password= getpass("Enter password: "),
                database = "streaming_service_db"
            )
            logged_in = True

        except Error as e:
            print(e)
            login_attempts -= 1

            if login_attempts == 0:
                # If the user is out of attempts, break to end the program
                print("No more attempts left, exiting app")
                break
            else:
                print(f"Wrong login information! Please re-enter your credentials. You have {login_attempts} retries remaining.")

    # Runs only when the program has succesfully connected to the database and
    # the conn variable has been set to a MySQL Connection object.
    main(conn)

  

    
  
