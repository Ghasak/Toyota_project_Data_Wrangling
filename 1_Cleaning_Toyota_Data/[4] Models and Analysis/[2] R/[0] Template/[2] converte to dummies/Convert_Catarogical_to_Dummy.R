# Here I will try to use the seperation using the dummy 

hsb2 <- read.csv("/Users/Ghasak/MEGAsync/[4] Models and Analysis/[2] R/[2] converte to dummies/test_dummy.csv")
gender <- hsb2[,1]
type   <- hsb2[,2]
male <- ifelse(gender == 'male', 1, 0)
female <- ifelse(gender == 'femal',1,0)
type1  <- ifelse(type == 1,1,0)
type2  <- ifelse(type == 2,1,0)
type3  <- ifelse(type == 3,1,0)
dataframe <- data.frame(male, female, type1,type2,type3)

# Write CSV in R
write.csv(dataframe, file = "/Users/Ghasak/MEGAsync/[4] Models and Analysis/[2] R/[2] converte to dummies/MyData.csv")



