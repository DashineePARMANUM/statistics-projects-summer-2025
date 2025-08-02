## IN THE WORKS

# Python Data Analysis Process - Detailed Notes: Female Oscar Winners Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis - Summer 2025*

---
## 0. Original Data and Setup
- `oscar_age_female.csv` contains 89 female Oscar winners including their age, name, and movie.
- `oscar_age_female.csv` was renamed `oscar_age_female_raw.csv` to differentiate with the modifed dataset.
- A copy `oscar_age_female.csv` was modified in Excel to remove all " and unecessary spaces.
- All work was conducted using Visual Studio Code application.
```python
    # libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score
    import numpy as np
```

---
## 1. Import and Inspect
```python
    ## Load the dataset.
    data = pd.read_csv(r"C:\Users\dmpar\Documents\GitHub\statistics-projects-summer-2025\Python_Data_Analysis\Python_Datasets\oscar_age_female.csv")
    # strip leading/trailing spaces
    data.columns = data.columns.str.strip()

    ## Display the first few rows.
    # head + print function to display first rows
    print(data.head())

    ## What are the column names?
    print(data.columns.tolist())

    ## How many rows and columns are there?
    # rows
    print(data.shape[0])
    # columns
    print(data.shape[1])

    ## What data types are in each column?
    print(data.dtypes)

    ## Are there any missing values? If so, where?
    print(data.isnull().sum())
```
---
## 2. Summary Statistics
```python

```
---
## 3. Data Visualization
```python

```
`Python_Images` may be consulted for all screenshots.

---
## 4. Exploratory Questions
```python

```

---
## 5. Linear Regression
```python

```

---
## 6. Key Insights
- 
  
---
## 7. Challenges and Solutions
-

---
## 8. Final File
- The runnable Python script containing all functions/steps (with explantions) used in this report is saved in `Python_Final.py` (`Python_Scripts`).
- `Python_Final+Ans.py` (`Python_Scripts`) may also be consulted for the code and output in a single file.
- Any of those files can be executed directly in Visual Studio Code to reproduce the analyses and insights described above.

---
*Contact: dashinee.parmanum@gmail.com*  
*LinkedIn: https://www.linkedin.com/in/dashinee-parmanum/*