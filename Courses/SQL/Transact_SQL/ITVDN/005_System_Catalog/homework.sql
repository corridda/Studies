USE [BookingsDB];
GO


/*ѕодключившись к базе BookingsDB, при помощи агрегатных функций и системных таблиц, подсчитать
количество таблиц в данной базе.*/
SELECT name, object_id FROM sys.objects
WHERE schema_id = SCHEMA_ID('dbo') AND type = 'U'

SELECT COUNT(*) FROM sys.objects
WHERE schema_id = SCHEMA_ID('dbo') AND type = 'U'


/*«адание 1
ѕолучить среднее значение дальности полета самолетов и среднее значение дл€ уникальных значений
дальности*/
EXEC sp_help aircrafts

INSERT INTO [dbo].[aircrafts]
VALUES ('SU8','Sukhoi SuperJet-110',3000)

SELECT AVG(range) AS Average_Range FROM aircrafts

-- вариант 1
SELECT AVG(q.[range]) AS Average_Range FROM (SELECT DISTINCT [range] FROM aircrafts) q

-- вариант 2
SELECT AVG(DISTINCT [range]) AS Average_Range FROM  aircrafts

DELETE FROM [dbo].[aircrafts]
WHERE [aircraft_code] = 'SU8'


/*«адание 2
ѕолучить количество броней и их среднюю стоимость*/
EXEC sp_help bookings

SELECT COUNT(*) AS rows, AVG([total_amount]) AS average_total_amount FROM [dbo].[bookings]