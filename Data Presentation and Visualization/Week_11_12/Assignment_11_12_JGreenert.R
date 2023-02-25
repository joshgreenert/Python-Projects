library(ggplot2)
library(tidyverse)
library(waterfalls)

## Set the working directory to the root of your DSC 520 directory
setwd("C:/Users/Josh/Documents/GitHub/Python-Projects/Data Presentation and Visualization/Week_11_12/")

# set the datasets.
df_education <- read.csv("education.csv")
df_birth <- read.csv("birth-rate.csv")

# Create a histogram
hist(df_education$reading, main="R Histogram",xlab="scores",col="darkmagenta")

# Create a box plot
ggplot(df_education, aes(x=reading, y=state)) + geom_boxplot() + ggtitle('R Box Plot')

# Create a bullet chart
# create the data frame with counts for each state
tibble(
  name = "R Bullet Chart",
  quant_value = 550,
  qualitative = 600
)
df_education %>% 
  ggplot(aes(x = reading, y =  state)) +
  geom_col(width = 0.5, aes(x = 625), fill = "grey") +
  geom_col(width = 0.25,aes(x = reading), fill = "green") +
  geom_col(aes(x = writing),fill = "black",color = NA,width = 0.25) +
  theme_minimal() +
  labs(title = "R Bullet Chart")

# Create another new chart (waterfall)
# filter the data to only include United States
df_birth_us <- filter(df_birth, Country == "United States")

# reshape the data from wide to long format
df_birth_us_long <- pivot_longer(df_birth_us, cols = -Country, names_to = "Year", values_to = "Value")

# Correct the years
df_birth_short <- data.frame(x = df_birth_us_long$Year, y = df_birth_us_long$Value)
df_bottom <- df_birth_short[(nrow(df_birth_short)/2 + 1):nrow(df_birth_short), ]

# create the waterfall chart
waterfall(df_bottom) + labs(title = "R Waterfall Chart")



