CREATE DATABASE HomeTask
	COLLATE Cyrillic_General_CI_AS
GO

USE HomeTask;
GO

CREATE TABLE AirCrafts
(
    [AircraftCode] char(3) NOT NULL PRIMARY KEY,
	[Model] nvarchar(30) NOT NULL,
	[Range] int NOT NULL
	CHECK ( [Range] > 0 ),
	[SeatsNumber] int NOT NULL,
	[FareConditions] nvarchar(100) NOT NULL
);

INSERT INTO AirCrafts ([AircraftCode],[Model],[Range],[SeatsNumber],[FareConditions])
	VALUES
		('773','Boeing 777-300',11100, 500, 'Business, Economy'),
		('763', 'Boeing 767-300', 7900, 150, 'Business, Lux'),
		( '733', 'Boeing 737-300', 4200, 480, 'Business, Economy'),
		( '320', 'Airbus A320-200', 5700, 650, 'Business, Economy'),
		( '321', 'Airbus A321-200', 5600, 800, 'Business, Economy'),
		( '319', 'Airbus A319-100', 6700, 120, 'Business, Lux'),
		( 'CN1', 'Cessna 208 Caravan', 1200, 650, 'Business, Economy'),
		( 'CR2', 'Bombardier CRJ-200', 2700, 50, 'Business, Lux');

SELECT * FROM AirCrafts

UPDATE AirCrafts
	SET [SeatsNumber] = 170
	OUTPUT inserted.*
	WHERE [AircraftCode] = '763';
GO

DELETE FROM AirCrafts
	OUTPUT deleted.*
	WHERE [AircraftCode] = 'CR2';
GO

DECLARE @valueTable table (
	[AircraftCode] char(3),
	[Model] nvarchar(30),
	[Range] int,
	[SeatsNumber] int,
	[FareConditions] nvarchar(100));

INSERT INTO @valueTable
	SELECT * FROM AirCrafts;

SELECT * FROM @valueTable;
GO
