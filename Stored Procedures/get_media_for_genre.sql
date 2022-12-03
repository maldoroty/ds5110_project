-- Get media for genre

USE streaming_service_db;

DROP procedure IF EXISTS ‘GetMedia’;

DELIMITER $$

CREATE PROCEDURE GetMedia(
    in genre_name VARCHAR(10)
)
BEGIN
    SELECT m.title, m.type
    from media m
    Join genre g
    ON m.g_id = g.g_id
    where g.genre_name = genre_name
    ;
    
END$$

DELIMITER ;