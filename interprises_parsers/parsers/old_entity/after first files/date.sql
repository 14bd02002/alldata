DROP TABLE IF EXISTS dates;
CREATE TABLE IF NOT EXISTS dates(id int NOT NULL PRIMARY KEY AUTO_INCREMENT, date VARCHAR(30) DEFAULT NULL);
LOAD DATA LOCAL INFILE 'date.csv' IGNORE INTO TABLE dates (date);


