setwd("C:/Users/Student/Desktop/Dropbox/Debt Paper/Data")
library(ggplot2)
library(dplyr)
library(ggpubr)
data1.data<-read.csv(file="Fig12.csv")
ggplot(data1.data, aes(x=g.i, y=d, size=Debt.Stock, color=State)) +
  geom_point(alpha=0.5) +
  scale_size(range = c(.1, 24))



                          
