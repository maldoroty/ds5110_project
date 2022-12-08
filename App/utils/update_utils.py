
def create_update_query(table_name, user_input):
    """
        Creates the query and parameters for updating the given table.
        Have to create the "params" list in order to re-order the inputs
        since the order of the attributes in the query and the order of
        the attributes in the prompt given to the user are different, so we
        have to re-order the attributes so they go into their proper place
        in the query. This allows us to reuse the "table_schemas" dictionary
        in "insert_utils.py".

        As well, we have to do type casting/conversion again because the
        input of the user is originally a string.
    """
    params = []
    if table_name == "customer":
        params.append(user_input[1]) # name
        params.append(user_input[2]) # email
        params.append(user_input[3]) # username
        params.append(user_input[4]) # password 
        params.append(int(user_input[5])) # credit_card
        params.append(int(user_input[5])) # customer_id
        update_query = """
            UPDATE customer 
            SET name = %s, email = %s, username = %s, password = %s, credit_card = %s
            WHERE customer_id = %s;
        """
    
    elif table_name == "actors":
        params.append(user_input[1]) # name
        params.append(int(user_input[2])) # ranks
        params.append(int(user_input[0])) # a_id
        update_query = """
            UPDATE actors
            SET name = %s, ranks = %s
            WHERE a_id = %s;
        """

    elif table_name == "directors":
        params.append(user_input[1]) # name
        params.append(int(user_input[2])) # ranks
        params.append(int(user_input[0])) # d_id
        update_query = """
            UPDATE directors 
            SET name = %s, ranks = %s
            WHERE d_id = %s;
        """

    elif table_name == "media":
        params.append(user_input[3]) # title
        params.append(user_input[4]) # type
        params.append(int(user_input[0])) # m_id
        params.append(int(user_input[1])) # d_id
        params.append(int(user_input[2])) # a_id
        params.append(int(user_input[5])) # g_id
        update_query = """
            UPDATE media
            SET title = %s, type = %s
            WHERE m_id = %s AND d_id = %s AND a_id = %s AND g_id = %s;
        """

    elif table_name == "ratings":
        params.append(float(user_input[1])) # ranking
        params.append(int(user_input[0])) # m_id
        update_query = """
            UPDATE ratings 
            SET ranking = %s
            WHERE m_id = %s;
        """

    elif table_name == "genre":
        params.append(user_input[1]) # genre_name
        params.append(int(user_input[0])) # g_id
        update_query = """
            UPDATE genre 
            SET genre_name = %s
            WHERE g_id = %s;
        """

    elif table_name == "subscription_plan":
        params.append(float(user_input[1])) # price
        params.append(user_input[0]) # s_type
        update_query = """
            UPDATE subscription_plan
            SET price = %s
            WHERE s_type = %s;
        """

    elif table_name == "subscription":
        params.append(user_input[1]) # start_sub
        params.append(user_input[2]) # end_sub
        params.append(int(user_input[0])) # s_id
        params.append(int(user_input[3])) # customer_id
        params.append(user_input[4]) # s_type
        update_query = """
            UPDATE subscription
            SET start_sub = %s, end_sub = %s
            WHERE s_id = %s AND customer_id = %s AND s_type = %s;
        """
        
    elif table_name == "trending_list":
        params.append(float(user_input[1])) # ranks
        params.append(float(user_input[0])) # m_id
        update_query = """
            UPDATE trending_list 
            SET m_id = %s
            WHERE ranks = %s;
        """
        
    elif table_name == "soundtracks":
        params.append(user_input[1]) # composer
        params.append(user_input[2]) # title
        params.append(int(user_input[0])) # composer
        params.append(int(user_input[3])) # m_id
        update_query = """
            UPDATE soundtracks
            SET composer = %s, title = %s 
            WHERE st_id = %s AND m_id = %s;
        """
        
    elif table_name == "recently_added":
        params.append(user_input[1]) # add_date
        params.append(int(user_input[0])) # m_id
        update_query = """
            UPDATE recently_added
            SET add_date = %s
            WHERE m_id = %s;
        """

    elif table_name == "leaving_soon":
        params.append(user_input[1]) # removal_date
        params.append(int(user_input[0])) # m_id
        update_query = """
            UPDATE leaving_soon
            SET removal_date = %s
            WHERE m_id = %s;
        """

    elif table_name == "production_company":
        params.append(user_input[1]) # name
        params.append(int(user_input[0])) # p_id
        params.append(int(user_input[2])) # m_id
        update_query = """
            UPDATE production_company 
            SET name = %s
            WHERE p_id = %s AND m_id = %s;
        """

    elif table_name == "contract":
        params.append(int(user_input[2])) # amount
        params.append(int(user_input[0])) # contract_id
        params.append(int(user_input[1])) # p_id
        update_query = """
            UPDATE contract
            SET amount = %s
            WHERE contract_id = %s AND p_id = %s;
        """

    elif table_name == "movies_watched":
        user_input[0] = int(user_input[0])
        user_input[1] = int(user_input[1])
        update_query = """
            UPDATE movies_watched 
            SET VALUES (%s, %s);
        """
    
    else:
        raise Exception("Given unknown table name!")

    return update_query, params
            
