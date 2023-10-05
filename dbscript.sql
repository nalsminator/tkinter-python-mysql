CREATE SCHEMA tkinterdb;

CREATE  TABLE tkinterdb.countries ( 
	`Id`                 INT  NOT NULL   AUTO_INCREMENT  PRIMARY KEY,
	`ISO3`               VARCHAR(3)  NOT NULL     ,
	`CountryName`        VARCHAR(64)  NOT NULL     ,
	`Capital`            VARCHAR(64)  NOT NULL     ,
	`CurrencyCode`       VARCHAR(3)  NOT NULL     
 ) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO tkinterdb.countries( `Id`, `ISO3`, `CountryName`, `Capital`, `CurrencyCode` ) VALUES ( 1, 'ARG', 'Argentina', 'Buenos Aires', 'ARS');
INSERT INTO tkinterdb.countries( `Id`, `ISO3`, `CountryName`, `Capital`, `CurrencyCode` ) VALUES ( 2, 'COL', 'Colombia', 'Bogota', 'COP');
INSERT INTO tkinterdb.countries( `Id`, `ISO3`, `CountryName`, `Capital`, `CurrencyCode` ) VALUES ( 3, 'MEX', 'Mexico', 'CDMX', 'MXN');
INSERT INTO tkinterdb.countries( `Id`, `ISO3`, `CountryName`, `Capital`, `CurrencyCode` ) VALUES ( 5, 'AUS', 'Australia', 'Canberra', 'AUD');
INSERT INTO tkinterdb.countries( `Id`, `ISO3`, `CountryName`, `Capital`, `CurrencyCode` ) VALUES ( 6, 'DEU', 'Germanyy', 'Berlin', 'EUR');
INSERT INTO tkinterdb.countries( `Id`, `ISO3`, `CountryName`, `Capital`, `CurrencyCode` ) VALUES ( 7, 'IND', 'India', 'New Delhi', 'INR');
INSERT INTO tkinterdb.countries( `Id`, `ISO3`, `CountryName`, `Capital`, `CurrencyCode` ) VALUES ( 8, 'LAO', 'Laos', 'Vientiane', 'LAK');
INSERT INTO tkinterdb.countries( `Id`, `ISO3`, `CountryName`, `Capital`, `CurrencyCode` ) VALUES ( 9, 'USA', 'United States', 'Washington', 'USD');