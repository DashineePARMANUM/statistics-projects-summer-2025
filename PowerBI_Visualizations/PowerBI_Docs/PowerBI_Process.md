# Power BI Visualization Process - Detailed Notes: Grades Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis - Summer 2025*

---
## 0. Original Data and Setup
- Started with a blank project.

---
## 1. Import and Clean Data
- Import data.
  - Imported the data from `grades.csv`.
- Inspect the fields: Rename them if needed.
  - No renaming, but data was transformed:
    - Turned on *Use first row as headers*.
    - Removed all , (comas) in the cells.
- Set appropriate data types.  
  - Confirmed that the data types were set up properly.

---
## 2. Create Basic Visuals
- Create a bar chart showing the average score of each test.
  - Created Chart 1.1 on slide *BarChart-AvgTest* which is a bar chart displaying the average score of each test.
- Create a column chart showing the final scores by student.
  - Created Chart 2.1 on slide *ColChart-Final* which is a column chart displaying the final score by student.
- Create a pie chart or donut chart showing the distribution of letter grades.
  - Created Chart 3.1 on slide *PieChart-Letter* which is a pie chart dispalying the percentage of student who obtianed each grade (Count is dispalyed when hoverign on a specific segment).

---
## 3. Use Slicers and Filters
- Add a slicer to filter by *Grade* (e.g., A, B, C).
- Add a second slicer to filter by *Last Name* (alphabetically or search box).
- Try combining filters (e.g., show only students with *Grade* "A" whose *Last Name* starts with “M”).

---
## 4. Create Cards and KPIs
- Add a Card to show the number of students.
- Add a Card to show the average *Final Score*.
- Add a Card showing the highest *Test 1 score*.

---
## 5. Write Basic DAX
- Create a calculated column called *AvgTestScore*:
- Create a measure for the overall average of all students' 1*AvgTestScore*:
- Add a Card for this measure.

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
