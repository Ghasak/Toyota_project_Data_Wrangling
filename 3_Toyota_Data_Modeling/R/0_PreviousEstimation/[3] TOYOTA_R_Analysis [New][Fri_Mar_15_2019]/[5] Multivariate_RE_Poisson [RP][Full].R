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
# Data1 <- data.frame(Data1)
# colnames(Data1)
# names(Data1)
# # colnames() work on a data.frame but names() does not work on a matrix:
# Data1$Crash_count
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
#               Halton Sequence in R-Using the package randtoolbox
# ================================================================================
library(randtoolbox)
dim1 = 39  # How many chains you want to draw
# You can get Normal distribution if you make normal =TRUE
n = 130
ux= halton(n, dim = dim1, init = TRUE, normal = TRUE, usetime = FALSE)
# sobol(n, dim = 1, init = TRUE, scrambling = 0, seed = 4711, normal = FALSE)
# torus(n, dim = 1, prime, init = TRUE, mixed = FALSE, usetime = FALSE,normal=FALSE)

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
#     Maximum Simulated Likelihood For Multivariate Indpendent Count Model
# ================================================================================
# Now this Model is the one similar to the m1, m2 and m3 above, I will use
# Negative Binomial Model for Young, Middel_Aged, and Poisson for Senior

LLF2 <- function(b){

  y1 <- Young
  y2 <- Middle_age
  y3 <- Senior
  #========= Define the Varibles for the MSL=================
  lmx1      <<- matrix(0,NROW(ux),1)
  lmx2      <<- matrix(0,NROW(ux),1)
  lmx3      <<- matrix(0,NROW(ux),1)
  SPrz1     <<- matrix(0,NROW(ux),1)
  SPrz2     <<- matrix(0,NROW(ux),1)
  SPrz3     <<- matrix(0,NROW(ux),1)
  P1        <<- matrix(0,NROW(ux),1)
  P2        <<- matrix(0,NROW(ux),1)
  P3        <<- matrix(0,NROW(ux),1)
  LLT       <<- matrix(0,NROW(Data1),1)   # Probabilit variable for each indivdiual q

    beta1  <-  b[1]
    beta2  <-  b[2]
    beta3  <-  b[3]
    beta4  <-  b[4]
    beta5  <-  b[5]
    beta6  <-  b[6]
    beta7  <-  b[7]
    beta8  <-  b[8]
    beta9  <-  b[9]
    beta10 <- b[10]
    beta11 <- b[11]
    beta12 <- b[12]
    beta13 <- b[13]

    beta14 <- b[14]
    beta15 <- b[15]
    beta16 <- b[16]
    beta17 <- b[17]
    beta18 <- b[18]
    beta19 <- b[19]
    beta20 <- b[20]
    beta21 <- b[21]
    beta22 <- b[22]
    beta23 <- b[23]
    beta24 <- b[24]
    beta25 <- b[25]
    beta26 <- b[26]

    beta27 <- b[27]
    beta28 <- b[28]
    beta29 <- b[29]
    beta30 <- b[30]
    beta31 <- b[31]
    beta32 <- b[32]
    beta33 <- b[33]
    beta34 <- b[34]
    beta35 <- b[35]
    beta36 <- b[36]
    beta37 <- b[37]
    beta38 <- b[38]
    beta39 <- b[39]


    f1 <- exp(b[40])
    f2 <- exp(b[41])
    f3 <- exp(b[42])
    f4 <- exp(b[43])
    f5 <- exp(b[44])
    f6 <- exp(b[45])

    # theta1 <- b[46]
    # theta2 <- b[47]

    sigma1  <- b[46]
    sigma2  <- b[47]
    sigma3  <- b[48]
    sigma4  <- b[49]
    sigma5  <- b[50]
    sigma6  <- b[51]
    sigma7  <- b[52]
    sigma8  <- b[53]
    sigma9  <- b[54]
    sigma10 <- b[55]
    sigma11 <- b[56]
    sigma12 <- b[57]
    sigma13 <- b[58]
    sigma14 <- b[59]
    sigma15 <- b[60]
    sigma16 <- b[61]
    sigma17 <- b[62]
    sigma18 <- b[63]
    sigma19 <- b[64]
    sigma20 <- b[65]
    sigma21 <- b[66]
    sigma22 <- b[67]
    sigma23 <- b[68]
    sigma24 <- b[69]
    sigma25 <- b[70]
    sigma26 <- b[71]
    sigma27 <- b[72]
    sigma28 <- b[73]
    sigma29 <- b[74]
    sigma30 <- b[75]
    sigma31 <- b[76]
    sigma32 <- b[77]
    sigma33 <- b[78]
    sigma34 <- b[79]
    sigma35 <- b[80]
    sigma36 <- b[81]

for (q in 1:NROW(Data1)) {
    Sumx <<- matrix(0,NROW(ux),1)
      for (r in 1:NROW(ux)){
          lmx1[r] = exp(    beta1
                         + (beta2 + sigma1  * ux[r,4]) * Prefectural_Dummy_new[q]
                         + (beta3 + sigma2  * ux[r,5]) * Minor_prefectural_road[q]
                         + (beta4 + sigma3  * ux[r,6]) * Othertypes[q]
                         + (beta5 + sigma4  * ux[r,7]) * conf2_Between_Less3.5_and_5.5m[q]
                         + (beta6 + sigma5  * ux[r,8]) * conf2_5.5_m_or_more[q]
                         + (beta7 + sigma6  * ux[r,9]) * conf2_9.0_m_or_more[q]
                         + (beta8 + sigma7  * ux[r,10])* conf1_30kmh_orless[q]
                         + (beta9 + sigma8  * ux[r,11])* conf1_40kmh_orless[q]
                         + (beta10+ sigma9  * ux[r,12])* conf1_50kmh_orless[q]
                         + (beta11+ sigma10 * ux[r,13])* conf1_No_regulation[q]
                         + (beta12+ sigma11 * ux[r,14])* log_traffic_volume_2[q]
                         + (beta13+ sigma12 * ux[r,15])* traffic_volume_dummy[q]
                         + f1 * ux[r,1])

          lmx2[r] = exp(   beta14
                         + (beta15+ sigma13 * ux[r,16])* Prefectural_Dummy_new[q]
                         + (beta16+ sigma14 * ux[r,17])* Minor_prefectural_road[q]
                         + (beta17+ sigma15 * ux[r,18])* Othertypes[q]
                         + (beta18+ sigma16 * ux[r,19])* conf2_Between_Less3.5_and_5.5m[q]
                         + (beta19+ sigma17 * ux[r,20])* conf2_5.5_m_or_more[q]
                         + (beta20+ sigma18 * ux[r,21])* conf2_9.0_m_or_more[q]
                         + (beta21+ sigma19 * ux[r,22])* conf1_30kmh_orless[q]
                         + (beta22+ sigma20 * ux[r,23])* conf1_40kmh_orless[q]
                         + (beta23+ sigma21 * ux[r,24])* conf1_50kmh_orless[q]
                         + (beta24+ sigma22 * ux[r,25])* conf1_No_regulation[q]
                         + (beta25+ sigma23 * ux[r,26])* log_traffic_volume_2[q]
                         + (beta26+ sigma24 * ux[r,27])* traffic_volume_dummy[q]
                         + f2 * ux[r,1]
                         + f3 * ux[r,2])

          lmx3[r] = exp(   beta27
                         + (beta28+ sigma25 * ux[r,28])* Prefectural_Dummy_new[q]
                         + (beta29+ sigma26 * ux[r,29])* Minor_prefectural_road[q]
                         + (beta30+ sigma27 * ux[r,30])* Othertypes[q]
                         + (beta31+ sigma28 * ux[r,31])* conf2_Between_Less3.5_and_5.5m[q]
                         + (beta32+ sigma29 * ux[r,32])* conf2_5.5_m_or_more[q]
                         + (beta33+ sigma30 * ux[r,33])* conf2_9.0_m_or_more[q]
                         + (beta34+ sigma31 * ux[r,34])* conf1_30kmh_orless[q]
                         + (beta35+ sigma32 * ux[r,35])* conf1_40kmh_orless[q]
                         + (beta36+ sigma33 * ux[r,36])* conf1_50kmh_orless[q]
                         + (beta37+ sigma34 * ux[r,37])* conf1_No_regulation[q]
                         + (beta38+ sigma35 * ux[r,38])* log_traffic_volume_2[q]
                         + (beta39+ sigma36 * ux[r,39])* traffic_volume_dummy[q]
                         + f4 * ux[r,1]
                         + f5 * ux[r,2]
                         + f6 * ux[r,3])

        # == Calculate the probability ========

      P1[r] = exp((y1[q])*(log(lmx1[r]))-(lmx1[r])-lfactorial(y1[q]))
      P2[r] = exp((y2[q])*(log(lmx2[r]))-(lmx2[r])-lfactorial(y2[q]))
      P3[r] = exp((y3[q])*(log(lmx3[r]))-(lmx3[r])-lfactorial(y3[q]))

      # ========== Probability of Zero ======
      SPrz1[r] = exp(-lmx1[r])
      SPrz2[r] = exp(-lmx2[r])
      SPrz3[r] = exp(-lmx3[r])
      # ========== Probability of Zero
      # === It seems that R cant assign matrix to a constant value so you have to
      # === Define the sum as a vector
      # === Define the Truncated Probability Function
      Sumx[r] = (P1[r]*P2[r]*P3[r])/(1-(SPrz1[r]*SPrz2[r]*SPrz3[r]))
      #browser()
      }
    LLT[q] = sum(Sumx)/NROW(ux)
  }
  return(log(LLT))
}

fx <<- matrix(1,6,1)    # Defind the variables of the
#init_disp <- c((1/m1$theta),(1/m2$theta))
sig_vect <<-matrix(1,36,1)
#=============================Call the function for test==================================
startx1 = c(Start,fx,sig_vect)  #,init_disp,sig_vect
library(maxLik)
ML2 <- maxLik(LLF2, start = startx1,method = "bfgs"
              ,control=list(printLevel=4))
# ================================================================================
#           Calculate teh Variance-Covaraince Matrix and Correlation
# ================================================================================

"-------Variance Covaraince Matrix -------"
"-------final iter = 79 and at convergence 228"
beta <- ML2$estimate
fn1  <- beta[43]
fn2  <- beta[44]
fn3  <- beta[45]
fn4  <- beta[46]
fn5  <- beta[47]
fn6  <- beta[48]
Var1 <- (fn1^2)
Var2 <- (fn2^2+fn3^2)
Var3 <- (fn4^2+fn5^2+fn6^2)
Cov12 <- fn1*fn2            # between Young and Middle aged drivers
Cov13 <- fn1*fn4            # between Young and Senior Drivers
Cov23 <- fn2*fn4+fn3*fn5    # between Middle aged and Senior drivers

Corr12 <- (fn1*fn2)/(fn1^2*(fn2^2+fn3^2))^0.5
Corr13 <- (fn1*fn4)/(fn1^2*(fn4^2+fn5^2+fn6^2))^0.5
Corr23 <- (fn2*fn2)/((fn2^2+fn3^2)*(fn4^2+fn5^2+fn6^2))^0.5

VC <- matrix(c(Var1,Cov12,Cov23,Cov12,Var2,Cov23,Cov13,Cov23,Var3),3,3)
COR <- matrix(c(1.00,Corr12,Corr13,Corr12,1.00,Corr23,Corr13,Corr23,1.00),3,3)
prmatrix(VC);prmatrix(COR)


# ================================================================================
#           Calculate Sandwich Standard Error in Two ways,
# ================================================================================
# Calculate the Hessian Sandwich Estimator
library(sandwich)
library(lmtest)
G <- ML2$gradient   # Get the gradient as a matrix for each parameter you want to estiamte
H <- ML2$hessian
sqrt(-solve(hessian(ML2)))
SE1 <- diag(sqrt(-solve(H)))
coeftest(ML2, vcov=sandwich)
vcov(ML2) # Caculate the variance-covariance matrix
coef(ML2)
logLik(ML2)

# Extract the gradients evaluated at each observation
library( sandwich )
Gradx <- estfun( ML2 )

# How to caculate the numerical gradient
Grad <-numericGradient(LLF2,coef(ML2)) #coef(ML2) c(2.561980,3.33142 ,-1.319369)
GX <- cbind(mean(Grad[,1]),mean(Grad[,2]),mean(Grad[,3]))
GX <-as.matrix(GX,3,1)
all.equal( c( estfun( ML2 ) ), GX )
# Verify as: cbind(Gradx[,1],Grad[,1])
JacobianX =(t(Gradx)%*%(Gradx))
HessianX = ML2$hessian
G2 = (solve(HessianX)%*%(JacobianX)%*%solve(HessianX))
V = (G2) # variance-covariance matrix is actually the estimator above
SE2 = sqrt(diag(V))

# Comparison among the two different estimators
cbind(SE1,SE2)
cbind(coef(ML2)/SE1,coef(ML2)/SE2)

# ================================================================================
#           Calculate the Standard Error for Display [Final Outcome]
# ================================================================================

cat("\014")                      # clean the console area

ff = logLik(ML2)/NROW(Data1)  # To match similar function in GAUSS code
AICx = -2*ff*NROW(Data1)+2*NROW(coef(ML2))   # Check with AIC(ML2) Similar value you get
BICx = -2*ff*NROW(Data1)+(NROW(coef(ML2)*log(NROW(Data1))))
LLx = ff*NROW(Data1)
SSx = (sum(diag(Gradx)*solve(HessianX)))
CLICx = LLx-SSx     # usually for the CML estimation comparison

# MacFadden's Rho Square
# rho <- 1-(LL1/LL0)
# rho.adj <- 1-((LL1-length(parameter))/LL0)
# t-values
t_stat1 <- coef(ML2)/SE1    # From inverse Hessian only
t_stat2 <- coef(ML2)/SE2    # From Sandwich Estimator Theory
# Display all estimation results
estimate <- ML2$estimate
standard_Err <- SE2
# rankx <- ifelse(abs(t_stat2)>1.96,"***",".")
results <- cbind(estimate,standard_Err,t_stat2)  #,rankx,deparse.level = 2)

rownames(results) <- c(
"(Intercept1)",
"NMajor" ,
"NMinor" ,
"Others_dum" ,
"RW1_2      " ,
"RW1_3      " ,
"RW1_4      " ,
"RW1_5      " ,
"Speed_Limit1",
"Speed_Limit2",
"Speed_Limit3",
"Speed_Limit5",
"LNSTV12h"    ,
"STV12h_dum"  ,
"(Intercept2)",
"NMajor     ",
"NMinor     ",
"Others_dum ",
"RW1_2      ",
"RW1_3      ",
"RW1_4      ",
"RW1_5      ",
"Speed_Limit1",
"Speed_Limit2",
"Speed_Limit3",
"Speed_Limit5",
"LNSTV12h"    ,
"STV12h_dum"  ,
"(Intercept2)",
"NMajor     " ,
"NMinor     " ,
"Others_dum " ,
"RW1_2      " ,
"RW1_3      " ,
"RW1_4      " ,
"RW1_5      " ,
"Speed_Limit1",
"Speed_Limit2",
"Speed_Limit3",
"Speed_Limit5",
"LNSTV12h"    ,
"STV12h_dum"  ,
"f1",
"f2",
"f3",
"f4",
"f5",
"f6")
print(results)
print("Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1")
paste("Log-likelihood at convergence = ", logLik(ML2))
paste("AIC    = ",AICx)
paste("BIC    = ",BICx)
paste("CLICx  = ",CLICx)




