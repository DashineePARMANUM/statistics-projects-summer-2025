# Power BI Visualization Process - Detailed Notes: Grades Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis - Summer 2025*

---
## 0. Original Data and Setup
- `grades.csv` contains 16 students including their first and last names, marks for test 1-4, and final marks and letter grades (CSV data repository at https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html - GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007: https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt).
- Started with a blank project.

---
## 1. Import and Clean Data
- Imported the data from `grades.csv`.
- Transformed data:
  - Enabled 'Use first row as headers'.
   - Removed all , (commas) in the cells.
- Confirmed that the data types were set up properly.

---
## 2. Create Basic Visuals
- Created slide *BarChart-AvgTest*.
  - Added Chart 1.1 = bar chart displaying the average score of each test.
- Created slide *ColChart-Final*.
  - Added Chart 2.1 = column chart displaying the final score by student.
- Created slide *PieChart-Letter*.
  - Added Chart 3.1 = pie chart displaying the percentage of students who obtained each grade (Count is displayed when hovering over segment).
- Created slide *Basic Visuals* and copied all charts:
  -  Chart 1.2 = copy of Chart 1.1
  -  Chart 2.2 = copy of Chart 2.1
  -  Chart 3.2 = copy of Chart 3.1
    
---
## 3. Use Slicers and Filters
- Duplicated slide *Basic Visuals* and renamed it *Slicers*.
- Renamed the charts:
  -  Chart 1.3 = copy of Chart 1.2
  -  Chart 2.3 = copy of Chart 2.2
  -  Chart 3.3 = copy of Chart 3.2
- Created Slicer 1.1 = allows to select any of the grades, creating a filter on all charts on the slide.
- Created Slicer 2.1 = allows to select any student last name, creating a filter on all charts on the slide.
- The slicers may be combined by selecting any grade in Slicer 1.1 and any last name in Slicer 2.1. 

---
## 4. Create Cards and KPIs
- Created slide *Cards*.
- Added Card 1.1 = *Count of Last name* = shows number of students.
- Added Card 2.1 = *Average of Final* = shows average mark of final.
- Added Card 3.1 = *Max of Test1* = shows highest mark for test 1.

---
## 5. Write Basic DAX
- Switched to Table View.
- Created New Column: AverageTestScore = ([Test1] + [Test2] + [Test3] + [Test4]) / 4.
- Created New Measure: OverallAverageTestScore= AVERAGE(grades[AverageTestScore]).
  - Added Card 4.1 to slide *Cards* = *OverallAverageTestScore*.

---
## 6. Add Tooltips and Interactions
- Switch back to Report View.
- Duplicated slide *Basic Visuals* and renamed it *Tooltips*.
- Renamed the charts:
  -  Chart 1.4 = copy of Chart 1.2
  -  Chart 2.4 = copy of Chart 2.2
  -  Chart 3.4 = copy of Chart 3.2
- Added tooltips:
  - Dragged *Max of AverageTestScore* to Tooltips for Chart 1.4.
  - Dragged *Average of Test1* to Tooltips for Chart 3.4.

---
## 7.  Create a Simple Dashboard
- Duplicated slide *Slicers* and renamed it *Dashboard*.
- Renamed the charts:
  -  Chart 1.5 = copy of Chart 1.3
  -  Chart 2.5 = copy of Chart 2.3
  -  Chart 3.5 = copy of Chart 3.3
- Copied the Cards from slide *Cards* and renamed them:
  -  Card 1.2 = copy of Card 1.1
  -  Card 2.2 = copy of Card 2.1
  -  Card 3.2 = copy of Card 3.1
  -  Card 4.2 = copy of Card 4.1
- Added textbox for title = *Student Performance Dashboard*.
- Moved charts, cards and textbox around to fit everything cleanly.
    
---
## 8. Key Insights
- Students with higher average test scores generally received higher final grades.
- The majority of students fall into the B grade as seen on the pie chart.
- The lowest performance on average occurred in Test 2, as shown in the bar chart.

---
## 9. Challenges and Solutions
- `grades.csv` had , (commas) within cells creating a formatting issues.
  - Transformed data by replacing , with blanks.
- Trouble fitting everything on slide *Dashboard*.
  - Changed the size of the charts, cards, slicers and text when needed.
  
---
## 10. Final File
- All slides are saved in `PowerBI_Final.pbix` (`PowerBI_Dashboards`).
- A pdf version is also available = `PowerBI_Final.pdf` (`PowerBI_Dashboards`):
  - Page 1 = slide *BarChart-AvgTest*
  - Page 2 = slide *ColChart-Final*
  - Page 3 = slide *PieChart-Letter*
  - Page 4 = slide *Basic Visuals*
  - Page 5 = slide *Slicers*
  - Page 6 = slide *Cards*
  - Page 7 = slide *Tooltips*
  - Page 8 = slide *Dashboard*
    
---
**Contact:** dashinee.parmanum@gmail.com
