
USE [BookingsDB];
GO

/*�� BookingsDB �������� ��������� �������:*/

-- ������ ���������, ��������� ������ ������� ��������� 2000 ��� �������������
SELECT * FROM [dbo].[aircrafts]
WHERE [range] > 2000 OR [range] IS NULL

/*�������� ���� ����������, ������ ������ �������� ������� ������� ����� �, �, �, ��� ��,
������� ���� ���������� � "Europe".*/
SELECT * FROM [dbo].[airports]
WHERE [city] LIKE '[�,�,�]%' AND [timezone] LIKE 'Europe%'
ORDER BY City

/*������ ���������� ������ ������, ��� ���������� ������� �������� �� ���������������� ����� 5 ���.*/
SELECT DISTINCT [flight_id], ([actual_arrival] - [scheduled_arrival]) AS [DIFF]
FROM [dbo].[flights]
WHERE ([scheduled_arrival] - [actual_arrival]) > '00:05:00.000'
