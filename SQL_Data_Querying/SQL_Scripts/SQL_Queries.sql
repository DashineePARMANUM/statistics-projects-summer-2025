-- SQL Data Querying: Major League Baseball Players Dataset
-- Dashinee Parmanum - dashinee.parmanum@gmail.com
-- Self-directed portfolio project in Statistics and Data Analysis — Summer 2025

-- Set up --------------------------------------------------------------------------------------------------------------

-- table creation
DROP TABLE IF EXISTS mlb_players;
CREATE TABLE mlb_players (Name VARCHAR(100), Team VARCHAR(10), Position VARCHAR(20), Height INT, Weight INT, Age FLOAT);

-- copy data from mlb_players.csv to table
COPY mlb_players(Name, Team, Position, Height, Weight, Age) FROM 'C:\temp\mlb_players.csv' DELIMITER ',' CSV HEADER;

-- Basic SELECT and Filtering ------------------------------------------------------------------------------------------

-- Show all records from the dataset (limit to 10 rows)
SELECT * FROM mlb_players LIMIT 10;

-- Retrieve all players where Age is greater than 25
SELECT * FROM mlb_players WHERE Age > 25;

-- Select Name and Height in inches, and create a new column showing Height in centimeters (1 inch = 2.54 cm)
SELECT Name, Height, Height * 2.54 AS Height_cm FROM mlb_players;

-- Conditional Columns (CASE / IF logic) -------------------------------------------------------------------------------

-- Create a column Is_Heavy that returns “Yes” if Weight is greater than 200 pounds, otherwise “No"
SELECT Name, CASE WHEN Weight > 200 THEN 'Yes' ELSE 'No' END AS Is_Heavy FROM mlb_players; -- doesn't show weight
SELECT Name, Weight, CASE WHEN Weight > 200 THEN 'Yes' ELSE 'No' END AS Is_Heavy FROM mlb_players; -- shows weight

-- Aggregations and Grouping -------------------------------------------------------------------------------------------

-- Count the total number of players
SELECT COUNT(*) FROM mlb_players; -- no column name
SELECT COUNT(*) AS Total_Players FROM mlb_players; -- with column name

-- Calculate the average Age of all players
SELECT AVG(Age) FROM mlb_players;

-- Find the number of players per Team
SELECT Team, COUNT(*) FROM mlb_players GROUP BY Team;

-- Calculate the average Height and average Weight for each Position
SELECT Position,AVG(Height) AS Average_Height, AVG(Weight) AS Average_Weight FROM mlb_players GROUP BY Position;

-- Conditional Aggregations -------------------------------------------------------------------------------------------

-- Count how many players are older than 30 years
SELECT COUNT(*) FROM mlb_players WHERE Age > 30;

-- Find the average Weight for players taller than 72 inches
SELECT AVG(Weight) FROM mlb_players WHERE Height > 72;

-- Joins / Lookups -----------------------------------------------------------------------------------------------------

-- Create a small lookup table for Team information (e.g., Team name and Home City)
-- lookup table creation
DROP TABLE IF EXISTS team_info;
CREATE TABLE team_info (Team VARCHAR(10) PRIMARY KEY, Home_City VARCHAR(50));
-- data creation/insertion into lookup table
INSERT INTO team_info (Team, Home_City) VALUES
('NY', 'New York'),
('BOS', 'Boston'),
('LAD', 'Los Angeles'),
('CHC', 'Chicago'),
('BAL', 'Baltimore');

-- Write a query to join player data with team info to show each player’s Name, Team, and Home City
SELECT p.Name, p.Team, t.Home_City FROM mlb_players p JOIN team_info t ON p.Team = t.Team;

-- Sorting and Limits --------------------------------------------------------------------------------------------------

-- Retrieve the top 5 heaviest players with their names and weights.
SELECT Name FROM mlb_players ORDER BY Weight DESC LIMIT 5; -- without weight displayed
SELECT Name, Weight FROM mlb_players ORDER BY Weight DESC LIMIT 5; -- with weight displayed
SELECT Name, Weight FROM mlb_players WHERE Weight IS NOT NULL ORDER BY Weight DESC LIMIT 5; -- no blank cell

-- Window Functions ----------------------------------------------------------------------------------------------------

-- Display each player’s Name, Position, Weight, and the average Weight for their Position in the same result
SELECT Name, Position, Weight, AVG(Weight) OVER (PARTITION BY Position) AS Average_Weight_Position FROM mlb_players;

-- Summary Tables / Views ----------------------------------------------------------------------------------------------

-- Create a summary view/table that shows average Height, Weight, and Age grouped by Team
DROP VIEW IF EXISTS team_summary;
CREATE VIEW team_summary AS
SELECT Team, AVG(Height) AS Average_Height, AVG(Weight) AS Average_Weight, AVG(Age) AS Average_Age
FROM mlb_players GROUP BY Team;

-- Query this summary view/table sorted by average Height descending
SELECT * FROM team_summary ORDER BY Average_Height DESC; 

-- Constraints and Data Validation -------------------------------------------------------------------------------------

-- Write a statement to add a constraint to ensure Age is always greater than zero
ALTER TABLE mlb_players ADD CONSTRAINT age_positive CHECK (Age > 0);

