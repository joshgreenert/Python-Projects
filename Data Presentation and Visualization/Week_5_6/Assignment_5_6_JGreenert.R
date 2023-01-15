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

# Set up an area chart
ggplot(df_unemployment, aes(x="Year", y="Value")) +
  geom_area( fill="#69b3a2", alpha=0.4) +
  geom_line(color="#69b3a2", size=2) +
  geom_point(size=3, color="#69b3a2") +
  theme_ipsum() +
  ggtitle("R Area Chart")

# Set up a Stacked area chart
