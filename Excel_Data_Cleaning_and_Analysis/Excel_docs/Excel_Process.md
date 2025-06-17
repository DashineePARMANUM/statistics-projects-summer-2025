# Excel Data Cleaning and Analysis Process - Detailed Notes: Home Sales Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis — Summer 2025*

---
## 1. Original Data and Setup
- "homes.csv" contains 50 home listings
- Converted the .csv file to .xlsx and rename sheet *data*.
- Created a *home ID* column (leftmost) to identify homes (numebr 1-50).
- Froze the top row to keep headers visible and the first column to keep home IDs visible while scrolling.
- Columns:
    A = home ID - added
    B = Sell (selling price)
    C = "List" (asking price)
    D = Price difference - added
    E = Is Expensive? (> 150) - added
    F = "Living" (living space)
    G = "Rooms" (rooms)
    H = "Beds" (bedrooms)
    I = “Baths” (bathrooms)
    J = “Age” (age)
    K = “Acres” (acreage)
    L = “Taxes” (taxes)
    M = 0.05 tax rate - added
    N = Bi * 0.05 - checking M - added

---
## 2. Data Cleaning and some Calculations
- Created column *Price Difference* with formula: Di =Ci-Bi for i = 2-51
- Created column *Is Expensive? (> 150)?* with formula: =IF(Bi>150, "yes", "no") for i = 2-51
- Calculated total selling price with formula: =SUM(B2:B51) 
- Calculated average living space with formula: =AVERAGE(F2:F51)
- Calculated total selling price for home with more than 4 bedrooms with formual: =SUMIF(H2:H51,">4",B2:B51)
- Count number of houses less than 50 years old with formula: =COUNTIF(J2:J51,"<50")

---
## 3. Conditional Formatting and Data Validation

- Applied **color scales** to Selling Price for visual differentiation.

- Added **data bars** to Bedrooms column for visual emphasis.

- Used **icon sets** on Price Difference:
  - Up arrow if positive,
  - Down arrow if negative,
  - Sideways arrow if zero.

- Applied **data validation** on Bedrooms column to restrict input to whole numbers between 1 and 10.

---
## 4. Absolute and Relative References

- Placed a fixed tax rate of 5% in a cell (`M52 = 0.05`).

- Calculated 5% tax on selling price using absolute cell referencing:  
  `=B2 * $M$52` in `M2`, copied down.

- Added a check column `(B2 * 0.05) - M2` to verify correct calculations.

---

## 5. Sheet Protection
- Unlocked the Price Difference column to allow editing.

- Protected the sheet with a password to prevent accidental edits on locked cells.

- Tested protection by trying to edit both locked and unlocked cells — worked as expected.

---
## 6. Lookup Functions

- Created a small agent lookup table with Home ID and Agent Name.

- Used `VLOOKUP` to fetch the agent name corresponding to each Home ID:  
  `=VLOOKUP(A2, $P$2:$Q$4, 2, FALSE)`

- Ensured exact matches to avoid errors.

---
## 7. Pivot Tables

- Created pivot tables for summarized insights:

  - **Average Selling Price by Bedrooms:**  
    Rows: Bedrooms; Values: Average of Selling Price.

  - **Total Taxes by Age Groups:**  
    Grouped Age into brackets (0–10 years, 11–20 years, etc.) and summed Taxes.

  - **Total Selling Price by Age Groups:**  
    Similar grouping, sum of Selling Price.

- Applied filters on Bathrooms to focus on homes with 3 or 4 baths in some views.

---
## 8. Charts

- Made charts for visual analysis:

  - **Bar chart** of average selling price by bedrooms (linked to first pivot table).

  - **Scatter plot** of Living Space vs Selling Price (from raw data).

  - **Line chart** showing total selling price by age groups.

- Customized chart titles, axis labels, and legend for clarity.

---
## 9. Dashboard Creation

- Created a new sheet named `Dashboard`.

- Consolidated all pivot tables and charts into this sheet for easy overview.

- Added slicers to filter dynamically by Age groups and Bedrooms.

- Connected slicers to multiple pivot tables for synchronized filtering.

---
## 10. Key Insights

- Homes with **6 bedrooms** have the highest average selling prices.

- There is a clear **positive correlation** between living space and selling price, consistent with market expectations.

---
## 11. Challenges and Solutions

- Grouping ages into bins required using Pivot Table Group feature.

- Ensuring consistent Home IDs for `VLOOKUP` required careful table range and absolute references.

- Locked/unlocked cell protection required trial and error to allow edits only where needed.

---
## 12. Final File

- All data, analysis, pivot tables, charts, and dashboard are saved in the file **home.xlsx**.
