library(ggplot2)
library(scales)
library(ggthemes)

setwd("~/projects/sitc/data/public/csv")
logistics<-read.csv("carpool-aggregate.csv", header=TRUE, stringsAsFactors=FALSE)

logistics$Actual<-as.numeric(logistics$Actual)
logistics$Capacity<-as.numeric(logistics$Capacity)
logistics$percentFull<-logistics$Actual/logistics$Capacity
logistics$Date<-as.Date(logistics$Date, "%m-%d")

ggplot(logistics, aes(x=Date, y=percentFull)) +
  geom_hline(yintercept=1, color="red") +
  geom_line() +
  geom_ribbon(aes(ymin=0, ymax=percentFull)) +
  facet_grid(Carpool ~ .) +
  scale_x_date(labels = date_format("%m/%d"), breaks = date_breaks("week")) +
  scale_y_continuous(labels = percent_format()) +
  theme_tufte(base_family="Helvetica", ticks=TRUE) +
  ylab("Capacity Utilization") +
  xlab("Date (day)") +
  ggtitle("Capacity Utilization by Group")