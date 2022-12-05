USE streaming_service_db;

DROP VIEW IF EXISTS ‘pc_public_info’;

create view pc_public_info as
	select c.contract_id, c.p_id, p.name as production_company
    from contract c, production_company p
    where c.p_id = p.p_id
    group by c.contract_id, c.p_id, p.name;
    
