USE [BookingsDB];
GO

EXEC sp_help @objname = 'ticket_flights'

/*«адание 1
ƒобавить несколько пользовательских ограничений на вводимые данные дл€ обработки возможных
некорректных значений.*/

IF OBJECT_ID('ticket_flights_fare_conditions_check') IS NOT NULL
BEGIN
	ALTER TABLE ticket_flights
	DROP CONSTRAINT ticket_flights_fare_conditions_check
END;
GO

ALTER TABLE ticket_flights
ADD CONSTRAINT ticket_flights_fare_conditions_check CHECK ([fare_conditions] IN ('Economy', 'Comfort', 'Business'));
GO


/*«адание 2
ѕроанализировав таблицы и варианты возможных запросов к ним, наложить ограничени€ на
уникальность значений дл€ возможных целевых полей таблиц.*/

EXEC sp_help @objname = 'boarding_passes'

IF OBJECT_ID('boarding_passes_flight_id_boarding_no_key') IS NOT NULL
BEGIN
	ALTER TABLE boarding_passes
	DROP CONSTRAINT boarding_passes_flight_id_boarding_no_key
END;
GO

ALTER TABLE [dbo].[boarding_passes]
ADD CONSTRAINT boarding_passes_flight_id_boarding_no_key UNIQUE (flight_id, boarding_no)
GO