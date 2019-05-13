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
directory_location <- paste0(getwd(),'/Desktop/1_Cleaning_Toyota_Data/[4] Models and Analysis/[2] R/[3] TOYOTA_R_Analysis [New][Fri_Mar_15_2019]/Dataset/1_Toyota_Data_set_Revised.csv')

Data1 <- read.csv(directory_location)

Total       = Data1$Crash_count
Young       = Data1$Driver_Young
Middle_age  = Data1$Driver_Middle_age
Senior      = Data1$Driver_Senior
# ================================================================================
#               Data Frame converting our data [Similar to Pandas]
# ================================================================================
Data1 <- data.frame(Data1)
colnames(Data1)
names(Data1)
# colnames() work on a data.frame but names() does not work on a matrix:
Data1$Crash_count
#Data1[1] # First column in our dataset
#lf = as.list(Data1[1])
#
# for (i in 1:length(colnames(Data1))){
#   print(colnames(Data1[i]))
# }
# ================================================================================
#                        All Parameters in our Dataset
# ================================================================================
  FilterLess35                    <- Data1[,1]
  Crash_count                     <- Data1[,2]
  Driver_Young                    <- Data1[,3]
  Driver_Middle_age               <- Data1[,4]
  Driver_Senior                   <- Data1[,5]
  High.speed                      <- Data1[,6]
  General_national_road           <- Data1[,7]
  Major_prefectural_road          <- Data1[,8]
  Minor_prefectural_road          <- Data1[,9]
  Othertypes                      <- Data1[,10]
  Prefectural_Dummy_new           <- Data1[,11]
  conf1_13.0_or_more              <- Data1[,12]
  conf1_19.5_m_or_more            <- Data1[,13]
  conf1_3.5_m_or_more             <- Data1[,14]
  conf1_5.5_m_or_more             <- Data1[,15]
  conf1_9.0_m_or_more             <- Data1[,16]
  conf1_Less_than_3.5_m           <- Data1[,17]
  conf2_13.0_or_more              <- Data1[,18]
  conf2_5.5_m_or_more             <- Data1[,19]
  conf2_9.0_m_or_more             <- Data1[,20]
  conf2_Between_Less3.5_and_5.5m  <- Data1[,21]
  conf3_Narrow_road               <- Data1[,22]
  conf3_One_lane                  <- Data1[,23]
  conf3_Two_to_Three_lanes        <- Data1[,24]
  conf3_larger_than_Four_lanes    <- Data1[,25]
  Width3.0m_and_less_5.5m         <- Data1[,26]
  Width3.0m_or_less               <- Data1[,27]
  Width_13.0m_or_more             <- Data1[,28]
  Width_5.5m_and_less_13.0m       <- Data1[,29]
  conf1_30kmh_orless              <- Data1[,30]
  conf1_40kmh_orless              <- Data1[,31]
  conf1_50kmh_orless              <- Data1[,32]
  conf1_60kmh_orless              <- Data1[,33]
  conf1_No_regulation             <- Data1[,34]
  conf2_High_speed_limit          <- Data1[,35]
  conf2_Low_speed_limit           <- Data1[,36]
  conf2_Medium_speed_limit        <- Data1[,37]
  conf2_No_regulation             <- Data1[,38]
  traffic_volume                  <- Data1[,39]
  log_traffic_volume              <- Data1[,40]
  traffic_volume_dummy            <- Data1[,41]

# ================================================================================
#               Run Univariate Poisson to get start values
# ================================================================================
#  the sing << to show the variable as a global varaible so you see this inside the function
# Define the Traffic volume variable as log(Traffic volume * 100)
log_traffic_volume_2 <- ifelse(Data1$traffic_volume == 0,0,log(Data1$traffic_volume*100))
# =======================Total Crash Count=============================
require(maxLik)
require(sandwich)
require(foreign)
require(ggplot2)
require(MASS)
outcome <- "Total"
variables <-   c("Prefectural_Dummy_new"
                 , "Minor_prefectural_road"
                 , "Othertypes"
                 , "conf2_Between_Less3.5_and_5.5m"
                 , "conf2_5.5_m_or_more"
                 , "conf2_9.0_m_or_more"
                 , "conf1_30kmh_orless"
                 , "conf1_40kmh_orless"
                 , "conf1_50kmh_orless"
                 , "conf1_No_regulation"
                 , "log_traffic_volume_2"
                 , "traffic_volume_dummy")
# our modeling effort,
# fully parameterized!
Total_formula <- as.formula(
  paste(outcome, paste(variables, collapse = " + "),sep = " ~ "))
print(Total_formula)
# Performing Negative Binomial Model [For fixed theta only (dispersion)]
mtotal <- glm.nb(Total_formula, link = log)
#,init.theta = 1.032713156,link = log)
summary(mtotal)

# # Performing Poisson Model
mtotal_poisson <- glm(Total_formula,family = "poisson")
# summary(m2)
# Start_m2 <<- m2$coefficients
# ===========================Young Drivers=============================
outcome <- "Young"
# our modeling effort,
# fully parameterized!
Young_formula <- as.formula(
  paste(outcome, paste(variables, collapse = " + "),sep = " ~ "))
print(Young_formula)
# Performing Negative Binomial Model [For fixed theta only (dispersion)]
m1 <- glm.nb(Young_formula, link = log)
#,init.theta = 1.032713156,link = log)
summary(m1)
Start_m1 <<- m1$coefficients
# # Performing Poisson Model
# m2 <- glm(Total_formula,family = "poisson")
# summary(m2)
# Start_m2 <<- m2$coefficients
#summary(m1)
Start_m1 <<- m1$coefficients
# ===========================Middle_age Drivers========================
outcome <- "Middle_age"
# our modeling effort,
# fully parameterized!
Middle_age_formula <- as.formula(
  paste(outcome, paste(variables, collapse = " + "),sep = " ~ "))
print(Middle_age_formula)
# Performing Negative Binomial Model [For fixed theta only (dispersion)]
m2 <- glm.nb(Middle_age_formula, link = log)
#,init.theta = 1.032713156,link = log)
summary(m2)
Start_m2 <<- m2$coefficients
# # Performing Poisson Model
# m2 <- glm(Total_formula,family = "poisson")
# summary(m2)
# Start_m2 <<- m2$coefficients
# ===========================Senior Drivers=============================
# Only Senior Drivers will be selected as Poisson count model [dispersion is not sig. from STATA]
outcome <- "Senior"
# our modeling effort,
# fully parameterized!
Senior_formula <- as.formula(
  paste(outcome, paste(variables, collapse = " + "),sep = " ~ "))
print(Senior_formula)
# Performing Negative Binomial Model [For fixed theta only (dispersion)]
m3 <- glm(Senior_formula, family = 'poisson')
#,init.theta = 1.032713156,link = log)
summary(m3)
Start_m3 <<- m3$coefficients
# # Performing Poisson Model
# m2 <- glm(Total_formula,family = "poisson")
# summary(m2)
# Start_m2 <<- m2$coefficients
# Test for Senior plot
par(mfrow=c(2,2))
plot(m3)
Start_m1 <<- matrix(Start_m1,nrow = NROW(Start_m1),1)
Start_m2 <<- matrix(Start_m2,nrow = NROW(Start_m2),1)
Start_m3 <<- matrix(Start_m3,nrow = NROW(Start_m3),1)

Start <<- rbind(Start_m1,Start_m2,Start_m3)
# ================================================================================
#              Maximum Simulated Likelihood Function Core
# ================================================================================
LLF1 <- function(b){

lmx1 = exp(    b[1]
             + b[2] * Prefectural_Dummy_new
             + b[3] * Minor_prefectural_road
             + b[4] * Othertypes
             + b[5] * conf2_Between_Less3.5_and_5.5m
             + b[6] * conf2_5.5_m_or_more
             + b[7] * conf2_9.0_m_or_more
             + b[8] * conf1_30kmh_orless
             + b[9] * conf1_40kmh_orless
             + b[10] * conf1_50kmh_orless
             + b[11] * conf1_No_regulation
             + b[12] * log_traffic_volume_2
             + b[13] * traffic_volume_dummy)

  P1 = exp((Total)*(log(lmx1))-(lmx1)-lfactorial(Total))
  return(log(P1))
}
startx1 = replicate(13,0)
ML2 <- maxLik(LLF1, start = startx1,method = "bfgs"
              ,control=list(printLevel=4))
summary(ML2)
ML2$estimate
# Here is the power of the package sandwich to calculate the Robust standard Error.

cov.ML2 <- vcov(ML2, type="HC0")
std.err <- sqrt(diag(cov.ML2))
r.est <- cbind(Estimate= coef(ML2), "Robust SE" = std.err,
               "Pr(>|z|)" = 2 * pnorm(abs(coef(ML2)/std.err), lower.tail=FALSE),
               LL = coef(ML2) - 1.96 * std.err,
               UL = coef(ML2) + 1.96 * std.err)
print(r.est)
# Compare between Maximum Likelihood Estimation vs ml.nb by the Package
# For Total Crash count only
print(cbind("MLE Est." = mtotal_poisson$coefficients,"Package Est." = ML2$estimate))

# ================================================================================
#              Maximum Simulated Likelihood For Negative Binomial Model
# ================================================================================
LLF1 <- function(b){
y <- Senior
lmx1 = exp(    b[1]
             + b[2] * Prefectural_Dummy_new
             + b[3] * Minor_prefectural_road
             + b[4] * Othertypes
             + b[5] * conf2_Between_Less3.5_and_5.5m
             + b[6] * conf2_5.5_m_or_more
             + b[7] * conf2_9.0_m_or_more
             + b[8] * conf1_30kmh_orless
             + b[9] * conf1_40kmh_orless
             + b[10] * conf1_50kmh_orless
             + b[11] * conf1_No_regulation
             + b[12] * log_traffic_volume_2
             + b[13] * traffic_volume_dummy)
  e2 <- 1/b[14]
  P1 = exp(lgamma(y+e2)-lfactorial(y)-lgamma(e2)+y*log(lmx1)+e2*log(e2)-(y+e2)*log(lmx1+e2))
  #exp((Total)*(log(lmx1))-(lmx1)-lfactorial(Total))

  return(log(P1))
}

startx1 = replicate(14,1)
ML3 <- maxLik(LLF1, start = startx1,method = "bfgs"
              ,control=list(printLevel=4))
summary(ML3)
ML3$estimate
print(cbind("MLE NBII Est." = ML3$estimate,"Package NBII Est." = m3$coefficients))


# Its evident that Senior drivers dispersion parameter is not significant.

# print(results)
# print("Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1")
# paste("Log-likelihood at convergence = ", logLik(ML2))
# paste("AIC    = ",AICx)
# paste("BIC    = ",BICx)
# paste("CLICx  = ",CLICx)

# ================================================================================
#     Maximum Simulated Likelihood For Multivariate Indpendent Count Model
# ================================================================================
# Now this Model is the one similar to the m1, m2 and m3 above, I will use
# Negative Binomial Model for Young, Middel_Aged, and Poisson for Senior

LLF1 <- function(b){

  y1 <- Young
  y2 <- Middle_age
  y3 <- Senior
  lmx1 = exp(    b[1]
                 + b[2] * Prefectural_Dummy_new
                 + b[3] * Minor_prefectural_road
                 + b[4] * Othertypes
                 + b[5] * conf2_Between_Less3.5_and_5.5m
                 + b[6] * conf2_5.5_m_or_more
                 + b[7] * conf2_9.0_m_or_more
                 + b[8] * conf1_30kmh_orless
                 + b[9] * conf1_40kmh_orless
                 + b[10] * conf1_50kmh_orless
                 + b[11] * conf1_No_regulation
                 + b[12] * log_traffic_volume_2
                 + b[13] * traffic_volume_dummy)

    lmx2 = exp(    b[14]
                 + b[15]* Prefectural_Dummy_new
                 + b[16]* Minor_prefectural_road
                 + b[17]* Othertypes
                 + b[18]* conf2_Between_Less3.5_and_5.5m
                 + b[19]* conf2_5.5_m_or_more
                 + b[20]* conf2_9.0_m_or_more
                 + b[21]* conf1_30kmh_orless
                 + b[22]* conf1_40kmh_orless
                 + b[23] * conf1_50kmh_orless
                 + b[24] * conf1_No_regulation
                 + b[25] * log_traffic_volume_2
                 + b[26] * traffic_volume_dummy)

      lmx3 = exp(  b[27]
                 + b[28]* Prefectural_Dummy_new
                 + b[29]* Minor_prefectural_road
                 + b[30]* Othertypes
                 + b[31]* conf2_Between_Less3.5_and_5.5m
                 + b[32]* conf2_5.5_m_or_more
                 + b[33]* conf2_9.0_m_or_more
                 + b[34]* conf1_30kmh_orless
                 + b[35]* conf1_40kmh_orless
                 + b[36] * conf1_50kmh_orless
                 + b[37] * conf1_No_regulation
                 + b[38] * log_traffic_volume_2
                 + b[39] * traffic_volume_dummy)

  e1 <- 1/b[40]
  e2 <- 1/b[41]

  P1 = exp(lgamma(y1+e1)-lfactorial(y1)-lgamma(e1)+y1*log(lmx1)+e1*log(e1)-(y1+e1)*log(lmx1+e1))
  P2 = exp(lgamma(y2+e2)-lfactorial(y2)-lgamma(e2)+y2*log(lmx2)+e2*log(e2)-(y2+e2)*log(lmx2+e2))
  P3 = exp((y3)*(log(lmx3))-(lmx3)-lfactorial(y3))

  return(log(P1)+log(P2)+log(P3))
}
startx1 = c(Start,1,1)
ML4 <- maxLik(LLF1, start = startx1,method = "bfgs"
              ,control=list(printLevel=4))
summary(ML4)
ML4$estimate
print(cbind("MLE NBII Est." = ML4$estimate,"Package NBII Est." = c(Start,0,0)))

# ================================================================================
#                     Last Note on Modeling comparison
# ================================================================================
# https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Poisson.html
# dpois(x, lambda, log = FALSE)
# ppois(q, lambda, lower.tail = TRUE, log.p = FALSE)
# qpois(p, lambda, lower.tail = TRUE, log.p = FALSE)
# rpois(n, lambda)

# https://stat.ethz.ch/R-manual/R-patched/library/stats/html/NegBinomial.html
# dnbinom(x, size, prob, mu, log = FALSE)
# pnbinom(q, size, prob, mu, lower.tail = TRUE, log.p = FALSE)
# qnbinom(p, size, prob, mu, lower.tail = TRUE, log.p = FALSE)
# rnbinom(n, size, prob, mu)

# You can use in the estimation as:

LLF1 <- function(b){
y <- Total
lmx1 = exp(    b[1]
             + b[2] * Prefectural_Dummy_new
             + b[3] * Minor_prefectural_road
             + b[4] * Othertypes
             + b[5] * conf2_Between_Less3.5_and_5.5m
             + b[6] * conf2_5.5_m_or_more
             + b[7] * conf2_9.0_m_or_more
             + b[8] * conf1_30kmh_orless
             + b[9] * conf1_40kmh_orless
             + b[10] * conf1_50kmh_orless
             + b[11] * conf1_No_regulation
             + b[12] * log_traffic_volume_2
             + b[13] * traffic_volume_dummy)
  e2 <- 1/b[14]
  P1 = dnbinom(y, size=e2, mu=lmx1, log = FALSE)
  #exp((Total)*(log(lmx1))-(lmx1)-lfactorial(Total))
  return(log(P1))
}

startx1 = replicate(14,1)
ML5 <- maxLik(LLF1, start = startx1,method = "bfgs"
              ,control=list(printLevel=4))
summary(ML5)
print(cbind("MLE NBII Est." = ML5$estimate,"Package NBII Est." = c(mtotal$coefficients,0)))


