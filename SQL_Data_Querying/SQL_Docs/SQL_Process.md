# SQL Data Querying Process - Detailed Notes: Major League Baseball Players Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis — Summer 2025*

---

## 1. Original Data and Setup
- "mlb_players.csv" contains 1034 major league baseball players including their names, teams, positions, heights (in inches), weights (in pounds), and ages (CSV data repository at https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html - GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007: https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt).
- Rename "mlb_players.csv" to "mlb_players_raw.csv" to differentiate from modifed dataset.
- Created "mlb_players.csv" which is the modified dataset (removed special characters and renaming columns for compatibility/ease when using SQL).
- Created a new dataset *statistics-projects-summer-2025* and table *mlb_players*.
- Used `COPY` to import data from "mlb_players.csv" into table *mlb_players*.

 ---
**Contact:** dashinee.parmanum@gmail.com
