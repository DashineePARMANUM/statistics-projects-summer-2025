## IN THE WORKS

#### Python Data Analysis: Female Oscar Winners Dataset
## Dashinee Parmanum - dashinee.parmanum@gmail.com - https://www.linkedin.com/in/dashinee-parmanum/
## Self-directed portfolio project in Statistics and Data Analysis - Summer 2025

#-------------------------------------------------------------------------------

#### code with output

#-------------------------------------------------------------------------------

# libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

### 1. Import and Inspect

## Load the dataset.
# use pandas
data = pd.read_csv(r"C:\Users\dmpar\Documents\GitHub\statistics-projects-summer-2025\Python_Data_Analysis\Python_Datasets\oscar_age_female.csv")
# strip leading/trailing spaces
data.columns = data.columns.str.strip()

## Display the first few rows.
# head + print function to display first rows
print(data.head())

## What are the column names?
print("Columns:", data.columns.tolist()) # Columns: [' Year', ' Age', ' Name', ' Movie', 'Unnamed: 4']

## How many rows and columns are there?
# rows
print(data.shape[0]) # 89
# columns
print(data.shape[1]) # 4

## What data types are in each column?
print(data.dtypes) # Year=int64; Age=int64; Name=object; Movie=object

## Are there any missing values? If so, where?
print(data.isnull().sum()) # no missing

#--------------------------------------------------------------------------------
### 2. Summary Statistics

## What is the average age of Oscar winners in this dataset?
print(data["Age"].mean()) # 36.12359550561798

## Who is the youngest and oldest winner? Include their names and movies.
# youngest
youngest = data.loc[data["Age"].idxmin()]
print("Youngest winner is" + youngest["Name"] + " of age " + str(youngest["Age"]) + " who starred in" + youngest["Movie"] + ".")
# Youngest winner is Marlee Matlin of age 21 who starred in Children of a Lesser God.
# oldest
oldest = data.loc[data["Age"].idxmax()]
print("Oldest winner is" + oldest["Name"] + " of age " + str(oldest["Age"]) + " who starred in" + oldest["Movie"] + ".")
# Oldest winner is Jessica Tandy of age 80 who starred in Driving Miss Daisy.

## How many winners were under 30? Over 50?
# under 30
print(len(data[data["Age"] < 30])) # 31
# over 50
print(len(data[data["Age"] > 50])) # 10

## What is the age range, standard deviation, and median age?
# range
print(data["Age"].max() - data["Age"].min()) # 59
# standard deviation
print(data["Age"].std()) # 11.745231357989796
# median
print(data["Age"].median()) # 33.0

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

## Create a histogram of ages using seaborn or matplotlib.
plt.figure(figsize=(8, 5))  # size of chart = 8x5
sns.histplot(data["Age"]) # create histogram
plt.title("Histogram of Age") # title
plt.xlabel("Age") # x-axis
plt.ylabel("Frequency") # y-axis
plt.show() # display

## Create a boxplot to visualize the distribution of ages.
plt.figure(figsize=(8, 5)) # size of chart = 8x5
sns.boxplot(x=data["Age"]) # create boxplot
plt.title("Boxplot of Age") # title
plt.show() # display

## Make a scatterplot of age vs index (or vs year if available).
plt.figure(figsize=(10, 5)) # size of chart = 8x5
sns.scatterplot(x=data.index, y=data["Age"]) # create scatterplot/plot points  
plt.title("Scatter of Age vs Index") # title
plt.xlabel("Age") # x-axis
plt.ylabel("Frequency") # y-axis
plt.show() # display 

## Create a bar chart of winners grouped by age ranges (e.g. 20s, 30s, 40s).
age_bins = pd.cut(data["Age"], bins=[20, 30, 40, 50, 60, 70], right=False) # create ranges
age_group_counts = age_bins.value_counts().sort_index() # count how many for each range + sort_index = ensure logical order
plt.figure(figsize=(8, 5)) # size of chart = 8x5
age_group_counts.plot(kind='bar')      # Create a vertical bar chart
plt.title("Histogram by Age range") # title
plt.xlabel("Age") # x-axis
plt.ylabel("Frequency") # y-axis
plt.show() # display 

#--------------------------------------------------------------------------------
### 4. Exploratory Questions
## Has the average age of winners increased or decreased over time?
## What is the most common age range for winning?
## Are there any outliers in the data? Who are they?
## How common are wins among actresses in their 20s compared to older age groups?

#--------------------------------------------------------------------------------
### 5. Linear Regression
## Build a linear regression model to predict age based on index (or year).
## What is the slope and intercept of the model?
## What is the R-squared value?
## Plot the regression line on your scatterplot.
## Plot the residuals. Do they appear normally distributed?