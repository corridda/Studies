/*«адание 1
ѕроизвести выборки, удовлетвор€ющие следующим критери€м:
- јэропорт с максимальным количеством рейсов
- Ќазвание городов и стоимости билетов к ним
- »мена пассажиров, стоимость забронированных ими билетов, стоимость брони и остальных
билетов этих пассажиров*/

USE [BookingsDB];
GO

-- јэропорт с максимальным количеством рейсов
WITH SubQ2 (airport, total_flights) AS
	(SELECT airport, SUM(total_flights) total_flights FROM
		(SELECT departure_airport airport, COUNT(departure_airport) total_flights FROM flights
		GROUP BY departure_airport
		UNION ALL
		SELECT arrival_airport airport, COUNT(arrival_airport) total_flights FROM flights
		GROUP BY arrival_airport) subq
	GROUP BY airport),
SubQ3 (airport, total_flights) AS
	(SELECT airport, total_flights FROM SubQ2
		WHERE total_flights = (SELECT MAX(total_flights) FROM SubQ2))
SELECT a.airport_name, SubQ3.total_flights FROM SubQ3
JOIN airports a
ON a.airport_code = SubQ3.airport;
GO


-- Ќазвание городов и стоимости билетов к ним
WITH SubQ_Flights AS
	(SELECT flight_id, flight_no, departure_airport, arrival_airport FROM flights),
SubQ_2 AS
	(SELECT DISTINCT sqf.flight_no, sqf.departure_airport, sqf.arrival_airport, tf.amount
	FROM SubQ_Flights sqf
	JOIN ticket_flights tf
		ON sqf.flight_id = tf.flight_id)
SELECT DISTINCT flight_no, departure_airport, arrival_airport, MIN(amount) OVER(PARTITION BY flight_no) min_amount
	FROM SubQ_2
	ORDER BY flight_no;
GO


-- »мена пассажиров, стоимость забронированных ими билетов, стоимость брони и остальных
--билетов этих пассажиров
SELECT t.passenger_id, t.passenger_name, b.total_amount
FROM tickets t
JOIN bookings b
	ON b.book_ref = t.book_ref;
GO
