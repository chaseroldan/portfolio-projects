DROP TABLE olympic_medalists;


CREATE TABLE olympic_medalists (
  ID INT,
  Name VARCHAR(100) NOT NULL,
  Sex VARCHAR(100) NOT NULL,
  Team VARCHAR(100) NOT NULL,
  NOC VARCHAR(100) NOT NULL,
  Games VARCHAR(100) NOT NULL,
  Year INT,
  Season VARCHAR(100) NOT NULL,
  City VARCHAR(100) NOT NULL,
  Sport VARCHAR(100) NOT NULL,
  Event VARCHAR(100) NOT NULL,
  Medal VARCHAR(100) NOT NULL
);


SELECT *
FROM olympic_medalists;