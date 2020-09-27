/*Задача 3 урока 10

Используя изученные подходы, осуществить следующие выборки:
- Список номеров рейсов для самолетов с максимальной дальностью полета.
- Номера рейсов, названия городов назначения, модели самолетов.
- Имена пассажиров, стоимость их последнего билета.*/

USE [BookingsDB];
GO

-- Имена пассажиров, стоимость их последнего билета.
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
GO


/*Задание 1
Создать процедуру, что будет производить выборку для задачи 3 урока 10*/

CREATE PROCEDURE spGetPassengerNameLastAmount
AS
	SET NOCOUNT ON;
	WITH SubQ1 AS
	(
		SELECT t.passenger_id, t.passenger_name, tf.amount, tf.flight_id FROM [dbo].[tickets] t
		LEFT JOIN [dbo].[ticket_flights] tf
		ON t.ticket_no = tf.ticket_no
	),
	SubQ2 AS
	(
		SELECT s.passenger_id, s.passenger_name, s.amount, f.scheduled_departure FROM SubQ1 s
		LEFT JOIN [dbo].[flights] f
		ON f.flight_id = s.flight_id
	),
	SubQ3 AS
	(
		SELECT s.passenger_id, s.passenger_name, s.amount,
			MAX(s.scheduled_departure) scheduled_departure
		FROM SubQ2 s
		GROUP BY s.passenger_id, s.passenger_name, s.amount
	)
	SELECT passenger_name, amount FROM SubQ3;
GO

EXECUTE spGetPassengerNameLastAmount
GO


/*Задание 2
Написать функцию, которая будет является функцией фильтром для дальности перелета самолета.
Используя эту функцию получить выборку уникальных моделей самолетов, чья дальность полета
превышает 3000 км.*/

CREATE FUNCTION fnGetAircrafts (@range int)
	RETURNS TABLE
AS
	RETURN 
	(
		SELECT * FROM [dbo].[aircrafts] WHERE [range] > @range
	)
GO

SELECT * FROM [dbo].[fnGetAircrafts](3000);
GO


/*Задание 2
Напишите алгоритм, определяющий является ли значение некоторой целочисленной переменной
простым числом с использованием процедур.*/


CREATE PROCEDURE spCheckWhetherNumberIsEven
	@Number int
AS
	DECLARE @iterator int;
	SET @iterator = 2;
	WHILE @iterator <= (@Number / 2)
	BEGIN
		IF @Number % @iterator = 0
			BREAK;
		ELSE
			SET @iterator = @iterator + 1;
	END
	IF @Number % @iterator <> 0 OR @Number = 2
		PRINT CAST(@Number as varchar) + ' is prime.'
	ELSE
		PRINT CAST(@Number as varchar) + ' is not prime.'
GO

DECLARE @iterator int = 2
WHILE @iterator < 22
	BEGIN
		EXEC spCheckWhetherNumberIsEven @Number = @iterator;
		SET @iterator = @iterator + 1
	END;
GO