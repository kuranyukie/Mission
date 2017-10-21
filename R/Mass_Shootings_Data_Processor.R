library(readr)

data = read_csv("Mass_Shootings_Dataset_Original.csv")
head(data)
summary(data)

# 1. Diagnosis of data problem

# 1.1 Check the format of variable names
names(data)

# 1.2 Check missing values
which(is.na(data$Location))
which(is.na(data$Date))
which(is.na(data$Summary))
which(is.na(data$`Mental Health Issues`))
which(is.na(data$Race))
which(is.na(data$Gender))
which(is.na(data$Latitude))
which(is.na(data$Longitude))

# 1.3 Check mis-formatted data

# 1.3.1 Check the class of "Date"
class(data$Date)

# 1.3.2 Check all data in "Location" and point out mis-formatted rows
library(stringr)
class(data$Location)
misformat = c()
for(i in 1:nrow(data)) {
  if(is.na(data$Location[i])) { # missing values
    misformat = c(misformat, data$No[i])
  }
  else {
    if(str_count(data$Location[i], ",") != 1) { # mis-formatted values
      misformat = c(misformat, data$No[i])
    }
  }
}
misformat # show which rows of Location are mis-formatted
length(misformat) # count how many rows are mis-formatted

# 1.4 Check levels of categorical variables

# Pick levels of categorical variables
unique(data$`Mental Health Issues`)
unique(data$Race)
unique(data$Gender)

# ======== Diagnosis Complete ======== 

# 2. Treat Data Problems

# Due to inconvenience of modifying 50 rows of "Location" in R, we just import a modified csv
data = read_csv("Mass_Shootings_Dataset_Modified.csv")

# 2.1 Unify names
names(data) # before
colnames(data)[8] = "Total Victims"
names(data) # after

# 2.2 Add missing values - locate them and fix them

which(is.na(data$Summary)) # before
data$Summary[1] = "A 64-year-old white man armed with 10 rifles rained down gunfire on Las Vegas country music festival, more than 500 people injured"
which(is.na(data$Summary)) # after

# 2.3 Treat mis-formatted data

# 2.3.1 Check variable "Location" (modified in csv)
misformat_loc = c()
missing_loc = c()
for(i in 1:nrow(data)) {
  if(is.na(data$Location[i])) { # missing values
    missing_loc = c(missing_loc, data$No[i])
  }
  else {
    if(str_count(data$Location[i], ",") != 1) { # mis-formatted values
      misformat_loc = c(misformat_loc, data$No[i])
    }
  }
}
# There are only 6 missing values that we can't find any data to fill in, so we should get "0" and "6" as the following output
length(misformat_loc) # count how many rows are mis-formatted
length(missing_loc)   # count how many missing values


# 2.3.2 Change the format of variable "Date"
class(data$Date) # before
data$Date = as.Date(data$Date,"%m/%d/%Y")
class(data$Date) # after


# 2.4 Unify levels - Modify multiple levels meaning the same thing

# Gender
unique(data$Gender) # before
data$Gender[which(data$Gender=="M")]="Male"
data$Gender[which(data$Gender=="M/F")]="Unknown"
data$Gender[which(data$Gender=="Male/Female")]="Unknown"
unique(data$Gender) #after

# Mental Health Issue
unique(data$`Mental Health Issues`) # before
data$`Mental Health Issues`[which(data$`Mental Health Issues`=="Unclear")]="Unknown"
data$`Mental Health Issues`[which(data$`Mental Health Issues`=="unknown")]="Unknown"
unique(data$`Mental Health Issues`) #after

# Race
unique(data$Race) # before
data$Race[which(data$Race=="Black American or African American")]="Black"
data$Race[which(data$Race=="White American or European American")]="White"
data$Race[which(data$Race=="Asian American")]="Asian"
data$Race[which(data$Race=="Some other race")]="Other"
data$Race[which(data$Race=="Two or more races")]="Other"
data$Race[which(data$Race=="Black American or African American/Unknown")]="Black"
data$Race[which(data$Race=="White American or European American/Some other Race")]="White"
data$Race[which(data$Race=="Native American or Alaska Native")]="Latino"
data$Race[which(data$Race=="white")]="White"
data$Race[which(data$Race=="black")]="Black"  
data$Race[which(data$Race=="Asian American/Some other race")]="Asian"  
data$Race[which(is.na(data$Race))]="Unknown"
unique(data$Race) # after

# 2.5 Add new variables
# 2.5.1 New variable: State - extract from location

## Extract state from original "Location" variable
data$State = rep(-1,nrow(data)) # initialize a new variable
for(i in 1:nrow(data)) {
  if(!is.na(data$Location[i])) { # exclude empty data
    state = trimws(strsplit(as.character(data$Location[i]), ",")[[1]][-1]) # split with comma and trim white space
    data$State[i] = state 
  }
  else {
    data$State[i] = "N/A"
  }
}

## Unify "State" with full names
### create a list using regular expression, mapping abbreviate names with full names and the related gun control policy
mapping = list(
  "AL" = c("Alabama", "0"),
  "AK" = c("Alaska", "0"),
  "AZ" = c("Arizona", "0"),
  "AR" = c("Arkansas", "0"),
  "CA" = c("California", "1"),
  "CO" = c("Colorado", "1"),
  "CT" = c("Connecticut", "1"),
  "DE" = c("Delaware", "1"),
  "DC" = c("District of Columbia", "1"),
  "FL" = c("Florida", "0"),
  "GA" = c("Georgia", "0"),
  "HI" = c("Hawaii", "1"),
  "ID" = c("Idaho", "0"),
  "IL" = c("Illinois", "1"),
  "IN" = c("Indiana", "0"),
  "IA" = c("Iowa", "1"),
  "KS" = c("Kansas", "0"),
  "KY" = c("Kentucky", "0"),
  "LA" = c("Louisiana", "0"),
  "ME" = c("Maine", "0"),
  "MD" = c("Maryland", "1"),
  "MA" = c("Massachusetts", "1"),
  "MI" = c("Michigan", "1"),
  "MN" = c("Minnesota", "0"),
  "MS" = c("Mississippi", "0"),
  "MO" = c("Missouri", "0"),
  "MT" = c("Montana", "0"),
  "NE" = c("Nebraska", "1"),
  "NV" = c("Nevada", "0"),
  "NH" = c("New Hampshire", "0"),
  "NJ" = c("New Jersey", "1"),
  "NM" = c("New Mexico", "0"),
  "NY" = c("New York", "1"),
  "NC" = c("North Carolina", "1"),
  "ND" = c("North Dakota", "0"),
  "OH" = c("Ohio", "0"),
  "OK" = c("Oklahoma", "0"),
  "OR" = c("Oregon", "1"),
  "PA" = c("Pennsylvania", "1"),
  "RI" = c("Rhode Island", "1"),
  "SC" = c("South Carolina", "0"),
  "SD" = c("South Dakota", "0"),
  "TN" = c("Tennessee", "0"),
  "TX" = c("Texas", "0"),
  "UT" = c("Utah", "0"),
  "VT" = c("Vermont", "0"),
  "VA" = c("Virginia", "0"),
  "WA" = c("Washington", "1"),
  "WV" = c("West Virginia", "0"),
  "WI" = c("Wisconsin", "1"),
  "WY" = c("Wyoming", "0")
)

### map names
unique(data$State) # before
for(i in 1:nrow(data)) {
  j = data$State[i]
  if(j %in% names(mapping)) {
    data$State[i] = mapping[[j]][1]
  }
}
unique(data$State) # after

# 2.5.2 New variable: Background Check

data$`Background Check` = rep(-1,nrow(data)) # initialize a new variable
for(i in 1:nrow(data)) {
  for(j in mapping) {
    if (data$State[i] == j[1]) {
      data$`Background Check`[i] = j[2]
    }
    if (data$State[i] == "N/A") {
      data$`Background Check`[i] = "N/A"
    }
  }
}
table(data$`Background Check`) # check modified variable
