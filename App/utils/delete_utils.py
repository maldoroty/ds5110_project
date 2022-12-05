
def create_delete_query(table_name, user_input):

    if table_name == "customer":
        user_input[0] = int(user_input[0])
        del_query = """
            DELETE FROM customer WHERE customer_id = %s;
        """
    
    elif table_name == "actors":
        user_input[0] = int(user_input[0])
        del_query = """
            DELETE FROM actors WHERE a_id = %s;
        """

    elif table_name == "directors":
        user_input[0] = int(user_input[0])
        del_query = """
            DELETE FROM directors WHERE d_id = %s;
        """

    elif table_name == "media":
        user_input[0] = int(user_input[0])
        user_input[1] = int(user_input[1])
        user_input[2] = int(user_input[2])
        user_input[3] = int(user_input[3])
        del_query = """
            DELETE FROM media WHERE m_id = %s AND d_id = %s AND a_id = %s AND g_id = %s;
        """

    elif table_name == "ratings":
        user_input[0] = int(user_input[0])
        del_query = """
            DELETE FROM ratings WHERE m_id = %s;
        """

    elif table_name == "genre":
        user_input[0] = int(user_input[0])
        del_query = """
            DELETE FROM genre WHERE g_id = %s;
        """

    elif table_name == "subscription_plan":
        user_input[1] = float(user_input[1])
        del_query = """
            DELETE FROM subscription_plan WHERE s_type = %s;
        """
    
    elif table_name == "subscription":
        user_input[0] = int(user_input[0])
        user_input[1] = int(user_input[1])
        del_query = """
            DELETE FROM subscription WHERE s_id = %s AND customer_id = %s AND s_type = %s;
        """
        
    elif table_name == "trending_list":
        user_input[0] = float(user_input[0])
        user_input[1] = float(user_input[1])
        del_query = """
            DELETE FROM trending_list WHERE ranks = %s AND m_id = %s;
        """
        # "movies_watched" : "c_id: int | m_id: int"
        
    elif table_name == "soundtracks":
        user_input[0] = int(user_input[0])
        user_input[1] = int(user_input[1])
        del_query = """
            DELETE FROM soundtracks WHERE st_id = %s AND m_id = %s;
        """
        
    elif table_name == "recently_added":
        user_input[0] = int(user_input[0])
        del_query = """
            DELETE FROM recently_added WHERE m_id = %s;
        """

    elif table_name == "leaving_soon":
        user_input[0] = int(user_input[0])
        del_query = """
             DELETE FROM leaving_soon WHERE m_id = %s;
        """

    elif table_name == "production_company":
        user_input[0] = int(user_input[0])
        user_input[1] = int(user_input[1])
        del_query = """
            DELETE FROM production_company WHERE p_id = %s AND m_id = %s;
        """

    elif table_name == "contract":
        user_input[0] = int(user_input[0])
        del_query = """
            DELETE FROM contract WHERE contract_id = %s;
        """

    elif table_name == "movies_watched":
        user_input[0] = int(user_input[0])
        user_input[1] = int(user_input[1])
        del_query = """
            DELETE FROM movies_watched WHERE c_id = %s AND m_id = %s;
        """
    
    else:
        raise Exception("Given unknown table name!")

    return del_query, user_input
            


