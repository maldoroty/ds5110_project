USE streaming_service_db;

DROP VIEW IF EXISTS ‘GetMedia’;

create view customer_public_info as
	select customer_id, name, email, username
    from customer;
    
