-- Get media for genre

USE new_schema;

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

-- update rating
DROP procedure IF EXISTS ‘UpdateRating’;

DELIMITER $$

CREATE PROCEDURE UpdateRating(
    in updated_m_id int, 
    in new_rating decimal(2, 1)
)
BEGIN
    UPDATE rating
	SET rating = new_rating
	WHERE rating.m_id = updated_m_id;
    
END$$

DELIMITER ;

-- update rating
DROP procedure IF EXISTS ‘UpdatePassword’;

DELIMITER $$

CREATE PROCEDURE UpdatePassword(
    in update_user int, 
    in update_password varchar(20)
)
BEGIN
    UPDATE customer
	SET password = update_password
	WHERE username = update_user;
    
END$$

DELIMITER ;
