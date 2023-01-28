library(ggplot2)

## Set the working directory to the root of your DSC 520 directory
setwd("C:/Users/Josh/Documents/GitHub/Python-Projects/Data Presentation and Visualization/Week_7_8/")

# set the datasets.
df_birthrates <- read.csv("birth-rate.csv")
df_crimerates <- read.csv("crimerates-by-state-2005.csv")

# Set up a Scatter plot
ggplot(df_crimerates, aes(x=murder, y=burglary)) + geom_point(color="blue") +ggtitle('R Scatterplot') + geom_smooth(method="auto", se=TRUE, fullrange=FALSE, level=0.95)

# Set up a bubble chart
ggplot(df_birthrates, aes(x = df_birthrates[df_birthrates["Country"] == "United States"], y = 2000)) + 
  geom_point(aes(color = Country, size = 2000), alpha = 0.5) +
  scale_size(range = c(0.5, 12)) 

# Set up a density chart

