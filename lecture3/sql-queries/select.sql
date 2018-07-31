SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = 'New York';
SELECT * FROM flights WHERE duration  > 500;
SELECT * FROM flights WHERE destination = 'Paris' AND duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500;


SELECT AVG(duration) FROM flights;
SELECT AVG(duration) FROM flights WHERE origin = 'New York';
SELECT COUNT(*) FROM flights;
SELECT COUNT(*) FROM flights WHERE origin = 'New York';
SELECT COUNT(*) FROM flights WHERE origin = 'Moscow';
SELECT MIN(duration) FROM flights;
SELECT * FROM flights WHERE duration = 245;
SELECT * FROM flights WHERE origin IN ('New York', 'Lima');
SELECT * FROM flights WHERE origin LIKE '%a%';
SELECT origin, COUNT(*) FROM flights GROUP BY origin;
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;


SELECT * FROM passengers WHERE name = 'Alice';
SELECT * FROM passengers WHERE id = 1;

-- INNER JOIN
SELECT origin, destination, name FROM flights 
    JOIN passengers ON passengers.flight_id = flights.id;

SELECT origin, destination, name FROM flights 
    JOIN passengers ON passengers.flight_id = flights.id WHERE name = 'Alice';

-- LEFT JOIN
SELECT origin, destination, name FROM flights 
    LEFT JOIN passengers ON passengers.flight_id = flights.id;

SELECT flight_id FROM passengers
    GROUP BY flight_id HAVING COUNT(*) > 1;

SELECT * FROM flights WHERE id IN 
    (SELECT flight_id FROM passengers
    GROUP BY flight_id HAVING COUNT(*) > 1);