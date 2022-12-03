-- Count the amount of specific media

USE streaming_service_db;

DROP function IF EXISTS ‘count_of_media’;

DELIMITER $$

CREATE FUNCTION count_of_media(type varchar(20))
returns int
deterministic

BEGIN
	declare media_count int;
    
    SELECT count(*) into media_count
    from media
    where media.type = type;
    
    return media_count
    ;
    
END$$

DELIMITER ;