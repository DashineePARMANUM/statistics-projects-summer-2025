# Power BI Visualization Process - Detailed Notes: Grades Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis - Summer 2025*

---
## 0. Original Data and Setup
- `grades.csv` contains 16 students including their first and last names, marks for test 1, 2, 3 and 4, and final marks and letter grade (CSV data repository at https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html - GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007: https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt).
- Started with a blank project.

---
## 1. Import and Clean Data
- Imported the data from `grades.csv`.
- Transformed data:
  - Turned on *Use first row as headers*.
   - Removed all , (comas) in the cells.
- Confirmed that the data types were set up properly.

---
## 2. Create Basic Visuals
- Created slide *BarChart-AvgTest*.
  - Added Chart 1.1 = bar chart displaying the average score of each test.
- Created slide *ColChart-Final*.
  - Added Chart 2.1 = column chart displaying the final score by student.
- Created slide *PieChart-Letter*.
  - Added Chart 3.1 = pie chart dispalying the percentage of student who obtianed each grade (Count is dispalyed when hovering over segment).
- Created slide *Basic Visuals* and copied all charts:
  -  Chart 1.2 = copy of Chart 1.1
  -  Chart 2.2 = copy of Chart 2.1
  -  Chart 3.2 = copy of Chart 3.1
    
---
## 3. Use Slicers and Filters
- Duplicated slide *Basic Visuals* and renamed it *Slicers*.
- Renamed the charts:
  -  Chart 1.3 = copy of Chart 1.1
  -  Chart 2.3 = copy of Chart 2.1
  -  Chart 3.3 = copy of Chart 3.1
- Created Slicer 1.1 = allows to select any of the grades, creating a filter on the all charts on the slide.
- Created Slicer 2.1 = allows to select any student last name, creating a filter on the all charts on the slide.
- The slicers may be combined by selecting any grade in Slicer 1.1 and any last anme in Slicer 2.1. 

---
## 4. Create Cards and KPIs
- Created slide *Cards*.
- Added Card 1.1 = *Count of Last name* = shows number of students.
- Added Card 2.1 = *Average of Final* = shows average mark of final.
- Added Card 3.1 = *Max of Test1* = shows highest mark for test 1.

---
## 5. Write Basic DAX
- Switched to Table View.
- Created New Column: AverageTestScore = ([Test1] + [Test2] + [Test3] + [Test4]) / 4
- Created New Measure: OverallAverageTestScore= AVERAGE(grades[AverageTestScore]) 
  - Added Card 4.1 to slide *Cards* = *OverallAverageTestScore*.

---
## 6. Add Tooltips and Interactions
- Add tooltips to your charts (e.g., when hovering over a bar, show student name and average score).
- Customize interactions between charts (e.g., clicking a slice of the pie filters the bar chart).

---
## 7.  Create a Simple Dashboard
- Arrange your charts, slicers, and cards into a clean layout on one page.
- Name the page *Student Performance Dashboard*.
- Add a title using a Text box.
- Format colors and fonts for readability.

---
## 8. Key Insights
- 

---
## 9. Challenges and Solutions
- 

---
## 10. Final File
- 

---
**Contact:** dashinee.parmanum@gmail.com
