/*Задание
Используя операторы для работы с множествами, получить список рейсов у которых запланированное и
фактическое время прибытия не совпадают*/

USE [BookingsDB];
GO

EXEC sp_help @objname = 'flights'
GO

SELECT COUNT(*) FROM [dbo].[flights];

WITH SubQ AS
(
	SELECT * FROM [dbo].[flights]
		WHERE [actual_arrival] IS NOT NULL
)
SELECT * FROM
	((SELECT [flight_id], [flight_no], [departure_airport], [arrival_airport] FROM SubQ)
	UNION
	(SELECT [flight_id], [flight_no], [departure_airport], [arrival_airport] FROM SubQ)) q
ORDER BY [flight_id], [flight_no];
GO


/*Задание 1
Создать представления для следующих выборок:
- Номер билета, номер рейса, название аэропорта отбытия, название аэропорта прибытия
- Номер рейса, бортовой номер самолета, количество мест в нем.*/

-- Номер билета, номер рейса, название аэропорта отбытия, название аэропорта прибытия
CREATE VIEW tickets_flights_airports WITH SCHEMABINDING AS
	WITH SubQ1 AS
	(
		SELECT tf.ticket_no, f.flight_no, f.departure_airport, f.arrival_airport
			FROM [dbo].[ticket_flights] tf
			JOIN [dbo].[flights] f
			ON tf.flight_id = f.flight_id
	),
	SubQ2 AS
	(
		SELECT s1.ticket_no, s1.flight_no, a.airport_name FROM SubQ1 s1
		JOIN [dbo].[airports] a
		ON a.airport_code = s1.departure_airport
	),
	SubQ3 AS
	(
		SELECT s1.ticket_no, s1.flight_no, a.airport_name FROM SubQ1 s1
		JOIN [dbo].[airports] a
		ON a.airport_code = s1.arrival_airport
	)
	SELECT s2.ticket_no, s2.flight_no, s2.airport_name AS departure_airport, s3.airport_name AS arrival_airport
	FROM SubQ2 s2
	JOIN SubQ3 s3
	ON s2.ticket_no = s3.ticket_no AND s2.flight_no = s3.flight_no;
GO


-- Номер рейса, бортовой номер самолета, количество мест в нем
CREATE VIEW flights_aircrafts_seats_number WITH SCHEMABINDING AS
	SELECT TOP(SELECT COUNT(DISTINCT f.flight_no) FROM [dbo].[flights] f)
		f.flight_no, f.aircraft_code, COUNT(s.seat_no) seats_number
		FROM [dbo].[flights] f
		LEFT JOIN [dbo].[aircrafts] a
		ON a.aircraft_code = f.aircraft_code
		LEFT JOIN [dbo].[seats] s
		ON a.aircraft_code = s.aircraft_code
		GROUP BY f.flight_no, f.aircraft_code
		ORDER BY f.flight_no;
GO