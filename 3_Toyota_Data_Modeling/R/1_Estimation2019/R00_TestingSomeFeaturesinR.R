
while (!is.null(dev.list()))  dev.off(dev.list()["RStudioGD"])
#dev.off(dev.list()["RStudioGD"]) # clean the Graph Area
rm(list=ls())                    # clean the Workspace (dataset)
cat("\014")                      # clean the console area
graphics.off()                   # close graphics windows (For R Script)



print("Hello World")

# Using this command will make your file works with an output same name, but you will store the results all
# But it wont work for estimation of any model.
print("You can use: R CMD BATCH \"--args arg1 arg2\" file.R & ")

# =========================================================================
while (!is.null(dev.list()))  dev.off(dev.list()["RStudioGD"])
#dev.off(dev.list()["RStudioGD"]) # clean the Graph Area
rm(list=ls())                    # clean the Workspace (dataset)
cat("\014")                      # clean the console area
graphics.off()                   # close graphics windows (For R Script)
# =========================================================================
#           Which Machine You are using to load the data
# =========================================================================
args<-commandArgs(TRUE)
print("==============================================")
print("Select which machine you are running your code")
print("==============================================")
Machine <- readline(prompt="Enter which machine you are using: 1: MacPro, 2: MacBookPro...?")
