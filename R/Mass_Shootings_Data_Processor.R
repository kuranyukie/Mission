data = read.csv("Mass_Shootings_Dataset.csv")

summary(data)

# Check format of "Location"
library(stringr)
misformat = c()
for(i in 1:nrow(data)) {
  if(str_count(data$Location[i], ",") != 1) {
    misformat = c(misformat, data$No[i])
  }
}
misformat # show which row of Location is misformatted

# Create variable "State"
## extract state from original "Location" variable

data$State = rep(-1,nrow(data))
for(i in 1:nrow(data)) {
  if(nchar(as.character(data$Location[i])) > 0) { # exclude empty data
    state = trimws(strsplit(as.character(data$Location[i]), ",")[[1]][-1]) # split with comma and trim white space
    data$State[i] = state 
  }
  else {
    data$State[i] = "N/A"
  }
}

## Unify "State" with full names

### 1) create a list using regular expression, mapping abbreviate names with full names and the related gun control policy
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

### 2) map names
for(i in 1:nrow(data)) {
  j = data$State[i]
  if(j %in% names(mapping)) {
    data$State[i] = mapping[[j]][1]
  }
}

# Create variable "Background_Check"

data$Background_Check = rep(-1,nrow(data))
for(i in 1:nrow(data)) {
  for(j in mapping) {
    if (data$State[i] == j[1]) {
      data$Background_Check[i] = j[2]
    }
    if (data$State[i] == "N/A") {
      data$Background_Check[i] = "N/A"
    }
  }
}
table(data$Background_Check) # check modified variable