## IN THE WORKS

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
    - ```sql
      ```sql
      DROP TABLE IF EXISTS mlb_players;
      CREATE TABLE mlb_players (
        Name VARCHAR(100),
        Team VARCHAR(10),
        Position VARCHAR(20),
        Height INT,
        Weight INT,
        Age FLOAT
      );
- Used *COPY* to import data from `mlb_players.csv` into table *mlb_players*.

---
## 1. Basic SELECT and Filtering

---
## 2. Conditional Columns (CASE / IF logic)

---
## 3. Aggregations and Grouping

---
## 4. Conditional Aggregations

---
## 5. Joins / Lookups

---
## 6. Sorting and Limits

---
## 7. Window Functions

---
## 8. Summary Tables / Views

---
## 9. Constraints and Data Validation

---
## 10. Key Insights
-

---
## 11. Challenges and Solutions
-

---
## 12. Final File
-
---
**Contact:** dashinee.parmanum@gmail.com
