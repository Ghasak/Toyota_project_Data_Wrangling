
while (!is.null(dev.list()))  dev.off(dev.list()["RStudioGD"])
#dev.off(dev.list()["RStudioGD"]) # clean the Graph Area
rm(list=ls())                    # clean the Workspace (dataset)
cat("\014")                      # clean the console area
graphics.off()                   # close graphics windows (For R Script)


# Data1 <- read.csv(file.choose())
directory_location <- "~/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/R/0_DataSet/dataSet.csv"
#directory_location <- paste0(getwd(),'/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/R/0_DataSet/dataSet.csv')
Data1 <- read.csv(directory_location)

print(Data1)
