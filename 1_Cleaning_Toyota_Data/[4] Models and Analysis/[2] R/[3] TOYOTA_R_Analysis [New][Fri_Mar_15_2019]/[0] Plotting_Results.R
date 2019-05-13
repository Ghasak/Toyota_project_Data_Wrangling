#  Title :           Traffic Accident Analysis                              #
#  Project Name:     Toyota City carsh data                                             #
#  Starting Data:    2018/April/02                                          #
#  File Name:        [1] Multivariate Truncated Poisson [First Trail]       #
#  Version:          V.01                                                   #
#  Last changed:     2018/July/25 17:56:05                                  #
#  Purpose:          Analysis different driver age groups                       #
#  Author:           Ghasak Ibrahim                                         #
#  Copyright:        (C) 2018-~                                             #
#  Product:                                                                 #
#  Please see the     note.txt file for more information on this model      #
#  All other righ    ts reserved.                                           #
#   Multivaraite     Truncated Poisson Model Using Copula and CML               #
#   parameterizin    g e expected number of crashes function only,          #
#   Homoscedastic     model                                                                     #

# ================================================================================
#               Cleaning the background of intialize Space
# ================================================================================
dev.off(dev.list()["RStudioGD"]) # clean the Graph Area
rm(list=ls())                    # clean the Workspace (dataset)
cat("\014")                      # clean the console area
graphics.off()                   # close graphics windows (For R Script)
# ================================================================================
#               Input Data and intialize the parameters vector
# ================================================================================
# Directory of the current project data on MacPro

# Data1 <- read.csv(file.choose())
Data1 <- read.csv("/Users/ghasak/Desktop/1_Cleaning_Toyota_Data/[4] Models and Analysis/[2] R/[3] TOYOTA_R_Analysis [New][Fri_Mar_15_2019]/Dataset/1_Toyota_Data_set_Revised.csv")

Total       = Data1$Crash_count
Young       = Data1$Driver_Young
Middle_age  = Data1$Driver_Middle_age
Senior      = Data1$Driver_Senior


# ================================================================================
#               Plotting the Distribution of crash counts
# ================================================================================
require(foreign)
require(ggplot2)
require(MASS)
library(ggplot2)
barfill <- "#4271AE"
barlines <- "#1F3552"
par(mfrow=c(2,2))
h1 <- hist(Total,breaks =20)
h2 <- hist(Young,breaks =20 )
h3 <- hist(Middle_age,breaks =20)
h4 <- hist(Senior,breaks = 20)

h1$counts=h1$counts/sum(h1$counts)
h2$counts=h2$counts/sum(h2$counts)
h3$counts=h3$counts/sum(h3$counts)
h4$counts=h4$counts/sum(h4$counts)
plot(h1,border="black", col="lightblue", freq = TRUE, density = NULL,plot=FALSE,
     xlim = c(0,max(Total)),
     ylim = c(0,max(h1$count))
     ,cex.lab=1.2, cex.axis=1.2, cex.main=1.2, cex.sub=1.2
     ,main="Histogram for Distance Traveled in m"
     ,xlab="Distance (m)"
     ,ylab="Probability"
     ,xaxs="i", yaxs="i" # meaning that 4% of the axis value is left on each side. To set this to 0: xaxs="i". See the xaxs section in ?par for more information.
     ,lwd = 2
     ,axes = FALSE
     ,ann=FALSE, xaxt="n", yaxt="n") # axes line width)#(max(h$counts)+max(h$counts)/1))
abline(v=seq(0, 50, 5), col="gray48",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
abline(v=seq(0, 50, 5), col="darkgray",lty = 4,lwd = 1.2) # To add horizantl line simply add h=0.001,
# abline(h=seq(0,(0.2),0.01), col="darkgray",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
# abline(h=c(0.05,0.1,0.15,0.2), col="gray48",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
# box(lty = 5, col = 'black',font = 10, font.lab = 7, font.axis = 20
#     ,cex.lab=1.2, cex.axis=1.2, cex.main=1.2, cex.sub=1.2
#     ,lwd = 3)
# generate the plot again to come to the front
plot(h1,add=TRUE,col="lightblue",axes = FALSE,ann=FALSE, xaxt="n", yaxt="n"
     )
bins =c( 0,  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
axis(1, at=bins, tick = TRUE, padj= -0.8,cex.axis = 1.2)  #h$breaks  #
axis(2,labels = TRUE, tick = TRUE, padj= -0.1,cex.axis = 1.2)  #h$breaks



plot(h2,border="black", col="lightblue", freq = TRUE, density = NULL,
     xlim = c(0,max(Young)),
     ylim = c(0,max(h2$count))
     ,cex.lab=1.2, cex.axis=1.2, cex.main=1.2, cex.sub=1.2
     ,main="Histogram for Distance Traveled in m"
     ,xlab="Distance (m)"
     ,ylab="Probability"
     ,xaxs="i", yaxs="i" # meaning that 4% of the axis value is left on each side. To set this to 0: xaxs="i". See the xaxs section in ?par for more information.
     ,lwd = 2
     ,axes = FALSE
     ,ann=FALSE, xaxt="n", yaxt="n") # axes line width)#(max(h$counts)+max(h$counts)/1))

plot(h3,border="black", col="lightblue", freq = TRUE, density = NULL,
     xlim = c(0,max(Middle_age)),
     ylim = c(0,max(h3$count))
     ,cex.lab=1.2, cex.axis=1.2, cex.main=1.2, cex.sub=1.2
     ,main="Histogram for Distance Traveled in m"
     ,xlab="Distance (m)"
     ,ylab="Probability"
     ,xaxs="i", yaxs="i" # meaning that 4% of the axis value is left on each side. To set this to 0: xaxs="i". See the xaxs section in ?par for more information.
     ,lwd = 2
     ,axes = FALSE
     ,ann=FALSE, xaxt="n", yaxt="n") # axes line width)#(max(h$counts)+max(h$counts)/1))

plot(h4,border="black", col="lightblue", freq = TRUE, density = NULL,
     xlim = c(0,max(Senior)),
     ylim = c(0,max(h4$count))
     ,cex.lab=1.2, cex.axis=1.2, cex.main=1.2, cex.sub=1.2
     ,main="Histogram for Distance Traveled in m"
     ,xlab="Distance (m)"
     ,ylab="Probability"
     ,xaxs="i", yaxs="i" # meaning that 4% of the axis value is left on each side. To set this to 0: xaxs="i". See the xaxs section in ?par for more information.
     ,lwd = 2
     ,axes = FALSE
     ,ann=FALSE, xaxt="n", yaxt="n") # axes line width)#(max(h$counts)+max(h$counts)/1))



# Multiple plot function
#
# ggplot objects can be passed in ..., or to plotlist (as a list of ggplot objects)
# - cols:   Number of columns in layout
# - layout: A matrix specifying the layout. If present, 'cols' is ignored.
#
# If the layout is something like matrix(c(1,2,3,3), nrow=2, byrow=TRUE),
# then plot 1 will go in the upper left, 2 will go in the upper right, and
# 3 will go all the way across the bottom.
#
# multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
#   library(grid)
#
#   # Make a list from the ... arguments and plotlist
#   plots <- c(list(...), plotlist)
#
#   numPlots = length(plots)
#
#   # If layout is NULL, then use 'cols' to determine layout
#   if (is.null(layout)) {
#     # Make the panel
#     # ncol: Number of columns of plots
#     # nrow: Number of rows needed, calculated from # of cols
#     layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
#                      ncol = cols, nrow = ceiling(numPlots/cols))
#   }
#
#   if (numPlots==1) {
#     print(plots[[1]])
#
#   } else {
#     # Set up the page
#     grid.newpage()
#     pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
#
#     # Make each plot, in the correct location
#     for (i in 1:numPlots) {
#       # Get the i,j matrix positions of the regions that contain this subplot
#       matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
#
#       print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
#                                       layout.pos.col = matchidx$col))
#     }
#   }
# }
# bins = seq(1,50,1)
#
# p1 <- ggplot(data = Data1, aes(x=Total))+geom_histogram(binwidth = 5,
#                                                             fill = barfill,
#                                                             color=barlines,
#                                                             center = 5)+
#                                         scale_x_continuous(breaks=seq(0,50, by = 1))
# p2 <- ggplot(data = Data1, aes(x=Young))+geom_histogram(binwidth = 5,
#                                                             fill = barfill,
#                                                             color=barlines,
#                                                             center = 1)+
#                                         scale_x_continuous(breaks=seq(0,50, by = 1))
# p3 <- ggplot(data = Data1, aes(x=Middle_age))+geom_histogram(binwidth = 5,
#                                                             fill = barfill,
#                                                             color=barlines,
#                                                             center = 1)+
#                                         scale_x_continuous(breaks=seq(0,50, by = 1))
# p4 <- ggplot(data = Data1, aes(x=Senior))+geom_histogram(binwidth = 5,
#                                                             fill = barfill,
#                                                             color=barlines,
#                                                             center = 1)+
#                                         scale_x_continuous(breaks=seq(0,50, by = 1))
# multiplot(p1, p2, p3, p4, cols=2)








