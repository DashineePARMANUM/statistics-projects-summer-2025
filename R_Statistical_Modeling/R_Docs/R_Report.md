# R Statistical Modeling Report: College Freshmen Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis - Summer 2025*

---
## 1. Introduction
This project looks at weight and BMI changes in college freshmen over the academic year using R. It explores overall trends in the data and includes some comparisons between males and females. The goal is to understand how students’ weight and BMI changed during the school year.

---
## 2. Data Description
- The dataset contains information for 67 students, including their weight in September and April, and their BMI in September and April.
- The data was sourced from the CSV data repository at https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html (`freshman_kgs.csv`).
- GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007: https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt

---
## 3. Methodology
- Imported the data using the *read.csv* function and inspected the data for missing values.
- Calculated summary statistics such as average weight in September.
- Used *ggplot2* to create histograms, scatterplots, and boxplots.
- Performed Statistical Testing, specifically t-tests.
- Built a linear regresison model using *lm* function; examined model residuals using base R plots to assess distribution and linearity assumptions.

---
## 4. Key Insights
- The average weight of students changed significantly from September to April.
- There was no statistically significant difference in average weight change between males and females from September to April.
- The strongest predictor of April weight is September weight, with a high R-squared value (~0.88), indicating a strong linear relationship.

---
## 5. Reflection and Learning Outcomes
This project reinforced my understanding of R for data cleaning, transformation, and analysis. Working with summary statistics, visualizations, regression models, and statistical tests helped deepen my ability to explore real-world data. 

---
## 6. Conclusion
By applying statistical techniques in R, I analyzed real-world student data to uncover trends in weight and BMI over time. This project highlights R’s utility as a powerful tool for data analysis, visualization, and model building in a statistical context.

---
**Contact:** dashinee.parmanum@gmail.com
