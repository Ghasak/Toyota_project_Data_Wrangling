#  Title :           Traffic Accident Analysis                         	    # 
#  Project Name:     Toyota City carsh data 						                    # 
#  Starting Data:    2018/April/02                                          #
#  File Name:        [1] Multivariate Truncated Poisson [First Trail]       #
#  Version:          V.01                                                   #
#  Last changed:     2018/July/25 17:56:05                                  #
#  Purpose:          Analysis different driver age groups		                #
#  Author:           Ghasak Ibrahim                                         #
#  Copyright:        (C) 2018-~                                             #
#  Product:                                                                 #
#  Please see the     note.txt file for more information on this model      #
#  All other righ    ts reserved.                                           #
#   Multivaraite     Truncated Poisson Model Using Copula and CML		        #	 	
#   parameterizin    g e expected number of crashes function only, 	        #	
#   Homoscedastic     model 				    						                        #

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
Data1 <- read.csv("/Users/ghasak/Desktop/TOYOTA_R_Analysis/Dataset/PartA.csv")

Total       = Data1[,1]
Young       = Data1[,2]
Middle_age  = Data1[,3]
Senior      = Data1[,4]
# ================================================================================
NMajor 			    		= Data1[,7]
NMinor							= Data1[,6]
Others_dum          = Data1[,8]
#// Road width in m
RW1_2               = Data1[,15]
RW1_3               = Data1[,16]
RW1_4						    = Data1[,17]
RW1_5							  = Data1[,18]
#// Speed limit allowence Speed_limit5 means no_speed_regulations
Speed_Limit1        = Data1[,20]
Speed_Limit2        = Data1[,21]
Speed_Limit3        = Data1[,22]
Speed_Limit5        = Data1[,24]
#// Traffic volume data 
LNSTV12h            = Data1[,30]
STV12h_dum          = Data1[,31]
# ================================================================================
NMajor 			    		= as.matrix(NMajor      ,NROW(Data1),1)
NMinor							= as.matrix(NMinor      ,NROW(Data1),1)
Others_dum          = as.matrix(Others_dum  ,NROW(Data1),1)
RW1_2               = as.matrix(RW1_2       ,NROW(Data1),1)
RW1_3               = as.matrix(RW1_3       ,NROW(Data1),1)
RW1_4						    = as.matrix(RW1_4       ,NROW(Data1),1)
RW1_5							  = as.matrix(RW1_5       ,NROW(Data1),1)
Speed_Limit1        = as.matrix(Speed_Limit1,NROW(Data1),1)
Speed_Limit2        = as.matrix(Speed_Limit2,NROW(Data1),1)
Speed_Limit3        = as.matrix(Speed_Limit3,NROW(Data1),1)
Speed_Limit5        = as.matrix(Speed_Limit5,NROW(Data1),1)
LNSTV12h            = as.matrix(LNSTV12h    ,NROW(Data1),1)
STV12h_dum          = as.matrix(STV12h_dum  ,NROW(Data1),1)
# ================================================================================
#               Halton Sequence in R-Using the package randtoolbox
# ================================================================================
library(randtoolbox)
dim1 = 1  # How many chains you want to draw
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
m1 <- glm(Total ~NMajor
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

Start_m1 <<- matrix(Start_m1,nrow = NROW(Start_m1),1)


Start <<- Start_m1

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
  f1  <<- exp(param[15])
 
  # ========= Define the Varibles for the MSL=================	  
  lmx1      <<- matrix(0,NROW(ux),1)

  SPrz1  	<<- matrix(0,NROW(ux),1)

  P1		<<- matrix(0,NROW(ux),1)
  Young <<- as.matrix(Young,NROW(Data1),1)
  LLT       <<- matrix(0,NROW(Data1),1)   # Probabilit variable for each indivdiual q
  # ========= Monte Carlo Simulation Started Here=================
  for (q in 1:NROW(Data1)) {
    Sumx <<- matrix(0,NROW(ux),1)
    for (r in 1:NROW(ux)){
      # ========== Expected Number of Crashes of Young Drivers
      lmx1[r] = exp(B1
                    + B2  * NMajor[q]
                    + B3  * NMinor[q]
                    + B4  * Others_dum[q]
                    + B5  * RW1_2[q]
                    + B6  * RW1_3[q]
                    + B7  * RW1_4[q]
                    + B8  * RW1_5[q]
                    + B9  * Speed_Limit1[q]
                    + B10 * Speed_Limit2[q]
                    + B11 * Speed_Limit3[q]
                    + B12 * Speed_Limit5[q]
                    + B13 * LNSTV12h[q]
                    + B14 * STV12h_dum[q]
                    + f1  * ux[r])
     
      # ========== Calculate the probability
      P1[r] = exp((Total[q])*(log(lmx1[r]))-(lmx1[r])-lfactorial(Total[q]))
     
      # ========== Probability of Zero 
      SPrz1[r] = exp(-lmx1[r])
      
      # ========== Probability of Zero 
      # === It seems that R cant assign matrix to a constant value so you have to 
      # === Define the sum as a vector
      # === Define the Truncated Probability Function
      # Sumx[r] = (P1[r]*P2[r]*P3[r])/(1-(SPrz1[r]*SPrz2[r]*SPrz3[r]))
      # 
      Sumx[r] = (P1[r])/(1-(SPrz1[r]))
    }
    # === Get the average
    LLT[q] = sum(Sumx)/NROW(ux)
    
    
    
  }
  #browser()
  
  return(log(LLT))
}

#=============================Call the function for test==================================
startx1 = c(Start,0)
library(maxLik)
ML2 <- maxLik(LLF2, start = startx1,method = "bfgs"
              ,control=list(printLevel=4))






