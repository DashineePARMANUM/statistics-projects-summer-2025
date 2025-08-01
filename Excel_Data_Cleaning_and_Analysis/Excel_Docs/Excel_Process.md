# Excel Data Cleaning and Analysis Process - Detailed Notes: Home Sales Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis - Summer 2025*

---
## 0. Original Data and Setup
- `homes.csv` contains 50 home listings with selling price, asking price, living space, rooms, bedrooms, bathrooms, age, acreage and taxes (CSV data repository at https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html - GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007: https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt).
- Converted the .csv file to .xlsx and rename sheet *data*.
- Created a *home ID* column (leftmost) to identify homes (number 1-50).

---
## 1. Freeze Panes (Freezing Rows/Columns)
- Froze the top row to keep headers visible and the first column to keep home IDs visible while scrolling.

---
## 2. Basic Formulas & Functions
- Created column *Price Difference* with formula: Di =Ci-Bi for i = 2-51
- Created column *Is Expensive? (> 150)?* with formula: =IF(Bi>150, "yes", "no") for i = 2-51
- Calculated total *Sell* with formula: =SUM(B2:B51) 
- Calculated average *Living* with formula: =AVERAGE(F2:F51)

---
## 3. Conditional Sum and Count
- Calculated total *Sell* for homes with more than 4 *Beds* with formula: =SUMIF(H2:H51,">4",B2:B51)
- Count number of houses less than 50 years old with formula: =COUNTIF(J2:J51,"<50")

---
## 4. Conditional Formatting
- Applied color scales to column *Sell* for visual differentiation (Red to Green scale, red being most expensive).
- Added data bars to column *Beds* for visual emphasis (Longer bars for more *Beds*).
- Added icon sets to *Price Difference* (Up arrow for positive, Down arrow for negative and Sideways arrow for 0).

---
 ## 5. Data Validation
- Applied data validation on column *Beds* to restrict input to whole numbers between 1 and 10.

---
## 6. Absolute vs Relative Cell References
- Placed a fixed tax rate of 5% in a cell (M52 = 0.05).
- Created column *0.05 tax rate* with formula: =Bi*$M$52 for i = 2-51
- Created column *Bi * 0.05 - checking M* with formula: =(Bi*0.05)-Mi for i = 2-51

---
## 7. Locking Cells and Protecting Sheet
- Unlocked the column *Price Difference* to allow editing.
- Protected the sheet with a password to prevent accidental edits on locked cells.
- Tested protection by trying to edit both locked and unlocked cells — worked as expected.

---
## 8. Lookup Functions
- Created a small agent lookup table with *home ID* and *Agent Name*.
- Used VLOOKUP to fetch the *Agent Name* corresponding to each *home ID* (=VLOOKUP(A2,$P$2:$Q$4,2,FALSE))
 
---
## 9. Pivot Tables
- Created 3 pivot tables for summarized insights:
  - Table 1.1 (sheet *pivot table* or `Excel_Images` for screenshot) = average *Sell* by *Beds* (Rows: *Beds*; Values: Average of *Sell*)
    - Applied filter to focus on homes with 3 or 4 *Baths*
  - Table 2.1 (sheet *pivot table* or `Excel_Images` for screenshot) = total *Taxes* by *Age* groups (Grouped *Age* into brackets and summed *Taxes*)
  - Table 3.1 (sheet *pivot table* or `Excel_Images` for screenshot) = total *Sell* by *Age* groups (Grouped *Age* into brackets and summed *Sell*)
 
---
## 10. Charts
- Made charts for visual analysis:
  - Chart 1.1 (sheet *chart* or `Excel_Images` for screenshot, derived from Table 1.1) = bar chart of average *Sell* by *Beds* 
  - Chart 2.1 (sheet *chart* or `Excel_Images` for screenshot, derived directly from *Sell* and *Living* columns of sheet *data*) = scatter plot of *Living* vs *Sell* 
  - Chart 3.1 (seesheet *chart* or `Excel_Images` for screenshot, derived from Table 3.1) = line chart of total *Sell* across *Age* groups
  - Customized chart titles, axis labels, and legend for clarity.

---
## 11. Mini Dashboard
- Created a new sheet named *dashboard*.
- Consolidated all pivot tables and charts into this sheet for easy overview.
   - Table 1.2 = copy of Table 1.1
   - Table 2.2 = copy of Table 2.1
   - Table 3.2 = copy of Table 3.1
   - Chart 1.2 = copy of Chart 1.1
   - Chart 2.2 = copy of Chart 2.1
   - Chart 3.2 = copy of Chart 3.1
- Added slicers to filter dynamically by *Age* groups (Table 1.2) and *Beds* (Tables 2.2 and 3.2).
- Connected slicers to multiple pivot tables for synchronized filtering (Tables 2.2 and 3.2).
- (`Excel_Images` for screenshot)

---
## 12. Key Insights
- Homes with 6 bedrooms have the highest average *Sell* as seen in Table 1.2 in sheet *dashboard*.
- There is a clear positive correlation between *Living* and *Sell*, consistent with market expectations as seen in Chart 3.2 in sheet *dashboard*.

---
## 13. Challenges and Solutions
- Grouping ages into bins required using Pivot Table Group feature.
- Locked/unlocked cell protection required trial and error to allow edits only where needed.

---
## 14. Final File
- All data, analysis, pivot tables, charts, and dashboard are saved in `homes.xlsx` (`Excel_Datasets`).

---
*Contact: dashinee.parmanum@gmail.com*  
*LinkedIn: https://www.linkedin.com/in/dashinee-parmanum/*