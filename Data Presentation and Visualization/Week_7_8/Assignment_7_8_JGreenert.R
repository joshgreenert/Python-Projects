library(ggplot2)

## Set the working directory to the root of your DSC 520 directory
setwd("C:/Users/Josh/Documents/GitHub/Python-Projects/Data Presentation and Visualization/Week_7_8/")

# set the datasets.
df_birthrates <- read.csv("birth-rate.csv")
df_crimerates <- read.csv("crimerates-by-state-2005.csv")

# Set up a Scatter plot
ggplot(df_crimerates, aes(x=murder, y=burglary)) + geom_point(color="blue") +ggtitle('R Scatterplot') + geom_smooth(method="auto", se=TRUE, fullrange=FALSE, level=0.95)

# Set up a bubble chart
# Set up values and years from the birth rate dataframe.
us_values <- as.numeric(df_birthrates[df_birthrates["Country"] == "United States"])
us_years <- names(df_birthrates)

# Create the dataframe.
us_birth_df = data.frame(us_years ,us_values)

ggplot(us_birth_df, aes(x = us_values, y = us_years, size = us_values))+ geom_point(alpha = 0.7) + ggtitle('R Bubble chart')

# Set up a density chart
ggplot(us_birth_df, aes(x=us_values)) + geom_density(fill="#69b3a2", color="#e9ecef", alpha=0.8) + ggtitle('R Density Plot')


