# Excel Data Cleaning and Analysis Report: Home Sales Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis — Summer 2025*

---
## 1. Introduction
This report documents the analysis of a home sales dataset using Microsoft Excel, focusing on calculating meaningful metrics and creating visualizations to explore real estate trends.

---
## 2. Data Description
The dataset contains information on 50 homes, including sale and asking prices, physical characteristics, age, and taxation. The data was sourced from the CSV data repository at https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html (`homes.csv`).  
GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007: https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt

---
## 3. Methodology
Before analysis, I calculated price differences and categorized homes as “expensive” based on price thresholds. Key Excel features utilized included conditional formatting to highlight data patterns, logical formulas (IF, SUMIF, COUNTIF) to aggregate information, and lookup functions (VLOOKUP) for enriching data with agent information.

Pivot tables:  
- Summarized average *Sell* by *Beds* (Table 1.1 - sheet *pivot table*)
  ![](statistics-projects-summer-2025/Excel_Data_Cleaning_and_Analysis/Excel_Images/Table1.1.png)
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
This project reinforced the application of Excel’s advanced features for practical data analysis tasks. Building a dashboard enhanced my skills in combining multiple Excel tools to present data accessibly. These competencies are valuable for statistical data analysis and business intelligence.

---
## 6. Conclusion
By combining logical computations and visualization in Excel, this project demonstrated effective methods for analyzing and presenting real estate data, offering actionable insights and showcasing essential analytical skills.

---
**Contact:** dashinee.parmanum@gmail.com
  
