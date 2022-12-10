library(readxl)
library(ggplot2)

## Set the working directory to the root of your DSC 520 directory
setwd("C:/Users/Josh/Documents/GitHub/Python-Projects/Data Presentation and Visualization/Week_1/")

## Set the data.
df_obama <- read_excel("obama-approval-ratings.xls")

# Create the bar chart
ggplot(df_obama, aes(Approve)) + geom_bar() + ggtitle("R Bar Chart - Approval Ratings")

# Create a stacked bar chart.
ggplot(df_obama, aes(fill=Approve, y=Disapprove, x=None)) + geom_bar(position="stack", stat="identity") +
  ggtitle("R Stacked Bar Chart - Approval Ratings")

# Create a pie chart.
piechart_df <- df_obama[ which( df_obama$Issue == "Race Relations"), ]
piechart_df <- piechart_df[, !names(piechart_df) %in% ("Issue")]

group_names = c("Approve", "Disapprove", "None")
group_values = c(piechart_df[[1, 1]], piechart_df[[1, 2]], piechart_df[[1, 3]])

newPiechart_df <-data.frame(group_names, group_values)

ggplot(newPiechart_df, aes(x="", y=group_values, fill=group_names)) + geom_bar(stat="identity", width=1) +
  coord_polar("y", start=0) + ggtitle("R Pie Chart - Race Relations Ratings")

# Create a donut chart.
newPiechart_df$fraction = newPiechart_df$group_values / sum(newPiechart_df$group_values)

# Compute the sum of cumulative percentages to find the top and bottom.
newPiechart_df$ymax = cumsum(newPiechart_df$fraction)
newPiechart_df$ymin = c(0, head(newPiechart_df$ymax, n=-1))

# Make the plot.
ggplot(newPiechart_df, aes(ymax=ymax, ymin=ymin, xmax=4, xmin=3, fill=group_names)) +
  geom_rect() + coord_polar(theta="y") +  xlim(c(2, 4)) + ggtitle("R Donut Chart - Race Relations Ratings")







