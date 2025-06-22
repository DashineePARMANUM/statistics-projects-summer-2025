# SQL Data Querying Report: Major League Baseball Players Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis — Summer 2025*

---
## 1. Introduction
This project explores player data from Major League Baseball (MLB) using SQL. The main objective was to analyze trends in player characteristics (such as age, weight, and height) across teams and positions.

---
## 2. Data Description
The dataset contains information for 1034 professional baseball players, including their names, teams, positions, heights (in inches), weights (in pounds), and ages. The data was cleaned by removing special characters and renaming columns for compatibility/ease when working with SQL. The data was sourced from the CSV data repository at https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html (mlb_players.csv). 
GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007: https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt

---
## 3. Methodology

Before analysis, I calculated price differences and categorized homes as “expensive” based on price thresholds. Key Excel features utilized included conditional formatting to highlight data patterns, logical formulas (IF, SUMIF, COUNTIF) to aggregate information, and lookup functions (VLOOKUP) for enriching data with agent information.

Pivot tables:  
- Summarized average *Sell* by *Beds* (Table 1.1 - sheet *pivot table*) 
- Summarized total *Taxes* by *Age* groups (Table 2.1 - sheet *pivot table*)
- Summarized total *Sell* by *Age* group (Table 3.1 - sheet *pivot table*)

Charts:  
- Bar chart of average *Sell* by *Beds* (Chart 1.1 - sheet *chart*, derived from Table 1.1) 
- Scatter plot of *Living* vs *Sell* (Chart 2.1 - sheet *chart*, derived directly from *Sell* and *Living* columns of sheet *data*) 
- Line chart of total *Sell* across *Age* groups (Chart 3.1 - sheet *chart*, derived from Table 3.1)  

Dashboard:  
- All pivot tables and charts from sheets *pivot table* and *charts* were copied to sheet *dashboard*.
- Slicers:  
  - *Age* slicer added to Table 1.2
  - Connected *Beds* slicer added to Table 2.2 and 3.2  

---
## 4. Key Insights
- Six-bedroom homes tend to command the highest average *Sell* as seen in Table 1.2 in sheet *dashboard*.
- A positive correlation exists between *Living* and *Sell*, confirming intuitive real estate market trends as seen in Chart 3.2 in sheet *dashboard*.

---
## 5. Reflection and Learning Outcomes
This project reinforced my understanding of SQL’s capabilities for data cleaning, transformation, and analysis. Using aggregate functions, conditional logic, joins, and window functions helped deepen my skills in extracting meaningful insights from structured data. Writing constraints and creating views also emphasized the importance of data integrity and reusable summaries.

---
## 6. Conclusion
By applying SQL querying techniques, I was able to analyze complex sports data to uncover trends and patterns related to player demographics and physical characteristics. This project highlights SQL’s utility as a powerful tool for statistical data analysis and database management.

---
**Contact:** dashinee.parmanum@gmail.com
