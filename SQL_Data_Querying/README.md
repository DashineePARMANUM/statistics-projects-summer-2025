# SQL Data Querying: Major League Baseball Players Dataset

This project showcases data analysis and querying in SQL using a major league baseball players dataset.

## Files and Folders
- **`SQL_Datasets`:**
  - `mlb_players_raw.csv` = Original raw dataset
  - `mlb_players.csv` = Modified dataset used to import data
- **`SQL_Docs`:**
  - `SQL_Report.md` = Detailed project overview and insights
  - `SQL_Process.md` = Step-by-step methodology
  - `SQL_Exercises.md` = Exercises/Questions
- **`SQL_Scripts`:**
  - `SQL_Queries.sql` = SQL queries for cleaning, exploration, and analysis

## Key Features
- Data import and table creation using PostgreSQL (PgAdmin).
- SQL querying for filtering, aggregation, and conditional logic.
- Use of window functions, views, joins, and constraints.
- Summary table/view creation for grouped statistics.
- Modular and reusable query structure.

## Skills Demonstrated
- SQL database setup and data import.
- Filtering, grouping, and aggregating data.
- CASE statements and conditional logic.
- JOIN operations for data enrichment.
- Data validation through constraints.

## Usage
- Load `mlb_players.csv` into your PostgreSQL database.
- Run `SQL_Queries.sql` (`SQL_Scripts`) using the Query Tool.
- Review methodology in `SQL_Process.md` (`SQL_Docs`).
- Explore questions and insights in `SQL_Exercises.md` and `SQL_Report.md` (`SQL_Docs`).
> Tip: If you're facing permission issues when importing `mlb_players.csv`, use a temporary directory close to your working database folder.

## Data Source and License
The dataset used in this project was obtained from the CSV data repository at https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html.
> "The computer code and data files described and made available on this web page are distributed under the GNU LGPL license."
GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007: https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt
