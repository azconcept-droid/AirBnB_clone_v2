-- This srcipt setup MYSQL server for this project

-- Create hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create new user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant hbnb_dev user all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'locahost';

-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush the privileges into MYSQL server
FLUSH PRIVILEGES;
