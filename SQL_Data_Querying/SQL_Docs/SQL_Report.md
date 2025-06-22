# SQL Data Querying Report: Major League Baseball Players Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis — Summer 2025*

---
## 1. Introduction
This project explores player data from Major League Baseball (MLB) using SQL. The main objective was to analyze trends in player characteristics (such as age, weight, and height) across teams and positions.

---
## 2. Data Description
The dataset contains information for 1034 professional baseball players, including their names, teams, positions, heights (in inches), weights (in pounds), and ages. The data was sourced from the CSV data repository at https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html (`mlb_players.csv`). 
GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007: https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt

---
## 3. Methodology
The dataset used was a CSV file containing MLB player information. I first prepared the data by removing special characters and renaming columns for compatibility/ease then performed SQL queries as follows:
- Created a new database and table to store the player data.  
- Imported the cleaned CSV file into the database using PostgreSQL’s *COPY* command.
- Used SQL queries to explore and analyze the data, including selecting and filtering records, creating conditional columns, and aggregating data by groups.  
- Created a lookup table to join team information with player data.  
- Applied sorting, window functions, and summary views to extract meaningful insights.  
- Added a constraint to ensure player ages are valid (positive).

---
## 4. Key Insights
- The top 5 heaviest players in the dataset are C.C. Sabathia (290 lbs), Chris Britton (278 lbs), Frank Thomas (275 lbs), Bobby Jenks (270 lbs), and Andrew Sisco (260 lbs).
- The team with the highest average player height is the Chicago White Sox (CWS), possibly indicating that this team tends to have taller players on average compared to other teams in the dataset.

---
## 5. Reflection and Learning Outcomes
This project reinforced my understanding of SQL’s capabilities for data cleaning, transformation, and analysis. Using aggregate functions, conditional logic, joins, and window functions helped deepen my skills in extracting meaningful insights from structured data. Writing constraints and creating views also emphasized the importance of data integrity and reusable summaries.

---
## 6. Conclusion
By applying SQL querying techniques, I was able to analyze complex sports data to uncover trends and patterns related to player demographics and physical characteristics. This project highlights SQL’s utility as a powerful tool for statistical data analysis and database management.

---
**Contact:** dashinee.parmanum@gmail.com
