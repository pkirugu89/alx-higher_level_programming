-- create hbtn_0d_usa db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the hbtn_0d_usa db
USE hbtn_0d_usa;
-- create table cities if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);

