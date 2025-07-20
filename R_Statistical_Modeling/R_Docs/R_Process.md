# R Statistical Modeling Process - Detailed Notes: College Freshmen Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis - Summer 2025*

---
## 0. Original Data and Setup
- `freshman_kgs.csv` contains 67 college freshmen including their sex, weight(kg) in Septemer and April, and BMI in September and April.
- All work was conducted using R Studio application.

---
## 1. Import and Inspect
```R
## Load the dataset into R and display the first few rows.
# load dataset
data <- read.csv("freshman_kgs.csv")
# display first rows
head(data)

## What are the column names?- Are they formatted properly (no spaces, lowercase, etc.)?
# displays columns names
colnames(data) 
# remove spaces/_ from columns names
colnames(data) <- tolower(gsub(" ", "_", colnames(data)))

## How many rows and columns are there?
# display dataset dimensions
dim(data)

## What data types are in each column?
# displays each column data type
str(data) 

## Are there any missing values? If so, where?
# check for missing values
colSums(is.na(data))
```
---
## 2. Summary Statistics
```R
## What is the average September weight and April weight for the full group?
# find average for september
average_weight_september <- mean(data$weight..sep.) 
# find average for april
average_weight_april <- mean(data$weight..apr.) 

## Compute the average weight change from September to April.
# create weight change column
data$weight_change <- data$weight..apr. - data$weight..sep.
# find average
average_weight_change <- mean(data$weight_change) 

## Do males or females have a higher average weight change?
# create 2 separate datasets
dataM <- subset(data, sex == "M")
dataF <- subset(data, sex == "F")
# find average weight change in males
dataM$weight_change <- dataM$weight..apr. - dataM$weight..sep.
mean_weight_change_males <- mean(dataM$weight_change)
# find average weight change in females
dataF$weight_change <- dataF$weight..apr. - dataF$weight..sep.
mean_weight_change_females <- mean(dataF$weight_change) 

# other way of doing this using built-in function
aggregate(weight_change ~ sex, data = data, mean) 

## What is the standard deviation of BMI in September vs April?
# find standard deviation for September BMI
StdDev_September <- sd(data$bmi..sep.)
# find standard deviation for April BMI
StdDev_April <- sd(data$bmi..apr.) 

## Which student gained the most weight?
# display row with highest Weight Change
data[which.max(data$weight_change), ]
```
---
## 3. Data Visualization
```R
# import library need for all ggplot functions
library(ggplot2) # library for plots

# ggplot = choose dataset/cols/etc
# labs = add title/x-axis/y-axis
# theme = center title (hjust = 0/default: left; 0.5: centered; 1: right)

## Create a histogram of April weights.
# geom_histogram = build the histogram
ggplot(data, aes(x = `weight..apr.`))+ geom_histogram() + 
  labs(title = "Histogram of April Weights", x = "Weight", y = "Frequency") +
  theme(plot.title = element_text(hjust = 0.5))

## Create a boxplot comparing April BMI by sex.
# geom_boxplot = build the boxplot
ggplot(data, aes(x = sex, y = `bmi..apr.`)) + geom_boxplot() + 
  labs(title = "Boxplot of April BMI by Sex", x = "Sex", y = "BMI") + 
  theme(plot.title = element_text(hjust = 0.5))

## Make a scatterplot of September vs April weight.
# geom_point = plot points
ggplot(data, aes(x = `weight..sep.`, y = `weight..apr.`)) + geom_point() +
  labs(title = "Scatter Plot of Weight: September vs April",
       x = "Weight in September",y = "Weight in April") + 
  theme(plot.title = element_text(hjust = 0.5))

## Add a regression line to the scatterplot.
# geom_smooth = add regression line
ggplot(data, aes(x = `weight..sep.`, y = `weight..apr.`)) + 
  geom_point() + geom_smooth(method = "lm") +
  labs(title = "Scatter Plot of Weight: September vs April",
       x = "Weight in September", y = "Weight in April") + 
  theme(plot.title = element_text(hjust = 0.5))

## Plot a histogram of weight changes (April-September).
# geom_histogram = build histogram
ggplot(data, aes(x = `weight_change`)) + geom_histogram() +
  labs(title = "Histogram of Weight Change", x = "Weight Change", y = "Frequency") + 
  theme(plot.title = element_text(hjust = 0.5))
```
---
## 4. Statistical Testing
```R
## Perform a paired t-test to determine if average weight changed significantly from September to April.
t.test(data$weight..sep., data$weight..apr., paired = TRUE)

## Perform an independent t-test to compare weight change between males and females.
t.test(weight_change ~ sex, data)
```
---
## 5. Linear Regression
```R
## Build a linear regression model to predict April weight using September weight.
# build regression model
model <- lm(`weight..apr.` ~ `weight..sep.`, data)
# display summary
summary(model)

## What is the slope and intercept? Interpret them.
# see summary display

## What is the Rsquared value?
# see summary display

## Plot the residuals and check if they seem normally distributed.
# Residual plot
plot(model$residuals, main = "Residuals Plot", ylab = "Residuals") 

# Histogram of residuals
hist(model$residuals, main = "Histogram of Residuals", xlab = "Residuals")

# Q-Q plot with x-y line
qqnorm(model$residuals)
qqline(model$residuals)
```
---
## 6. Key Insights
- The average weight of students changed from September to April.
- Males did not gain more weight on average than females over the academic year.
- The strongest predictor of April weight is September weight, with a high R-squared value (~0.88), indicating a strong linear relationship.
  
---
## 7. Challenges and Solutions
- Residual plot generation with ggplot: *ggplot(model, aes(...))* didn’t work since *model* is not a data frame.
  - Switched to base R plotting for residual analysis to avoid unnecessary transformation or copying.
- Sex-based comparisons: Creating subsets for males and females was straightforward
  - However, I also learned to use *aggregate()* for more concise group-based statistics.

---
## 8. Final File
-

---
**Contact:** dashinee.parmanum@gmail.com
