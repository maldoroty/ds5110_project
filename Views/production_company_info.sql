USE streaming_service_db;

DROP VIEW IF EXISTS ‘pc_public_info’;

create view pc_public_info as
	select contract_id, p_id
    from contract;
    
