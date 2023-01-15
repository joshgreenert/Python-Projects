library(ggplot2)
library(treemap)
library(hrbrthemes)

## Set the working directory to the root of your DSC 520 directory
setwd("C:/Users/Josh/Documents/GitHub/Python-Projects/Data Presentation and Visualization/Week_5_6/")

# set the datasets.
df_expenditures <- read.csv("expenditures.txt", sep="\t")
df_unemployment <- read.csv("unemployement-rate-1948-2010.csv")

# Set up a Tree map chart.
treemap(df_expenditures, index="category", vSize="expenditure", type="index", title="R Tree Map")

# Set up the variables for the next chart.
df_unemployment[['Year']] = as.Date(ISOdate(df_unemployment[['Year']], 1, 1), format = "%Y")

# Remove the two bottom rows since they are just the first and second month only.
df_unemployment <- head(df_unemployment, -2)

# Loop over the data.frame to get the unique years and median of each year
yearly_averages <- c()
vector_index <- 0

for(index in 1:nrow(df_unemployment)){

  if(df_unemployment[["Period"]][index] == "M01"){
    if(index <= 0){
      total <- 0
      total <- total + df_unemployment[["Value"]][index]
    }
    else{
      # Get the average for every year.
      total <- total / 12
      yearly_averages[vector_index] <-  total
      
      # Increment the vector index for added value
      vector_index <- vector_index + 1
      
      total <- 0
      total <- total + df_unemployment[["Value"]][index]
    }
  }
  else if(df_unemployment[["Period"]][index] != "M12"){
    total <- total + df_unemployment[["Value"]][index]
  }
}

# Add the new values to the new dataframe along with the years.
new_years <- unique(df_unemployment["Year"])
new_years <- head(new_years, -1)
new_df_unemployment = data.frame(new_years ,yearly_averages)

# Set up an area chart
ggplot(new_df_unemployment, aes(x=yearly_averages, y=Year)) +
  geom_area( fill="#69b3a2") +
  ggtitle("R Area Chart")

# Set up a Stacked area chart




