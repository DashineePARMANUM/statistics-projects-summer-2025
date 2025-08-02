#### Python Data Analysis: Female Oscar Winners Dataset
## Dashinee Parmanum - dashinee.parmanum@gmail.com - https://www.linkedin.com/in/dashinee-parmanum/
#### Python Data Analysis: Female Oscar Winners Dataset
## Dashinee Parmanum - dashinee.parmanum@gmail.com - https://www.linkedin.com/in/dashinee-parmanum/
## Self-directed portfolio project in Statistics and Data Analysis - Summer 2025

#-------------------------------------------------------------------------------

#### only code

#-------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

### 1. Import and Inspect

## Load the dataset.
data = pd.read_csv(r"C:\Users\dmpar\Documents\GitHub\statistics-projects-summer-2025\Python_Data_Analysis\Python_Datasets\oscar_age_female.csv")
data.columns = data.columns.str.strip()

## Display the first few rows.
print(data.head())

## What are the column names?
print(data.columns.tolist())

## How many rows and columns are there?
print(data.shape[0])
print(data.shape[1])

## What data types are in each column?
print(data.dtypes)

## Are there any missing values? If so, where?
print(data.isnull().sum())

#--------------------------------------------------------------------------------
### 2. Summary Statistics

## What is the average age of Oscar winners in this dataset?
print(data["Age"].mean())

## Who is the youngest and oldest winner? Include their names and movies.
youngest = data.loc[data["Age"].idxmin()]
print("Youngest winner is" + youngest["Name"] + " of age " + str(youngest["Age"]) + " who starred in" + youngest["Movie"] + ".")
oldest = data.loc[data["Age"].idxmax()]
print("Oldest winner is" + oldest["Name"] + " of age " + str(oldest["Age"]) + " who starred in" + oldest["Movie"] + ".")

## How many winners were under 30? Over 50?
print(len(data[data["Age"] < 30]))
print(len(data[data["Age"] > 50]))

## What is the age range, standard deviation, and median age?
print(data["Age"].max() - data["Age"].min())
print(data["Age"].std())
print(data["Age"].median())

## Are there more winners in their 20s or 30s?
difference_20_30 = len(data[(data["Age"] >= 20) & (data["Age"] < 30)]) - len(data[(data["Age"] >= 30) & (data["Age"] < 40)])
if difference_20_30 > 0:
    print("More winners in their 20s.")
elif difference_20_30 < 0:
    print("More winners in their 30s.")
else:
    print("Equal number of winners in their 20s and 30s.")

#--------------------------------------------------------------------------------
### 3. Data Visualization

## Create a histogram of ages.
plt.figure(figsize=(8, 5))
sns.histplot(data["Age"])
plt.title("Histogram of Age")
plt.xlabel("Age") 
plt.ylabel("Frequency")
plt.show() 

## Create a boxplot to visualize the distribution of ages.
plt.figure(figsize=(8, 5))
sns.boxplot(x=data["Age"])
plt.title("Boxplot of Age")
plt.show() 

## Make a scatterplot of age vs index.
plt.figure(figsize=(8, 5))
sns.scatterplot(x=data.index, y=data["Age"])  
plt.title("Scatter of Age vs Index")
plt.xlabel("Index")
plt.ylabel("Age")
plt.show() 

## Create a bar chart of winners grouped by age ranges (e.g. 20s, 30s, 40s).
age_bins = pd.cut(data["Age"], bins=[20, 30, 40, 50, 60, 70], right=False)
age_group_counts = age_bins.value_counts().sort_index() 
plt.figure(figsize=(8, 5))
age_group_counts.plot(kind='bar')
plt.title("Bar Chart by Age range")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#--------------------------------------------------------------------------------
### 4. Exploratory Questions

## Has the average age of winners increased or decreased over time? - Chart 5
data_sorted_year = data.sort_values("Year") 
plt.figure(figsize=(8, 5))
sns.lineplot(x="Year", y="Age", data=data_sorted_year) 
sns.regplot(x="Year", y="Age", data=data_sorted_year, scatter=False, color="red", label="Trend Line")
plt.title("Age through the years")
plt.xlabel("Year")
plt.ylabel("Age")
plt.show() 

## What is the most common age range for winning?
print(age_group_counts.idxmax())

## Are there any outliers in the data? Who are they?
Q1 = data["Age"].quantile(0.25)
Q3 = data["Age"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(data[(data["Age"] < lower_bound) | (data["Age"] > upper_bound)])

## How common are wins among actresses in their 20s compared to older age groups?
print(age_bins.value_counts().sort_index())

#--------------------------------------------------------------------------------
### 5. Linear Regression

## Build a linear regression model to predict age based on index (or year).
x = data[["Year"]]
y = data["Age"]
model = LinearRegression()
model.fit(x, y)

## What is the slope and intercept of the model?
print(model.coef_[0])
print(model.intercept_)

## What is the R-squared value?
y_pred = model.predict(x)
print(r2_score(y, y_pred))

## Plot the regression line on your scatterplot.
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Year", y="Age", data=data_sorted_year)
plt.plot(data["Year"], y_pred)
plt.title("Linear Regression: Age vs Year")
plt.xlabel("Year")
plt.ylabel("Age")
plt.legend()
plt.show()

## Plot the residuals. Do they appear normally distributed?
residuals = y - y_pred
plt.figure(figsize=(8, 5))
sns.histplot(residuals, kde=True)
plt.title("Distribution of Residuals")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.show()