-- First We Create The DataBase
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
-- Then We Create The User
CREATE USER IF NOT EXISTS `hbnb_test`@`localhost` IDENTIFIED BY 'hbnb_test_pwd';
-- Then We Grant All Privileges To The User
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO `hbnb_test`@`localhost`;
-- Grant SELECT To The User on 'performance_schema' DB
GRANT SELECT ON performance_schema.* TO `hbnb_test`@`localhost`;
