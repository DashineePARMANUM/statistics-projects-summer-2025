# Excel Data Cleaning and Analysis Exercises: Home Sales Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis — Summer 2025*

---

## 1. Freeze Panes (Freezing Rows/Columns)
- Freeze the top row to keep headers visible when scrolling vertically.  
- Freeze the first column to keep home IDs visible when scrolling horizontally.

## 2. Basic Formulas & Functions
- Create a column **Price Difference** = Selling Price - Asking Price.  
- Create a column **Is Expensive** using `IF`: if Selling Price > 500,000 then “Yes” else “No”.  
- Calculate total Selling Price using `SUM`.  
- Calculate average Living Space using `AVERAGE`.

## 3. Conditional Sum and Count
- Use `SUMIF` to calculate total Selling Price for homes with more than 4 bedrooms.  
- Use `COUNTIF` to count homes with age less than 10 years.

## 4. Conditional Formatting
- Apply color scales to Selling Price.  
- Add data bars to Bedrooms column.  
- Use icon sets on Price Difference (up arrow for positive, down arrow for negative, sideways for zero).

## 5. Data Validation
- Add data validation on Bedrooms column to allow only whole numbers between 1 and 10.

## 6. Absolute vs Relative Cell References
- Put 0.05 (tax rate) in a separate cell.  
- Calculate 5% tax on Selling Price using an absolute reference for the tax rate.  
- Copy the formula down and check results.

## 7. Locking Cells and Protecting Sheet
- Unlock Price Difference column.  
- Protect the sheet so only unlocked cells can be edited.  
- Test by trying to edit locked and unlocked cells.

## 8. Lookup Functions
- Create a small lookup table for Agent Names by Home ID.  
- Use `VLOOKUP` to fetch Agent Name for a Home ID.

## 9. Pivot Tables
- Create a pivot table showing average Selling Price by Bedrooms.  
- Create a pivot table showing total Taxes grouped by home age brackets (0-10, 11-20 years).  
- Filter the pivot table to show homes with more than 2 bathrooms.

## 10. Charts
- Make a bar chart of average Selling Price by Bedrooms.  
- Make a scatter plot of Living Space vs Selling Price.  
- Make a line chart showing total Selling Price across age groups.

## 11. Mini Dashboard
- Create a new sheet named “Dashboard”.  
- Insert pivot tables and charts.  
- Add slicers to filter by Bedrooms or Age bracket.  
- Write a summary answering:  
  - Which bedroom count has the highest average selling price?  
  - Is there a correlation between Living Space and Selling Price?
 
 ---
**Contact:** dashinee.parmanum@gmail.com
