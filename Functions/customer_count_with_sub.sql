-- Count the amount of customers with a given subscription type
-- Count the amount of genres

USE streaming_service_db;

DROP function IF EXISTS ‘count_of_subscriptions’;

DELIMITER $$

CREATE FUNCTION count_of_subscription(sub_type varchar(20))
returns int
deterministic

BEGIN
	declare customer_count int;
    
    SELECT count(*) into customer_count
    from subscription s, customer c
     where s.customer_id = c.customer_id and s.s_type = sub_type;
    
    return customer_count
    ;
    
END$$