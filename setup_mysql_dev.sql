-- First We Create The DataBase
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
-- Then We Create The User
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY 'hbnb_dev_pwd';
-- Then We Grant All Privileges To The User
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO `hbnb_dev`@`localhost`;
-- Grant SELECT To The User on 'performance_schema' DB
GRANT SELECT ON performance_schema.* TO `hbnb_dev`@`localhost`;
