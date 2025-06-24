# SQL Data Querying Process - Detailed Notes: Major League Baseball Players Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis — Summer 2025*

---
## 0. Original Data and Setup
- `mlb_players.csv` contains 1034 major league baseball players including their names, teams, positions, heights (in inches), weights (in pounds), and ages (CSV data repository at https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html - GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007: https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt).
- Rename `mlb_players.csv` to `mlb_players_raw.csv` to differentiate from modifed dataset.
- Created `mlb_players.csv` which is the modified dataset (removed special characters and renaming columns for compatibility/ease when using SQL).
- All SQL work was conducted using the pgAdmin application, connected to a local PostgreSQL server.
- Created a new dataset *statistics-projects-summer-2025* and table *mlb_players*.
  ```sql
  DROP TABLE IF EXISTS mlb_players;
  CREATE TABLE mlb_players (Name VARCHAR(100), Team VARCHAR(10), Position VARCHAR(20), Height INT, Weight INT, Age FLOAT);
  ```
- Used *COPY* to import data from `mlb_players.csv` into table *mlb_players*.
  ```sql
  COPY mlb_players(Name, Team, Position, Height, Weight, Age) FROM 'C:\temp\mlb_players.csv' DELIMITER ',' CSV HEADER;
  ```
  
---
## 1. Basic SELECT and Filtering
```sql
-- Show all records from the dataset (limit to 10 rows)
SELECT * FROM mlb_players LIMIT 10;

-- Retrieve all players where Age is greater than 25
SELECT * FROM mlb_players WHERE Age > 25;

-- Select Name and Height in inches, and create a new column showing Height in centimeters (1 inch = 2.54 cm)
SELECT Name, Height, Height * 2.54 AS Height_cm FROM mlb_players;
```

---
## 2. Conditional Columns (CASE / IF logic)
```sql
-- Create a column Is_Heavy that returns “Yes” if Weight is greater than 200 pounds, otherwise “No"
SELECT Name, CASE WHEN Weight > 200 THEN 'Yes' ELSE 'No' END AS Is_Heavy FROM mlb_players; -- doesn't show weight
SELECT Name, Weight, CASE WHEN Weight > 200 THEN 'Yes' ELSE 'No' END AS Is_Heavy FROM mlb_players; -- shows weight
```

---
## 3. Aggregations and Grouping
```sql
-- Count the total number of players
SELECT COUNT(*) FROM mlb_players; -- no column name
SELECT COUNT(*) AS Total_Players FROM mlb_players; -- with column name

-- Calculate the average Age of all players
SELECT AVG(Age) FROM mlb_players;

-- Find the number of players per Team
SELECT Team, COUNT(*) FROM mlb_players GROUP BY Team;

-- Calculate the average Height and average Weight for each Position
SELECT Position,AVG(Height) AS Average_Height, AVG(Weight) AS Average_Weight FROM mlb_players GROUP BY Position;
```

---
## 4. Conditional Aggregations
```sql
-- Count how many players are older than 30 years
SELECT COUNT(*) FROM mlb_players WHERE Age > 30;

-- Find the average Weight for players taller than 72 inches
SELECT AVG(Weight) FROM mlb_players WHERE Height > 72;
```

---
## 5. Joins / Lookups
```sql
-- Create a small lookup table for Team information (e.g., Team name and Home City)
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
```
---
## 6. Sorting and Limits
```sql
-- Retrieve the top 5 heaviest players with their names and weights.
SELECT Name FROM mlb_players ORDER BY Weight DESC LIMIT 5; -- without weight displayed
SELECT Name, Weight FROM mlb_players ORDER BY Weight DESC LIMIT 5; -- with weight displayed
SELECT Name, Weight FROM mlb_players WHERE Weight IS NOT NULL ORDER BY Weight DESC LIMIT 5; -- no blank cell
```

---
## 7. Window Functions
```sql
-- Display each player’s Name, Position, Weight, and the average Weight for their Position in the same result
SELECT Name, Position, Weight, AVG(Weight) OVER (PARTITION BY Position) AS Average_Weight_Position FROM mlb_players;
```
---
## 8. Summary Tables / Views
```sql
-- Create a summary view/table that shows average Height, Weight, and Age grouped by Team
DROP VIEW IF EXISTS team_summary;
CREATE VIEW team_summary AS
SELECT Team, AVG(Height) AS Average_Height, AVG(Weight) AS Average_Weight, AVG(Age) AS Average_Age
FROM mlb_players GROUP BY Team;

-- Query this summary view/table sorted by average Height descending
SELECT * FROM team_summary ORDER BY Average_Height DESC; 
```
---
## 9. Constraints and Data Validation
```sql
-- Write a statement to add a constraint to ensure Age is always greater than zero
ALTER TABLE mlb_players ADD CONSTRAINT age_positive CHECK (Age > 0);
```
---
## 10. Key Insights
- The top 5 heaviest players in the dataset are:
  - C.C. Sabathia (290 lbs)
  - Chris Britton (278 lbs)
  - Frank Thomas (275 lbs)
  - Bobby Jenks (270 lbs)
  - Andrew Sisco (260 lbs)
- The team with the highest average player height is the Chicago White Sox (CWS), possibly indicating a preference for taller athletes or recruitment trends within that organization.

---
## 11. Challenges and Solutions
- The dataset required manual modification directly in Excel to clean up special characters and fix inconsistent headers for compatibility with SQL.
  - Edited `mlb_players.csv` manually in Excel to ensure proper formatting before importing.
- Encountered issues importing data into PostgreSQL due to file path or permission restrictions.
  - Created a temporary folder (e.g., `C:\temp`) with appropriate access permissions to store `mlb_players.csv`, enabling successful import via the `COPY` command.
- Running the table creation script multiple times led to errors about the table already existing.
  - Added `DROP TABLE IF EXISTS` before `CREATE TABLE` statements to avoid conflicts.
    
---
**Contact:** dashinee.parmanum@gmail.com
