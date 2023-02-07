library(ggplot2)

## Set the working directory to the root of your DSC 520 directory
setwd("C:/Users/Josh/Documents/GitHub/Python-Projects/Data Presentation and Visualization/Week_9_10/")

# set the datasets.
df_costcos <- read.csv("costcos-geocoded.csv")
df_ppg <- read.csv("ppg2008.csv")

# Create a heat map
drops <- c("Name")
df_ppg <- df_ppg[ , !(names(df_ppg) %in% drops)]

# set the data into a matrix to get the heat map to work.
data <- as.matrix(df_ppg)
heatmap(data, scale="column", main="R Heat Map")

# Create a spatial chart
df_costcos

ggplot(df_costcos, aes(Longitude, Latitude, group = State)) + 
  geom_polygon(fill = "white", colour = "grey50") + 
  coord_quickmap() + ggtitle('R Spatial Chart')

# Create a contour Chart
ggplot(df_costcos, aes(x = Longitude, y = Latitude, fill = ..level..)) +
  stat_density_2d(geom = "polygon") + ggtitle('R Contour Chart')