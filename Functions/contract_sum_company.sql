-- get total amount of money from a production company

USE streaming_service_db;

DROP function IF EXISTS ‘get_money’;

DELIMITER $$

CREATE FUNCTION get_money(prod_name varchar(20))
returns int
deterministic

BEGIN
	declare total_amount int;
    
    SELECT sum(c.amount) into total_amount
	FROM production_company p, contract c
	WHERE p.p_id = c.p_id and prod_name = p.name
	GROUP BY prod_name;
    
    return total_amount
    ;
    
END$$

DELIMITER ;