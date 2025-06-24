## IN THE WORKS

# Power BI Visualization Exercises: Grades Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis — Summer 2025*

---
## 0. Original Data and Setup
- 

---
## 1. Import and Clean Data
- Import data.
- Inspect the fields: Rename them if needed.
- Set appropriate data types.

---
## 2. Create Basic Visuals
- Create a **bar chart** showing the average score of each test.
- Create a **column chart** showing the final scores by student.
- Create a **pie chart** or **donut chart** showing the distribution of letter grades.

---
## 3. Use Slicers and Filters
- Add a **slicer** to filter by `Grade` (e.g., A, B, C).
- Add a second slicer to filter by `Last Name` (alphabetically or search box).
- Try combining filters (e.g., show only students with Grade "A" whose last name starts with “M”).

---
## 4. Create Cards and KPIs
- Add a **Card** to show the number of students (`Count`).
- Add a Card to show the **average Final Score**.
- Add a Card showing the **highest Test 1 score**.

---
## 5. Write Basic DAX
- Create a **calculated column** called `AvgTestScore`:
   ```DAX
   AvgTestScore = ([Test1] + [Test2] + [Test3] + [Test4]) / 4
   ```

- Create a measure for the overall average of all students' AvgTestScore:
```DAX
AverageTestScore = AVERAGE(grades[AvgTestScore])
```

- Add a Card for this measure.

---
## 6. Add Tooltips and Interactions
- Add tooltips to your charts (e.g., when hovering over a bar, show student name and average score).
- Customize interactions between charts (e.g., clicking a slice of the pie filters the bar chart).

---
## 7.  Create a Simple Dashboard
- Arrange your charts, slicers, and cards into a clean layout on one page.
- Name the page "Student Performance Dashboard".
- Add a title using a Text box.
- Format colors and fonts for readability.

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
- All data, analysis, pivot tables, charts, and dashboard are saved in the file `homes.xlsx` (`Excel_Datasets`).

---
**Contact:** dashinee.parmanum@gmail.com