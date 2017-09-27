#You are provided with a file "BMIclass.csv" which contains data on
#age, weight, height, body mass index (BMI), and BMI classification (Class).
#You will be asked to load the dataset into R from this file, perform
#some data cleaning, and develop some basic diagnostics on this dataset. 

#BEGIN--------------------------------------------------------------#

#Section I: Reading and Loading data from .csv files

#Q1.
#Read the file "bmiclass.csv" 
#Load the contents in an dataset called "bmiclass"
library(readr)
library(dplyr)
library(ggplot2)
library(car)

bmiclass = read.csv(file = "BMIclass.csv")

#Q2. View the contents of bmiclass and examine the structure
head(bmiclass, 10)

#Q3. Summarize the dataset bmiclass
summary(bmiclass)

#-----------------------------------------------------------------#

#SECTION II:Data Cleaning


#Q4. Identify data entry inconsistencies/errors in the variable "Class".
#for example, some entries maybe in upper case and some in lower case.
unique(bmiclass$Class)

#Q5. Clean the data entry errors to ensure consistency of text, 
#i.e. all either upper case or all lower case
bmiclass$Class[which(bmiclass$Class == "NORMAL")] = "normal"
bmiclass$Class = factor(bmiclass$Class)
unique(bmiclass$Class)

#Dealing with Missing values

#Q6. Identify location of missing values i.e. list the rows containing missing values
which(is.na(bmiclass$BMI))

#Q7. Compute the mean of BMI while retaining missing values
mean(bmiclass$BMI, na.rm = TRUE)

#Q8. Impute by replacing all the missing values with a value = 21
bmiclass$BMI[is.na(bmiclass$BMI)] = 21

#------------------------------------------------------------------#

#SECTION III: Data Visualization

#Q9. Graph a scatterplot between the variables of bmiclass
pairs(bmiclass)

#Q10. Identifying any outliers in the dataset bmiclass
Boxplot(bmiclass)

#Q11. Create a bargraph of average BMI by Class
barplot(by(bmiclass$BMI, bmiclass$Class, mean), 
        xlab = "Class Classification", ylab = "Average BMI")

#Q12. Create a scatterplot of age and BMI, differentiated by Class
#Provide an interpretation of your output.
scatterplot = qplot(data = bmiclass, x = age, y = BMI, 
                    col = Class, xlab = "age", ylab = "BMI", 
                    main = "Scatter plot of age and BMI")
scatterplot
scatterplot_2 = qplot(data = bmiclass, x = age, y = BMI, 
                    col = Class, xlab = "age", ylab = "BMI", ylim = c(10,60),
                    main = "Scatter plot without outliers")
scatterplot_2

#Q13. Add a smoothing line to the scatterplot created in Q12.
scatterplot + geom_point() + geom_smooth()

#Q14. Create a histogram of BMI, differentiated by Class.
#Provide an interpretation of your output.
ggplot(bmiclass, aes(x=BMI)) + geom_histogram() + xlim(0,60) + facet_grid(~Class)

#Q15. Create a boxplots of BMI by Class.
#Provide an interpretation of your output.
#Boxplot with Outliers
ggplot(bmiclass, aes(x=Class, y=BMI)) + geom_boxplot(outlier.color = "red")
#Boxplot without Outliers
ggplot(bmiclass, aes(x=Class, y=BMI)) + geom_boxplot(outlier.color = "red") + ylim(10,50)

#END----------------------------------------------------------------#
