library(readxl)
library(ggplot2)

## Set the working directory to the root of your DSC 520 directory
setwd("C:/Users/Josh/Documents/GitHub/Python-Projects/Data Presentation and Visualization/Week_3_4/")

## Set the data.
df_population <- read_excel("world-population.xlsm")

# Create a line chart.
ggplot(data=df_population, aes(x=Population, y=Year, group=1)) +
  geom_line(color="red")+
  geom_point() + ggtitle("R Line Chart")

# Create a step chart.
ggplot(df_population, aes(x = Population, y = Year)) + 
  geom_step() + ggtitle("R Step Chart")