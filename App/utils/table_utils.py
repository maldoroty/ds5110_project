table_schemas = {"customer" : "customer_id: int | name: varchar(20) | email: varchar(30) | username: varchar(30) | password: varchar(20) | credit_card: int",
                 "actors" : "a_id: int | name: varchar(20) | ranks: int",
                 "directors" : "d_id: int | name: varchar(20) | ranks: int",
                 "media" : "m_id: int | d_id: int | a_id: int | title: varchar(20) | type: varchar(20) | g_id: int",
                 "rating" : "m_id: int | rating: decimal(2, 1)",
                 "genre" : "g_id: int | genre_name: varchar(10)",
                 "subscription_plan" : "s_type: varchar(20) | price: decimal(4, 2)",
                 "subscription" : "s_id: int | start_sub: date | end_sub: date | customer_id: int | s_type: varchar(20)",
                 "trending_list" : "ranks: int | m_id: int",
                 "soundtracks" : "st_id: int | composer: varchar(20) | title: varchar(40) | m_id: int",
                 "recently_added" : "m_id: int | add_date: date",
                 "leaving_soon" : "m_id: int | removal_date: date",
                 "production_company" : "p_id: int | name: varchar(40) | m_id: int",
                 "contract" : "contract_id: int | p_id: int | amount: int",
                 "movies_watched" : "c_id: int | m_id: int"}

views = ["pc_public_info", "customer_public_info"]

sub_types = ["Daily", "Weekly", "Monthly", "Quarterly", "Half Yearly", "Yearly", "Family Month", "Family Year", "Giant Family Month", "Giant Family Year"]

genre_types = ["Adventure", "Drama", "Western", "History", "Romance", "Animation", "Horror", "Action", "Comedy", "Sci-Fi"]

keys_for_deletion = {"customer" : "customer_id: int",
                     "actors" : "a_id: int",
                     "directors" : "d_id: int",
                     "media" : "m_id: int | d_id: int | a_id: int | g_id: int",
                     "rating" : "m_id: int",
                     "genre" : "g_id: int",
                     "subscription_plan" : "s_type: varchar(20)",
                     "subscription" : "s_id: int | customer_id: int | s_type: varchar(20)",
                     "trending_list" : "ranks: int | m_id: int",
                     "soundtracks" : "st_id: int |  m_id: int",
                     "recently_added" : "m_id: int",
                     "leaving_soon" : "m_id: int",
                     "production_company" : "p_id: int | m_id: int",
                     "contract" : "contract_id: int",
                     "movies_watched" : "c_id: int | m_id: int"}