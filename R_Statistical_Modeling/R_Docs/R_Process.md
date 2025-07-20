## IN THE WORKS

# R Statistical Modeling Process - Detailed Notes: College Freshmen Dataset

**Dashinee Parmanum**  
*Self-directed portfolio project in Statistics and Data Analysis - Summer 2025*

---
## 0. Original Data and Setup
- `freshman_kgs.csv` contains 67 college freshmen including their sex, weight(kg) in Septemer and April, and BMI in September and April.
- All work was conducted using R Studio application.

---
## 1. Import and Inspect

## Load the dataset into R and display the first few rows.
```R
data <- read.csv("freshman_kgs.csv")
head(data)
```

## What are the column names?- Are they formatted properly (no spaces, lowercase, etc.)?
colnames(data) # sex, weight..sep., weight..apr., bmi..sep., bmi..apr.
colnames(data) <- tolower(gsub(" ", "_", colnames(data)))

## How many rows and columns are there?
dim(data) # 67 rows & 5 columns

## What data types are in each column?
str(data) # chr, int, int, num, num

## Are there any missing values? If so, where?
colSums(is.na(data)) # no NAs in any cols

---
## 2. Summary Statistics

## What is the average September weight and April weight for the full group?
average_weight_september <- mean(data$weight..sep.) # average_weight_september = 65.0597
average_weight_april <- mean(data$weight..apr.) # average_weight_april = 66.23881

## Compute the average weight change from September to April.
# create weight change column
data$weight_change <- data$weight..apr. - data$weight..sep.
# find average
average_weight_change <- mean(data$weight_change) # average_weight_change = 1.179104

## Do males or females have a higher average weight change?
# create 2 separate datasets
dataM <- subset(data, sex == "M")
dataF <- subset(data, sex == "F")
# find average weight change in males
dataM$weight_change <- dataM$weight..apr. - dataM$weight..sep.
mean_weight_change_males <- mean(dataM$weight_change) # mean_weight_change_males = -1.15625
# find average weight change in females
dataF$weight_change <- dataF$weight..apr. - dataF$weight..sep.
mean_weight_change_females <- mean(dataF$weight_change) # mean_weight_change_females = -1.2

# other way of doing this using built-in function
aggregate(weight_change ~ sex, data = data, mean) 
# same results: weight_change (sex = F) = 1.2; weight_change (sex = M) = 1.15625 

# Conclusion = females have a higher average weight change

## What is the standard deviation of BMI in September vs April?
StdDev_September <- sd(data$bmi..sep.) # StdDev_September = 3.308901
StdDev_April <- sd(data$bmi..apr.) # StdDev_April = 3.602527

## Which student gained the most weight?
data[which.max(data$weight_change), ] # row 67, weight_change of 11

---
## 3. Data Visualization
library(ggplot2) # library for plots

## Create a histogram of April weights.
ggplot(data, aes(x = `weight..apr.`))+ geom_histogram() + 
  labs(title = "Histogram of April Weights", x = "Weight", y = "Frequency") +
  theme(plot.title = element_text(hjust = 0.5))
# ggplot = choose dataset/cols/etc
# geom_histogram = build the histogram
# labs = add title/x-axis/y-axis
# theme = center title (hjust = 0/default: left; 0.5: centered; 1: right)

## Create a boxplot comparing April BMI by sex.
ggplot(data, aes(x = sex, y = `bmi..apr.`)) + geom_boxplot() + 
  labs(title = "Boxplot of April BMI by Sex", x = "Sex", y = "BMI") + 
  theme(plot.title = element_text(hjust = 0.5))
# geom_boxplot = build the boxplot

## Make a scatterplot of September vs April weight.
ggplot(data, aes(x = `weight..sep.`, y = `weight..apr.`)) + geom_point() +
  labs(title = "Scatter Plot of Weight: September vs April",
       x = "Weight in September",y = "Weight in April") + 
  theme(plot.title = element_text(hjust = 0.5))
# geom_point = plot points

## Add a regression line to the scatterplot.
ggplot(data, aes(x = `weight..sep.`, y = `weight..apr.`)) + 
  geom_point() + geom_smooth(method = "lm") +
  labs(title = "Scatter Plot of Weight: September vs April",
       x = "Weight in September", y = "Weight in April") + 
  theme(plot.title = element_text(hjust = 0.5))
# geom_smooth = add regression line

## Plot a histogram of weight changes (April-September).
ggplot(data, aes(x = `weight_change`)) + geom_histogram() +
  labs(title = "Histogram of Weight Change", x = "Weight Change", y = "Frequency") + 
  theme(plot.title = element_text(hjust = 0.5))
# geom_histogram = build histogram

---
## 4. Statistical Testing

## Perform a paired t-test to determine if average weight changed significantly from September to April.
t.test(data$weight..sep., data$weight..apr., paired = TRUE)
# t = -2.4822, df = 66, p-value = 0.01561
# alternative hypothesis: true mean difference is not equal to 0
# 95 percent confidence interval: (-2.1275377 ; -0.2306713)
# sample estimates: mean difference = -1.179104 
# p < 0.05 = statistically significant decrease in average weight from September to April
# CI doesn't contain 0 = supports conclusion that change is not due to random chance

## Perform an independent t-test to compare weight change between males and females.
t.test(weight_change ~ sex, data)
# t = 0.044559, df = 47.303, p-value = 0.9646
# alternative hypothesis: true difference in means between group F and group M is not equal to 0
# 95 percent confidence interval: (-1.931114 ; 2.018614)
# sample estimates: mean in group F = 1.20000; mean in group M = 1.15625 
# p > 0.05 = no statistically significant difference in weight change between males and females
# CI contains 0 = supports conclusion of no significant difference

---
## 5. Linear Regression

## Build a linear regression model to predict April weight using September weight.
model <- lm(`weight..apr.` ~ `weight..sep.`, data)
summary(model)
# Residuals:
# Min       1Q   Median       3Q      Max 
# -13.7665  -1.8313   0.2823   2.0795  11.5414 
# ---
# Coefficients:
# Estimate Std. Error t value Pr(>|t|)    
# (Intercept)   5.04686    2.77894   1.816    0.074 .  
# weight..sep.  0.94055    0.04209  22.344   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# ---
# Residual standard error: 3.859 on 65 degrees of freedom
# Multiple R-squared:  0.8848,	Adjusted R-squared:  0.883 
# F-statistic: 499.2 on 1 and 65 DF,  p-value: < 2.2e-16

## What is the slope and intercept? Interpret them.
# intercept = 5.04686, for September weight = 0 (not possible), April weight = 5.04686
# ---
# slope = 0.94055, for every 1kg increase in September weight, 
# there's a 0.94kg increase in April weight = strong linear relationship

## What is the Rsquared value?
# Rsquared = 0.8848 (from summary)

## Plot the residuals and check if they seem normally distributed.
# Residual plot
plot(model$residuals, main = "Residuals Plot", ylab = "Residuals") 

# Histogram of residuals
hist(model$residuals, main = "Histogram of Residuals", xlab = "Residuals")

# Q-Q plot with x-y line
qqnorm(model$residuals)
qqline(model$residuals)

---
## 6. Key Insights
- 

---
## 7. Challenges and Solutions
- 

---
## 8. Final File
-

---
**Contact:** dashinee.parmanum@gmail.com
