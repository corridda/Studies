/*��������� ��������� �������, ����������� ��������� �������:
- ������ ������� ������ ��� ��������� � ������������ ���������� ������.
- ������ ������, �������� ������� ����������, ������ ���������.
- ����� ����������, ��������� �� ���������� ������.*/

USE [BookingsDB];
GO

-- ������ ������� ������ ��� ��������� � ������������ ���������� ������.
WITH SubQ AS
(
	SELECT TOP(2) * FROM aircrafts
	ORDER BY range DESC
)
SELECT DISTINCT f.flight_no, s.model, s.[range] FROM flights f
JOIN SubQ s
ON s.aircraft_code = f.aircraft_code
ORDER BY f.flight_no


-- ������ ������, �������� ������� ����������, ������ ���������.
WITH SubQ AS
(
	SELECT f.flight_no, f.arrival_airport, a.model FROM flights f
	JOIN aircrafts a
	ON a.aircraft_code = f.aircraft_code
)
SELECT DISTINCT s.flight_no, a.city, s.model FROM SubQ s
LEFT JOIN airports a
ON a.airport_code = s.arrival_airport
ORDER BY s.flight_no


-- ����� ����������, ��������� �� ���������� ������.
WITH SubQ1 AS
(
	SELECT t.passenger_id, t.passenger_name, tf.amount, tf.flight_id FROM tickets t
	LEFT JOIN ticket_flights tf
	ON t.ticket_no = tf.ticket_no
),
SubQ2 AS
(
	SELECT s.passenger_id, s.passenger_name, s.amount, f.scheduled_departure FROM SubQ1 s
	LEFT JOIN flights f
	ON f.flight_id = s.flight_id
),
SubQ3 AS
(
	SELECT s.passenger_id, s.passenger_name, s.amount,
		MAX(s.scheduled_departure) scheduled_departure
	FROM SubQ2 s
	GROUP BY s.passenger_id, s.passenger_name, s.amount
)
SELECT passenger_name, amount FROM SubQ3
