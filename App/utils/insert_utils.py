
def create_insert_query(table_name, attrs):
    """
        Takes the table name and attributes and produces an appropriate query.
        We have to do a lot of type casting since the attributes/fields entered
        by the user is originally a string, and it depends on the table name as
        to which attributes are casted to which types.
    """
    if table_name == "customer":
        attrs[0] = int(attrs[0])
        attrs[5] = int(attrs[5])
        inst_query = """
            INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s);
        """
    
    elif table_name == "actors":
        attrs[0] = int(attrs[0])
        attrs[2] = int(attrs[2])
        inst_query = """
            INSERT INTO actors VALUES (%s, %s, %s);
        """

    elif table_name == "directors":
        attrs[0] = int(attrs[0])
        attrs[2] = int(attrs[2])
        inst_query = """
            INSERT INTO directors VALUES (%s, %s, %s);
        """

    elif table_name == "media":
        attrs[0] = int(attrs[0])
        attrs[1] = int(attrs[1])
        attrs[2] = int(attrs[2])
        attrs[5] = int(attrs[5])
        inst_query = """
            INSERT INTO media VALUES (%s, %s, %s, %s, %s, %s);
        """

    elif table_name == "ratings":
        attrs[0] = int(attrs[0])
        attrs[1] = float(attrs[1])
        inst_query = """
            INSERT INTO ratings VALUES (%s, %s);
        """

    elif table_name == "genre":
        attrs[0] = int(attrs[0])
        inst_query = """
            INSERT INTO genre VALUES (%s, %s);
        """

    elif table_name == "subscription_plan":
        attrs[1] = float(attrs[1])
        inst_query = """
            INSERT INTO subscription_plan VALUES (%s, %s);
        """

    elif table_name == "subscription":
        attrs[0] = int(attrs[0])
        attrs[3] = int(attrs[3])
        inst_query = """
            INSERT INTO subscription VALUES (%s, %s, %s, %s, %s);
        """
        
    elif table_name == "trending_list":
        attrs[0] = float(attrs[0])
        attrs[1] = float(attrs[1])
        inst_query = """
            INSERT INTO trending_list VALUES (%s, %s);
        """
        
    elif table_name == "soundtracks":
        attrs[0] = int(attrs[0])
        attrs[3] = int(attrs[3])
        inst_query = """
            INSERT INTO soundtracks VALUES (%s, %s, %s, %s);
        """
        
    elif table_name == "recently_added":
        attrs[0] = int(attrs[0])
        inst_query = """
            INSERT INTO recently_added VALUES (%s, %s);
        """

    elif table_name == "leaving_soon":
        attrs[0] = int(attrs[0])
        inst_query = """
            INSERT INTO leaving_soon VALUES (%s, %s);
        """

    elif table_name == "production_company":
        attrs[0] = int(attrs[0])
        attrs[2] = int(attrs[2])
        inst_query = """
            INSERT INTO production_company VALUES (%s, %s, %s);
        """

    elif table_name == "contract":
        attrs[0] = int(attrs[0])
        attrs[1] = int(attrs[1])
        attrs[2] = int(attrs[2])
        inst_query = """
            INSERT INTO contract VALUES (%s, %s, %s);
        """

    elif table_name == "movies_watched":
        attrs[0] = int(attrs[0])
        attrs[1] = int(attrs[1])
        inst_query = """
            INSERT INTO movies_watched VALUES (%s, %s);
        """
    
    else:
        raise Exception("Given unknown table name!")

    return inst_query, attrs
            
