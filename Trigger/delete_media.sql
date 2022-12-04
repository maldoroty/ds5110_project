-- delete row from leaving soon when deleted in media
DELIMITER $$
CREATE TRIGGER remove_media
BEFORE DELETE ON media
FOR EACH ROW
BEGIN
DELETE FROM leaving_soon WHERE leaving_soon.m_id = OLD.m_id;

END $$;

DELIMITER ;

DROP TRIGGER remove_media;