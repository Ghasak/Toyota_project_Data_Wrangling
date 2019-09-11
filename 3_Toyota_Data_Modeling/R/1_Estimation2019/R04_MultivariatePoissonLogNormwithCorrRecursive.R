#  Title :           Traffic Accident Analysis                              #
#  Project Name:     Toyota City carsh data                                 #
#  Starting Data:    2019/Sep.l/00                                          #
#  File Name:        [1] Multivariate Truncated Poisson [First Trail]       #
#  Version:          V.01                                                   #
#  Last changed:     2019/Sep./00 00:00:00                                  #
#  Purpose:          Analysis different driver age groups                   #
#  Author:           Ghasak Ibrahim                                         #
#  Copyright:        (C) 2019-Sep.                                          #
#  Product:                                                                 #
#  Please see the     note.txt file for more information on this model      #
#  All other rights reserved.                                               #
#       Multivaraite Truncated Poisson Model Using Copula and CML           #
#   parameterizing   expected number of crashes function only,              #
#   Homoscedastic     model                                                 #
# ========================================================================= #
# =========================================================================
#               Cleaning the background of intialize Space
# =========================================================================
while (!is.null(dev.list()))  dev.off(dev.list()["RStudioGD"])
#dev.off(dev.list()["RStudioGD"]) # clean the Graph Area
rm(list=ls())                    # clean the Workspace (dataset)
cat("\014")                      # clean the console area
graphics.off()                   # close graphics windows (For R Script)

# =========================================================================
#           Input Data and Intializing the parameter vectors
# =========================================================================

# Data1 <- read.csv(file.choose())
directory_location <- "~/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/R/0_DataSet/dataSet.csv"
#directory_location <- "/Users/ghasak/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/R/0_DataSet/dataSet.csv"
#directory_location <- paste0(getwd(),'/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/R/0_DataSet/dataSet.csv')
Data1 <- read.csv(directory_location)

Total       = Data1$Crash_count
Young       = Data1$Driver_Young
Middle_age  = Data1$Driver_Middle_age
Senior      = Data1$Driver_Senior
# =======================================================================
#               Data Frame converting our data [Similar to Pandas]
# =======================================================================
MinorPrefecturalRoad             <- Data1$Minor_prefectural_road
OtherRoadTypes                   <- Data1$Narrow_road
Conf30KmhorLess                  <- Data1$conf1_30kmh_orless
Conf40KmhorLess                  <- Data1$conf1_40kmh_orless
Conf50KmhorLess                  <- Data1$conf1_50kmh_orless
Conf60KmhorLess                  <- Data1$conf1_60kmh_orless
ConfNoRegulation                 <- Data1$conf1_No_regulation
LogTrafficVolume                 <- Data1$log_traffic_volume
IntersTypeThreeArms              <- Data1$IS_IT_THREE_ARMS
LogShortestWidth                 <- Data1$LOG_SHORTEST_WIDTH_INTER
LogNoDriveWays                   <- Data1$LOG_NO_DRIVE_WAYS
LogNoLanes                       <- Data1$LOG_NUMBER_OF_LANES
NoLanesChanged                   <- Data1$NO_OF_LANES_CHANGED
IsThereSkewness                  <- Data1$IS_THERE_SKEWNESS
NonDividedSigleRoadway           <- Data1$NON_DIVIDED_SINGLE_ROADWAY
LogAverageWidthPhysicalMedian    <- Data1$LOG_AVERAGE_WIDTH_PHYSICAL_MEDIAN
IsThereCentralStrip              <- Data1$IS_THERE_CENTRAL_STRIP
SignalizedHighLevelSignal        <- Data1$SIGNALIZED_HIGH_LEVEL_SIGNAL
PedestrianSignalExisted          <- Data1$FLASHING_GREEN_PED

# =======================================================================
#               Halton Sequence in R-Using the package randtoolbox
# =======================================================================
library(randtoolbox)
dim1 = 3  # How many chains you want to draw
# You can get Normal distribution if you make normal =TRUE
n = 130
ux= halton(n, dim = dim1, init = TRUE, normal = TRUE, usetime = FALSE)
# sobol(n, dim = 1, init = TRUE, scrambling = 0, seed = 4711, normal = FALSE)
# torus(n, dim = 1, prime, init = TRUE, mixed = FALSE, usetime = FALSE,normal=FALSE)

# =====================================================================
#               Run Univariate Poisson to get start values
# =====================================================================
require(maxLik)
require(sandwich)
require(foreign)
require(ggplot2)
require(MASS)

outcome <- "Total"
variables <-   c("MinorPrefecturalRoad",
                 "OtherRoadTypes",
                 "Conf30KmhorLess",
                 "Conf40KmhorLess",
                 "Conf50KmhorLess",
                 "Conf60KmhorLess",
                 "ConfNoRegulation",
                 "LogTrafficVolume",
                 "IntersTypeThreeArms",
                 "LogShortestWidth",
                 "LogNoDriveWays",
                 "LogNoLanes",
                 "NoLanesChanged",
                 "IsThereSkewness",
                 "NonDividedSigleRoadway",
                 "LogAverageWidthPhysicalMedian",
                 "IsThereCentralStrip",
                 "SignalizedHighLevelSignal",
                 "PedestrianSignalExisted")

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

# ===============================================================
#              Maximum Simulated Likelihood For
#             Multivariate Indpendent Count Model
# ===============================================================
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
    beta10 <-  b[10]
    beta11 <-  b[11]
    beta12 <-  b[12]
    beta13 <-  b[13]
    beta14 <-  b[14]
    beta15 <-  b[15]
    beta16 <-  b[16]
    beta17 <-  b[17]
    beta18 <-  b[18]
    beta19 <-  b[19]
    beta20 <-  b[20]
    beta21 <-  b[21]
    beta22 <-  b[22]
    beta23 <-  b[23]
    beta24 <-  b[24]
    beta25 <-  b[25]
    beta26 <-  b[26]
    beta27 <-  b[27]
    beta28 <-  b[28]
    beta29 <-  b[29]
    beta30 <-  b[30]
    beta31 <-  b[31]
    beta32 <-  b[32]
    beta33 <-  b[33]
    beta34 <-  b[34]
    beta35 <-  b[35]
    beta36 <-  b[36]
    beta37 <-  b[37]
    beta38 <-  b[38]
    beta39 <-  b[39]
    beta40 <-  b[40]
    beta41 <-  b[41]
    beta42 <-  b[42]
    beta43 <-  b[43]
    beta44 <-  b[44]
    beta45 <-  b[45]
    beta46 <-  b[46]
    beta47 <-  b[47]
    beta48 <-  b[48]
    beta49 <-  b[49]
    beta50 <-  b[50]
    beta51 <-  b[51]
    beta52 <-  b[52]
    beta53 <-  b[53]
    beta54 <-  b[54]
    beta55 <-  b[55]
    beta56 <-  b[56]
    beta57 <-  b[57]
    beta58 <-  b[58]
    beta59 <-  b[59]
    beta60 <-  b[60]

    f1     <-  b[61]
    #f2     <-  b[62]
    f3     <-  b[62]
    #f4     <-  b[64]
    #f5     <-  b[65]
    f6     <-  b[63]

for (q in 1:NROW(Data1)) {
    Sumx <<- matrix(0,NROW(ux),1)
      for (r in 1:NROW(ux)){
          lmx1[r] = exp(   beta1
                         + beta2 * MinorPrefecturalRoad[q]
                         + beta3 * OtherRoadTypes[q]
                         + beta4 * Conf30KmhorLess[q]
                         + beta5 * Conf40KmhorLess[q]
                         + beta6 * Conf50KmhorLess[q]
                         + beta7 * Conf60KmhorLess[q]
                         + beta8 * ConfNoRegulation[q]
                         + beta9 * LogTrafficVolume[q]
                         + beta10* IntersTypeThreeArms[q]
                         + beta11* LogShortestWidth[q]
                         + beta12* LogNoDriveWays[q]
                         + beta13* LogNoLanes[q]
                         + beta14* NoLanesChanged[q]
                         + beta15* IsThereSkewness[q]
                         + beta16* NonDividedSigleRoadway[q]
                         + beta17* LogAverageWidthPhysicalMedian[q]
                         + beta18* IsThereCentralStrip[q]
                         + beta19* SignalizedHighLevelSignal[q]
                         + beta20* PedestrianSignalExisted[q]
                         + f1 * ux[r,1])

          lmx2[r] = exp(   beta21
                         + beta22* MinorPrefecturalRoad[q]
                         + beta23* OtherRoadTypes[q]
                         + beta24* Conf30KmhorLess[q]
                         + beta25* Conf40KmhorLess[q]
                         + beta26* Conf50KmhorLess[q]
                         + beta27* Conf60KmhorLess[q]
                         + beta28* ConfNoRegulation[q]
                         + beta29* LogTrafficVolume[q]
                         + beta30* IntersTypeThreeArms[q]
                         + beta31* LogShortestWidth[q]
                         + beta32* LogNoDriveWays[q]
                         + beta33* LogNoLanes[q]
                         + beta34* NoLanesChanged[q]
                         + beta35* IsThereSkewness[q]
                         + beta36* NonDividedSigleRoadway[q]
                         + beta37* LogAverageWidthPhysicalMedian[q]
                         + beta38* IsThereCentralStrip[q]
                         + beta39* SignalizedHighLevelSignal[q]
                         + beta40* PedestrianSignalExisted[q]
                         #+ f2 * ux[r,1]
                         + f3 * ux[r,2])

          lmx3[r] = exp(   beta41
                         + beta42* MinorPrefecturalRoad[q]
                         + beta43* OtherRoadTypes[q]
                         + beta44* Conf30KmhorLess[q]
                         + beta45* Conf40KmhorLess[q]
                         + beta46* Conf50KmhorLess[q]
                         + beta47* Conf60KmhorLess[q]
                         + beta48* ConfNoRegulation[q]
                         + beta49* LogTrafficVolume[q]
                         + beta50* IntersTypeThreeArms[q]
                         + beta51* LogShortestWidth[q]
                         + beta52* LogNoDriveWays[q]
                         + beta53* LogNoLanes[q]
                         + beta54* NoLanesChanged[q]
                         + beta55* IsThereSkewness[q]
                         + beta56* NonDividedSigleRoadway[q]
                         + beta57* LogAverageWidthPhysicalMedian[q]
                         + beta58* IsThereCentralStrip[q]
                         + beta59* SignalizedHighLevelSignal[q]
                         + beta60* PedestrianSignalExisted[q]
                         #+ f4 * ux[r,1]
                         #+ f5 * ux[r,2]
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


fx <<- matrix(1,3,1)    # Defind the variables of the
#init_disp <- c((1/m1$theta),(1/m2$theta))
#sig_vect <<-matrix(1,36,1)
#=============================Call the function for test==================
startx1 = c(Start,fx)  #,init_disp,sig_vect
library(maxLik)
ML2 <- maxLik(LLF2, start = startx1,method = "bfgs"
              ,control=list(printLevel=4))

# ==================================================================
#    Calculate teh Variance-Covaraince Matrix and Correlation
# ==================================================================

"-------Variance Covaraince Matrix -------"
"-------final iter = 79 and at convergence 228"
beta  <- ML2$estimate
fn1   <- beta[61]
fn2   <- 0
fn3   <- beta[62]
fn4   <- 0
fn5   <- 0
fn6   <- beta[63]
Var1  <-  (fn1^2)
Var2  <-  (fn2^2+fn3^2)
Var3  <-  (fn4^2+fn5^2+fn6^2)
Cov12 <-  fn1*fn2            # between Young and Middle aged drivers
Cov13 <-  fn1*fn4            # between Young and Senior Drivers
Cov23 <-  fn2*fn4+fn3*fn5    # between Middle aged and Senior drivers

Corr12 <- (fn1*fn2)/(fn1^2*(fn2^2+fn3^2))^0.5
Corr13 <- (fn1*fn4)/(fn1^2*(fn4^2+fn5^2+fn6^2))^0.5
Corr23 <- (fn2*fn2)/((fn2^2+fn3^2)*(fn4^2+fn5^2+fn6^2))^0.5

VC <- matrix(c(Var1,Cov12,Cov23,Cov12,Var2,Cov23,Cov13,Cov23,Var3),3,3)
COR <- matrix(c(1.00,Corr12,Corr13,Corr12,1.00,Corr23,Corr13,Corr23,1.00),3,3)
prmatrix(VC);prmatrix(COR)


# =====================================================================
#           Calculate Sandwich Standard Error in Two ways,
# =====================================================================
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

# ==========================================================================
#           Calculate the Standard Error for Display [Final Outcome]
# ==========================================================================

# cat("\014")                      # clean the console area

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
"MinorPrefecturalRoad",
"OtherRoadTypes",
"Conf30KmhorLess",
"Conf40KmhorLess",
"Conf50KmhorLess",
"Conf60KmhorLess",
"ConfNoRegulation",
"LogTrafficVolume",
"IntersTypeThreeArms",
"LogShortestWidth",
"LogNoDriveWays",
"LogNoLanes",
"NoLanesChanged",
"IsThereSkewness",
"NonDividedSigleRoadway",
"LogAverageWidthPhysicalMedian",
"IsThereCentralStrip",
"SignalizedHighLevelSignal",
"PedestrianSignalExisted",
"(Intercept2)",
"MinorPrefecturalRoad",
"OtherRoadTypes",
"Conf30KmhorLess",
"Conf40KmhorLess",
"Conf50KmhorLess",
"Conf60KmhorLess",
"ConfNoRegulation",
"LogTrafficVolume",
"IntersTypeThreeArms",
"LogShortestWidth",
"LogNoDriveWays",
"LogNoLanes",
"NoLanesChanged",
"IsThereSkewness",
"NonDividedSigleRoadway",
"LogAverageWidthPhysicalMedian",
"IsThereCentralStrip",
"SignalizedHighLevelSignal",
"PedestrianSignalExisted",
"(Intercept3)",
"MinorPrefecturalRoad",
"OtherRoadTypes",
"Conf30KmhorLess",
"Conf40KmhorLess",
"Conf50KmhorLess",
"Conf60KmhorLess",
"ConfNoRegulation",
"LogTrafficVolume",
"IntersTypeThreeArms",
"LogShortestWidth",
"LogNoDriveWays",
"LogNoLanes",
"NoLanesChanged",
"IsThereSkewness",
"NonDividedSigleRoadway",
"LogAverageWidthPhysicalMedian",
"IsThereCentralStrip",
"SignalizedHighLevelSignal",
"PedestrianSignalExisted",
"f1",
"f3",
"f6")
print(results)
print("Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1")
paste("Log-likelihood at convergence = ", logLik(ML2))
paste("AIC    = ",AICx)
paste("BIC    = ",BICx)
paste("CLICx  = ",CLICx)

