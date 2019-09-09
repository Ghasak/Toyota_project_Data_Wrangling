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
"/Users/ghasak/Desktop/TOYOTA_R_Analysis/Dataset/PartA.csv"
# Data1 <- read.csv(file.choose())
Data1 <- read.csv("C:/Users/ghasak/Desktop/Toyota Estimation new/PartA.csv")

Total       = Data1[,1]
Young       = Data1[,2]
Middle_age  = Data1[,3]
Senior      = Data1[,4]
# ================================================================================
NMajor                      = Data1[,7]
NMinor                          = Data1[,6]
Others_dum          = Data1[,8]
#// Road width in m
RW1_2               = Data1[,15]
RW1_3               = Data1[,16]
RW1_4                           = Data1[,17]
RW1_5                             = Data1[,18]
#// Speed limit allowence Speed_limit5 means no_speed_regulations
Speed_Limit1        = Data1[,20]
Speed_Limit2        = Data1[,21]
Speed_Limit3        = Data1[,22]
Speed_Limit5        = Data1[,24]
#// Traffic volume data 
LNSTV12h            = Data1[,30]
STV12h_dum          = Data1[,31]
# ================================================================================
#               Halton Sequence in R-Using the package randtoolbox
# ================================================================================
library(randtoolbox)
dim1 = 42  # How many chains you want to draw
# You can get Normal distribution if you make normal =TRUE
n = 130
ux= halton(n, dim = dim1, init = TRUE, normal = TRUE, usetime = FALSE)
# sobol(n, dim = 1, init = TRUE, scrambling = 0, seed = 4711, normal = FALSE)
# torus(n, dim = 1, prime, init = TRUE, mixed = FALSE, usetime = FALSE,normal=FALSE)
# ================================================================================
#               Run Univariate Poisson to get start values
# ================================================================================
#  the sing << to show the variable as a global varaible so you see this inside the function 
# foo <- function(){
#   bar <<- 1
# }


# ===========================Young Drivers=============================
m1 <- glm(Young ~NMajor
          +NMinor
          +Others_dum
          +RW1_2
          +RW1_3
          +RW1_4
          +RW1_5
          +Speed_Limit1
          +Speed_Limit2
          +Speed_Limit3
          +Speed_Limit5
          +LNSTV12h
          +STV12h_dum, family="poisson", data=Data1)

#summary(m1)
Start_m1 <<- m1$coefficients

# ===========================Middle_age Drivers=============================
m2 <- glm(Middle_age ~NMajor
          +NMinor
          +Others_dum
          +RW1_2
          +RW1_3
          +RW1_4
          +RW1_5
          +Speed_Limit1
          +Speed_Limit2
          +Speed_Limit3
          +Speed_Limit5
          +LNSTV12h
          +STV12h_dum, family="poisson", data=Data1)

#summary(m1)
Start_m2 <<- m2$coefficients
# ===========================Senior Drivers=============================
m3 <- glm(Senior ~NMajor
          +NMinor
          +Others_dum
          +RW1_2
          +RW1_3
          +RW1_4
          +RW1_5
          +Speed_Limit1
          +Speed_Limit2
          +Speed_Limit3
          +Speed_Limit5
          +LNSTV12h
          +STV12h_dum, family="poisson", data=Data1)

#summary(m1)
Start_m3 <<- m3$coefficients

Start_m1 <<- matrix(Start_m1,nrow = NROW(Start_m1),1)
Start_m2 <<- matrix(Start_m2,nrow = NROW(Start_m2),1)
Start_m3 <<- matrix(Start_m3,nrow = NROW(Start_m3),1)

Start <<- rbind(Start_m1,Start_m2,Start_m3)

# ================================================================================
#              Maximum Simulated Likelihood Function Core
# ================================================================================

LLF2 <<- function (param){
# ========= Parameters Input=================
      B1  <<- param[1]
      B2  <<- param[2]
      B3  <<- param[3]
      B4  <<- param[4]
      B5  <<- param[5]
      B6  <<- param[6]
      B7  <<- param[7]
      B8  <<- param[8]
      B9  <<- param[9]
      B10 <<- param[10]
      B11 <<- param[11]
      B12 <<- param[12]
      B13 <<- param[13]
      B14 <<- param[14]
      B15 <<- param[15]
      B16 <<- param[16]
      B17 <<- param[17]
      B18 <<- param[18]
      B19 <<- param[19]
      B20 <<- param[20]
      B21 <<- param[21]
      B22 <<- param[22]
      B23 <<- param[23]
      B24 <<- param[24]
      B25 <<- param[25]
      B26 <<- param[26]
      B27 <<- param[27]
      B28 <<- param[28]
      B29 <<- param[29]
      B30 <<- param[30]
      B31 <<- param[31]
      B32 <<- param[32]
      B33 <<- param[33]
      B34 <<- param[34]
      B35 <<- param[35]
      B36 <<- param[36]
      B37 <<- param[37]
      B38 <<- param[38]
      B39 <<- param[39]
      B40 <<- param[40]
      B41 <<- param[41]
      B42 <<- param[42]
      f1  <<- param[43]
      f2  <<- param[44]
      f3  <<- param[45]
      f4  <<- param[46]
      f5  <<- param[47]
      f6  <<- param[48] 
      f7  <<- param[49]
      f8  <<- param[50]
      f9  <<- param[51]
      f10 <<- param[52]
      f11 <<- param[53]
      f12 <<- param[54]
      f13 <<- param[55]
      f14 <<- param[56]
      f15 <<- param[57]
      f16 <<- param[58]
      f17 <<- param[59]
      f18 <<- param[60]
      f19 <<- param[61]
      f20 <<- param[62]
      f21 <<- param[63]
      f22 <<- param[64]
      f23 <<- param[65]
      f24 <<- param[66]
      f25 <<- param[67]
      f26 <<- param[68]
      f27 <<- param[69]
      f28 <<- param[70]
      f29 <<- param[71]
      f30 <<- param[72] 
      f31 <<- param[73]
      f32 <<- param[74]
      f33 <<- param[75]
      f34 <<- param[76]
      f35 <<- param[77]
      f36 <<- param[78]
      f37 <<- param[79]
      f38 <<- param[80]
      f39 <<- param[81]
      f40 <<- param[82]
      f41 <<- param[83]
      f42 <<- param[84]
      f43 <<- param[85] 
      f44 <<- param[86] 
      f45 <<- param[87] 
      
# ========= Define the Varibles for the MSL=================      
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
# ========= Monte Carlo Simulation Started Here=================
      for (q in 1:NROW(Data1)) {
        Sumx <<- matrix(0,NROW(ux),1)
        for (r in 1:NROW(ux)){
            # ========== Expected Number of Crashes of Young Drivers
            lmx1[r] = exp(B1
                          + (B2 +f7 *ux[r, 4]) * NMajor[q]
                          + (B3 +f8 *ux[r, 5]) * NMinor[q]
                          + (B4 +f9 *ux[r, 6]) * Others_dum[q]
                          + (B5 +f10*ux[r, 7]) * RW1_2[q]
                          + (B6 +f11*ux[r, 8]) * RW1_3[q]
                          + (B7 +f12*ux[r, 9]) * RW1_4[q]
                          + (B8 +f13*ux[r, 10])* RW1_5[q]
                          + (B9 +f14*ux[r, 11])* Speed_Limit1[q]
                          + (B10+f15*ux[r,12]) * Speed_Limit2[q]
                          + (B11+f16*ux[r,13]) * Speed_Limit3[q]
                          + (B12+f17*ux[r,14]) * Speed_Limit5[q]
                          + (B13+f18*ux[r,15]) * LNSTV12h[q]
                          + (B14+f19*ux[r,16]) * STV12h_dum[q]
                          + f1  * ux[r,1])
            # ========== Expected Number of Crashes of Middle aged Drivers
            lmx2[r] = exp(B15
                          + (B16+f20 *ux[r,17]) * NMajor[q]
                          + (B17+f21 *ux[r,18]) * NMinor[q]
                          + (B18+f22 *ux[r,19]) * Others_dum[q]
                          + (B19+f23 *ux[r,20]) * RW1_2[q]
                          + (B20+f24 *ux[r,21]) * RW1_3[q]
                          + (B21+f25 *ux[r,22]) * RW1_4[q]
                          + (B22+f26 *ux[r,23]) * RW1_5[q]
                          + (B23+f27 *ux[r,24]) * Speed_Limit1[q]
                          + (B24+f28 *ux[r,25]) * Speed_Limit2[q]
                          + (B25+f29 *ux[r,26]) * Speed_Limit3[q]
                          + (B26+f30 *ux[r,27]) * Speed_Limit5[q]
                          + (B27+f31 *ux[r,28]) * LNSTV12h[q]
                          + (B28+f32 *ux[r,29]) * STV12h_dum[q]
                          + f2  * ux[r,1]
                          + f3  * ux[r,2])
            # ========== Expected Number of Crashes of Senior Drivers
            lmx3[r] = exp(B29
                          + (B30+f33 *ux[r,30])* NMajor[q]
                          + (B31+f34 *ux[r,31])* NMinor[q]
                          + (B32+f35 *ux[r,32])* Others_dum[q]
                          + (B33+f36 *ux[r,33])* RW1_2[q]
                          + (B34+f37 *ux[r,34])* RW1_3[q]
                          + (B35+f38 *ux[r,35])* RW1_4[q]
                          + (B36+f39 *ux[r,36])* RW1_5[q]
                          + (B37+f40 *ux[r,37])* Speed_Limit1[q]
                          + (B38+f41 *ux[r,38])* Speed_Limit2[q]
                          + (B39+f42 *ux[r,39])* Speed_Limit3[q]
                          + (B40+f43 *ux[r,40])* Speed_Limit5[q]
                          + (B41+f44 *ux[r,41])* LNSTV12h[q]
                          + (B42+f45 *ux[r,42])* STV12h_dum[q]
                          + f4  * ux[r,1]
                          + f5  * ux[r,2]
                          + f6  * ux[r,3])  
            # ========== Calculate the probability
            P1[r] = exp((Young[q])*(log(lmx1[r]))-(lmx1[r])-lfactorial(Young[q]))
            P2[r] = exp((Middle_age[q])*(log(lmx2[r]))-(lmx2[r])-lfactorial(Middle_age[q]))
            P3[r] = exp((Senior[q])*(log(lmx3[r]))-(lmx3[r])-lfactorial(Senior[q]))
            # ========== Probability of Zero 
            SPrz1[r] = exp(-lmx1[r])
            SPrz2[r] = exp(-lmx2[r])
            SPrz3[r] = exp(-lmx3[r])
            # ========== Probability of Zero 
            # === It seems that R cant assign matrix to a constant value so you have to 
            # === Define the sum as a vector
            # === Define the Truncated Probability Function
            Sumx[r] = (P1[r]*P2[r]*P3[r])/(1-(SPrz1[r]*SPrz2[r]*SPrz3[r]))
        }
            # === Get the average
            LLT[q] = sum(Sumx)/NROW(ux)

      }
      return(log(LLT))
    }
  

fx <<- matrix(0.1,45,1)    # Defind the variables of the 
#=============================Call the function for test==================================
startx1 = c(Start,fx)
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
"f6",
"sigma1 ",
"sigma2 ",
"sigma3 ",
"sigma4 ",
"sigma5 ",
"sigma6 ",
"sigma7 ",
"sigma8 ",
"sigma9 ",
"sigma10",
"sigma11",
"sigma12",
"sigma13",
"sigma14",
"sigma15",
"sigma16",
"sigma17",
"sigma18",
"sigma19",
"sigma20",
"sigma21",
"sigma22",
"sigma23",
"sigma24",
"sigma25",
"sigma26",
"sigma27",
"sigma28",
"sigma29",
"sigma30",
"sigma31",
"sigma32",
"sigma33",
"sigma34",
"sigma35",
"sigma36",
"sigma37",
"sigma38",
"sigma39")
print(results)
print("Signif. codes:  0 â€?***â€? 0.001 â€?**â€? 0.01 â€?*â€? 0.05 â€?.â€? 0.1 â€? â€? 1")
paste("Log-likelihood at convergence = ", logLik(ML2))
paste("AIC    = ",AICx)
paste("BIC    = ",BICx)
paste("CLICx  = ",CLICx)



     
