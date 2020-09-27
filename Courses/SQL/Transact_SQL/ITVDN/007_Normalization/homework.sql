USE [ITVDNdb];
GO

IF OBJECT_ID('Colors') IS NOT NULL
	DROP TABLE [dbo].[Colors]
GO

CREATE TABLE Colors(
	Id int IDENTITY(1,1) PRIMARY KEY,
	Color varchar(20)
);
GO

INSERT INTO Colors ([Color])
VALUES ('Red'), ('Blue'), ('Yellow'), ('Black');
GO


IF OBJECT_ID('Items') IS NOT NULL
	DROP TABLE [dbo].[Items]
GO

CREATE TABLE Items(
	Id int IDENTITY(1,1) PRIMARY KEY,
	Item varchar(50),
	Price decimal(4,2)
);
GO

INSERT INTO Items ([Item], [Price])
VALUES	('T-Shirt_1', 12.00),
		('T-Shirt_2', 15.00),
		('Polo', 12.00),
		('SweatShirt', 25.00);
GO


IF OBJECT_ID('ItemColor') IS NOT NULL
	DROP TABLE [dbo].[ItemColor]
GO

CREATE TABLE ItemColor
(
    --Id int IDENTITY(1,1) PRIMARY KEY,
	ItemId int CONSTRAINT FK_ItemColor_ItemId_Items_Id FOREIGN KEY
		REFERENCES Items(Id)
		ON DELETE CASCADE,
	ColorId int CONSTRAINT FK_ItemColor_ColorId_Colors_Id FOREIGN KEY
		REFERENCES Colors(Id)
		ON DELETE CASCADE,
	CONSTRAINT UQ_ItemColor UNIQUE (ItemId, ColorId)
);
GO

INSERT INTO ItemColor ([ItemId], [ColorId])
VALUES	(1, 1), (1, 2), (2, 1), (2, 3), (3, 1), (3, 3), (4, 4);
GO

SELECT * FROM [dbo].[Items];
SELECT * FROM [dbo].[ItemColor];
SELECT * FROM [dbo].[Colors];
GO

WITH CTE_1 (ItemId, ColorId) AS
(
	SELECT [ItemId], [ColorId] FROM [dbo].[ItemColor]
	WHERE [ItemId] IN
		(SELECT [Id] FROM [dbo].[Items]
			WHERE [Item] LIKE '%T-Shirt%')
),
CTE_2 (Item, ColorId) AS
(
	SELECT Items.[Item], CTE_1.ColorId FROM [dbo].[Items]
	RIGHT JOIN CTE_1 ON [dbo].[Items].Id = CTE_1.ItemId
)
SELECT q.Item, c.Color FROM CTE_2 AS q
LEFT JOIN [dbo].[Colors] AS c
ON q.ColorId = c.Id;
GO