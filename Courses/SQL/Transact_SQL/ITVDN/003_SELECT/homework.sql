
USE [BookingsDB];
GO

/*Из BookingsDB получить следующие выборки:*/

-- Номера самолетов, дистанция полета которых превышает 2000 или неопределенна
SELECT * FROM [dbo].[aircrafts]
WHERE [range] > 2000 OR [range] IS NULL

/*Названия всех аэропортов, первый символ названия городов которых буквы А, Б, В, так же,
часовая зона начинается с "Europe".*/
SELECT * FROM [dbo].[airports]
WHERE [city] LIKE '[А,Б,В]%' AND [timezone] LIKE 'Europe%'
ORDER BY City

/*Только уникальные номера рейсов, чье отклонение времени прибытия от запланированного более 5 мин.*/
SELECT DISTINCT [flight_id], ([actual_arrival] - [scheduled_arrival]) AS [DIFF]
FROM [dbo].[flights]
WHERE ([scheduled_arrival] - [actual_arrival]) > '00:05:00.000'
