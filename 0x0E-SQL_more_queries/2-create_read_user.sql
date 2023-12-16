-- script that creates db hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant SELECT privilege to the user on the db.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

