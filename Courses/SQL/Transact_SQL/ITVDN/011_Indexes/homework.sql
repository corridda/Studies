USE [BookingsDB];
GO

/*Задание. Определить тип недостающего индекса для таблицы билетов и создать его.*/

SET STATISTICS TIME ON;
GO

SELECT * FROM [dbo].[tickets]
WHERE [passenger_id] = '5163 816189'

SELECT * FROM tickets t
JOIN [dbo].[bookings] b
ON t.book_ref = b.book_ref
WHERE t.book_ref = '58F8FF';
GO

CREATE NONCLUSTERED INDEX IX_NCL_tickets_book_ref
    ON [dbo].[tickets]([book_ref]);
GO

SELECT * FROM tickets t
JOIN [dbo].[bookings] b
ON t.book_ref = b.book_ref
WHERE t.book_ref = '58F8FF';
GO



/*Задание 1
Создать индекс для выборки номера рейса, аэропорта назначения и его статуса.*/

SELECT * FROM flights
WHERE flight_no = 'PG0353'

CREATE NONCLUSTERED INDEX IX_NCL_flights_flight_no_arrival_airport_status
    ON [dbo].[flights]
    ([flight_no], [arrival_airport], [status])
