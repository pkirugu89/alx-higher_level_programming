-- script that creates a table 'unique_id' in 'hbtn_0d_2' db
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);

