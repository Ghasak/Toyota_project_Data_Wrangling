##########################################################################
dev.off(dev.list()["RStudioGD"]) # clean the Graph Area
rm(list=ls())                    # clean the Workspace (dataset)
cat("\014")                      # clean the console area
graphics.off()                   # close graphics windows (For R Script)
#########################################################################
library(extrafont)
windowsFonts(A = windowsFont("Times New Roman"))  
# http://stackoverflow.com/questions/27689222/changing-fonts-for-graphs-in-r#
# Clean the Graph Area and the workspace and the console
##########################################################################
# Windows
# mydata=read.csv ("C:\\Users\\Ghasak\\Documents\\MEGA\\MEGAsync\\Dataset\\ToyoData.csv")   # reading csv file
# Mac
# mydata = read.csv("/Users/Ghasak/MEGAsync/Dataset/ToyoData.csv")
# Windows Lab MYM-Lab
  mydata = read.csv("C:\\Users\\ghasak\\Documents\\MEGAsync\\Dataset\\ToyoData.csv")
##########################################################################
library(copula)
library(copBasic)
library(VineCopula)
library(rgl)
library(lattice)
library(evd)
library(maxLik)
##########################################################################
Young      <- mydata[,2]
Middle_age <- mydata[,3]
Senior     <- mydata[,4]
##########################################################################


# Procedure to Calcuate Frank Copula between y1 and y2 with corrleation theta #
  
Frank <- function(aup, adown, bup, bdown,theta ){
  alpha=1e-3;
  n <- length(aup)
  Frankq <- matrix(0,1,n)
  for (q in 1:n){
    
    Frankq[q] <- (((((aup[q]+alpha)^(-theta))+((bup[q]+alpha)^(-theta)))-1)^(-1/theta)
    -((((adown[q]+alpha)^(-theta))+((bup[q])^(-theta)))-1)^(-1/theta)
    -((((aup[q]+alpha)^(-theta))+((bdown[q])^(-theta)))-1)^(-1/theta)
    +((((adown[q]+alpha)^(-theta))+((bdown[q]+alpha)^(-theta)))-1)^(-1/theta))
    
  }
  return(Frankq)
}


##########################################################################
# Calcuate the probabilty of upper and lower parts of the probability

##########################################################################

CDFPG <-function(yin,lambda,up){
  # yin and lambda must be a vector wiht same length  
  n <- length(yin)
  a2u <- matrix(1,1,n)*exp(-lambda);
  if (up == 1) {
    for (q in 1:n){
      #a2u[q]=exp(-lambda[q]);
      i=0
      while(i < yin[q]){ 
        for (i in 1:yin[q]) {
          a2u[q]=a2u[q]+exp(i*log(lambda[q])-(lambda[q])-lfactorial(i));
          i=i+1
        }
        
      }
      
    }
    return(a2u)
  } else if (up == 0) {
    a2l <- matrix(0,1,n)
    for (q in 1:n){
      for (i in 1:yin[q]){
        a2l[q]=a2l[q]+exp((i-1)*log(lambda[q])-(lambda[q])-lfactorial(i-1));
      }
    }
  }
  return(a2l)
}
#######################################################################
LL1 <- function(x) {
  beta_1  <- x[1] 
  beta_2  <- x[2]
  beta_3  <- x[3]
  beta_4  <- x[4] 
  beta_5  <- x[5]
  beta_6  <- x[6]
  beta_7  <- x[7] 
  beta_8  <- x[8]
  beta_9  <- x[9]
  beta_10 <- x[10] 
  beta_11 <- x[11]
  beta_12 <- x[12]
  beta_13 <- x[13] 
  beta_14 <- x[14]
  beta_15 <- x[15]
  beta_16 <- x[16] 
  beta_17 <- x[17]
  beta_18 <- x[18]
  beta_19 <- x[19] 
  beta_20 <- x[20]
  beta_21 <- x[21]
  beta_22 <- x[22] 
  beta_23 <- x[23]
  beta_24 <- x[24]
  beta_25 <- x[25] 
  beta_26 <- x[26]
  beta_27 <- x[27]
  beta_28 <- x[28] 
  beta_29 <- x[29]
  beta_30 <- x[30]
  beta_31 <- x[31] 
  beta_32 <- x[32]
  beta_33 <- x[33]
  beta_34 <- x[34] 
  beta_35 <- x[35]
  beta_36 <- x[36]
  beta_37 <- x[37] 
  beta_38 <- x[38]
  beta_39 <- x[39]
  beta_40 <- x[40] 
  beta_41 <- x[41]
  beta_42 <- x[42]
  
  PrefRoad_dum                <- mydata[,5];
  PrefRoad_dum2               <- mydata[,6];
  Major_PrefRoad_dum          <- mydata[,7];
  Others_dum                  <- mydata[,8];
  speed_Limit1                <- mydata[,9];
  speed_Limit2                <- mydata[,10];
  speed_Limit3                <- mydata[,11];
  speed_Limit4                <- mydata[,12];
  speed_Limit5                <- mydata[,13];
  rw_3_less                   <- mydata[,14];
  rw_3_55                     <- mydata[,15];
  rw_5_13                     <- mydata[,16];
  lnsTV12h                    <- mydata[,17];
  stV12h_dum                  <- mydata[,18];
  
  
  # Expected Crash Funcation for Young Drivers #
  lmy1= exp(beta_1
            +beta_2*PrefRoad_dum2            
            +beta_3*Major_PrefRoad_dum                      
            +beta_4*Others_dum        
            +beta_5*speed_Limit1         
            +beta_6*speed_Limit2         
            +beta_7*speed_Limit3
            +beta_8*speed_Limit4         
            +beta_9*speed_Limit5         
            +beta_10*rw_3_less
            +beta_11*rw_3_55         
            +beta_12*rw_5_13         
            +beta_13*lnsTV12h
            +beta_14*stV12h_dum);         
  # Expected Crash Funcation for Middle Age Drivers #        
  lmy2= exp(beta_15
            +beta_16*PrefRoad_dum2            
            +beta_17*Major_PrefRoad_dum                      
            +beta_18*Others_dum         
            +beta_19*speed_Limit1         
            +beta_20*speed_Limit2         
            +beta_21*speed_Limit3
            +beta_22*speed_Limit4         
            +beta_23*speed_Limit5         
            +beta_24*rw_3_less
            +beta_25*rw_3_55         
            +beta_26*rw_5_13         
            +beta_27*lnsTV12h
            +beta_28*stV12h_dum); 				 
  # Expected Crash Funcation for Senior Drivers #        
  lmy3= exp(beta_29
            +beta_30*PrefRoad_dum2            
            +beta_31*Major_PrefRoad_dum                      
            +beta_32*Others_dum         
            +beta_33*speed_Limit1         
            +beta_34*speed_Limit2         
            +beta_35*speed_Limit3
            +beta_36*speed_Limit4         
            +beta_37*speed_Limit5         
            +beta_38*rw_3_less
            +beta_39*rw_3_55         
            +beta_40*rw_5_13         
            +beta_41*lnsTV12h
            +beta_42*stV12h_dum); 					
  
  
  
  # The Bivariate NBII probability density function
  # Defined as the log-likelihood function
  #Possion Probability caluclation@
  Prob_1 =  Young*log(lmy1)-(lmy1)-lfactorial(Young);
  Prob_2 =  Middle_age*log(lmy2)-(lmy2)-lfactorial(Middle_age);
  Prob_3 =  Senior*log(lmy3)-(lmy3)-lfactorial(Senior);
  # Log-likelihood function
  LL1 <- sum((Prob_1)+(Prob_2)+(Prob_3))
  #browser()
  return(LL1)
  
  
}

start <- matrix(0,nrow=42, ncol = 1)

# The Start value for the dispersion parameter
OPM1 <- optim(start,LL1,method="BFGS",hessian=TRUE,control=list(maxit=10000, fnscale=-1))

# Estimated Parameters
parameter1 <- OPM1$par
#######################################################################

LL <- function(x) {
  # starting time
  start_time <- Sys.time()
  
  iterate_time <<- 0
  
  beta_1  <- x[1] 
  beta_2  <- x[2]
  beta_3  <- x[3]
  beta_4  <- x[4] 
  beta_5  <- x[5]
  beta_6  <- x[6]
  beta_7  <- x[7] 
  beta_8  <- x[8]
  beta_9  <- x[9]
  beta_10 <- x[10] 
  beta_11 <- x[11]
  beta_12 <- x[12]
  beta_13 <- x[13] 
  beta_14 <- x[14]
  beta_15 <- x[15]
  beta_16 <- x[16] 
  beta_17 <- x[17]
  beta_18 <- x[18]
  beta_19 <- x[19] 
  beta_20 <- x[20]
  beta_21 <- x[21]
  beta_22 <- x[22] 
  beta_23 <- x[23]
  beta_24 <- x[24]
  beta_25 <- x[25] 
  beta_26 <- x[26]
  beta_27 <- x[27]
  beta_28 <- x[28] 
  beta_29 <- x[29]
  beta_30 <- x[30]
  beta_31 <- x[31] 
  beta_32 <- x[32]
  beta_33 <- x[33]
  beta_34 <- x[34] 
  beta_35 <- x[35]
  beta_36 <- x[36]
  beta_37 <- x[37] 
  beta_38 <- x[38]
  beta_39 <- x[39]
  beta_40 <- x[40] 
  beta_41 <- x[41]
  beta_42 <- x[42]

  PrefRoad_dum                <- mydata[,5];
  PrefRoad_dum2               <- mydata[,6];
  Major_PrefRoad_dum          <- mydata[,7];
  Others_dum                  <- mydata[,8];
  speed_Limit1                <- mydata[,9];
  speed_Limit2                <- mydata[,10];
  speed_Limit3                <- mydata[,11];
  speed_Limit4                <- mydata[,12];
  speed_Limit5                <- mydata[,13];
  rw_3_less                   <- mydata[,14];
  rw_3_55                     <- mydata[,15];
  rw_5_13                     <- mydata[,16];
  lnsTV12h                    <- mydata[,17];
  stV12h_dum                  <- mydata[,18];


# Expected Crash Funcation for Young Drivers #
lmy1= exp(beta_1
		 +beta_2*PrefRoad_dum2            
		 +beta_3*Major_PrefRoad_dum                      
		 +beta_4*Others_dum        
		 +beta_5*speed_Limit1         
		 +beta_6*speed_Limit2         
		 +beta_7*speed_Limit3
		 +beta_8*speed_Limit4         
		 +beta_9*speed_Limit5         
		 +beta_10*rw_3_less
		 +beta_11*rw_3_55         
		 +beta_12*rw_5_13         
		 +beta_13*lnsTV12h
		 +beta_14*stV12h_dum);   
  
# Expected Crash Funcation for Middle Age Drivers #        
lmy2= exp(beta_15
		 +beta_16*PrefRoad_dum2            
		 +beta_17*Major_PrefRoad_dum                      
		 +beta_18*Others_dum         
		 +beta_19*speed_Limit1         
		 +beta_20*speed_Limit2         
		 +beta_21*speed_Limit3
		 +beta_22*speed_Limit4         
		 +beta_23*speed_Limit5         
		 +beta_24*rw_3_less
		 +beta_25*rw_3_55         
		 +beta_26*rw_5_13         
		 +beta_27*lnsTV12h
		 +beta_28*stV12h_dum); 		
  
# Expected Crash Funcation for Senior Drivers #        
lmy3= exp(beta_29
		 +beta_30*PrefRoad_dum2            
		 +beta_31*Major_PrefRoad_dum                      
		 +beta_32*Others_dum         
		 +beta_33*speed_Limit1         
		 +beta_34*speed_Limit2         
		 +beta_35*speed_Limit3
		 +beta_36*speed_Limit4         
		 +beta_37*speed_Limit5         
		 +beta_38*rw_3_less
		 +beta_39*rw_3_55         
		 +beta_40*rw_5_13         
		 +beta_41*lnsTV12h
		 +beta_42*stV12h_dum); 					
####################################################################
  
  a1u = CDFPG(Young, lmy1 ,1);
  a1l  = CDFPG(Young, lmy1  ,0);

  a2u=CDFPG(Middle_age,lmy2,1);
  a2l=CDFPG(Middle_age,lmy2,0);
  
  a3u=CDFPG(Senior,lmy3,1);
  a3l=CDFPG(Senior,lmy3,0);
  
  
  theta1 =x[43];
  theta2 =x[44];
  theta3 =x[45];
  
  Prob12  =  Frank(a1u,a1l,a2u,a2l,theta1);
  Prob13  =  Frank(a1u,a1l,a3u,a3l,theta2);
  Prob23  =  Frank(a2u,a2l,a3u,a3l,theta3);
  
  	


  # The Bivariate NBII probability density function
  # Defined as the log-likelihood function
  #Possion Probability caluclation@
  # Prob_1 =  Young*log(lmy1)-(lmy1)-lfactorial(Young);
  # Prob_2 =  Middle_age*log(lmy2)-(lmy2)-lfactorial(Middle_age);
  # Prob_3 =  Senior*log(lmy3)-(lmy3)-lfactorial(Senior);
  # Log-likelihood function
  alpha <- 1e-3
  LL <- sum(log(Prob12+alpha)+log(Prob13+alpha)+log(Prob23+alpha))
  #browser()
  
  
  time_taken <<- Sys.time() - start_time

  if(iterate_time %% 100 == 0){
    print(LL)
  print(iterate_time)
  print(time_taken)
  }
  iterate_time <<- iterate_time + 1

  #browser()
  return(LL)

  
}

#start <- matrix(0,nrow=45, ncol = 1)#
# start <- cbind( -3.52323,
#                 0.34214,
#                 0.19620,
#                 0.49018,
#                 0.39374,
#                 0.37504,
#                 0.52828,
#                 0.13558,
#                 0.49041,
#                 0.05295,
#                 0.14552,
#                 -0.03387,
#                 0.34951,
#                 2.02843,
#                 -2.21228,
#                 -0.03798,
#                 0.14580,
#                 0.33770,
#                 0.20034,
#                 0.62577,
#                 0.43807,
#                 0.22905,
#                 0.44474,
#                 -0.08743,
#                 0.07380,
#                 0.02765,
#                 0.35098,
#                 1.95627,
#                 -3.30447,
#                 0.22296,
#                 0.29460,
#                 0.41748,
#                 0.26101,
#                 0.72757,
#                 0.26407,
#                 0.24977,
#                 0.27330,
#                 0.07903,
#                 0.32281,
#                 0.23721,
#                 0.26332,
#                 1.20164,
#                 0.12289,
#                 0.74673,
#                 0.38726,
#                 0.27330,
#                 0.07903,
#                 0.32281,
#                 0.23721,
#                 0.26332,
#                 1.20164,
#                 0.12289,
#                 0.74673,
#                 0.38726)
start <- as.matrix(rbind(as.matrix(parameter1),1.06463353,0.99836471,0.99513005))

# The Start value for the dispersion parameter
OPM <- optim(start,LL,method="BFGS",hessian=TRUE,control = list(fnscale = -1, maxit = 500, factr=1e-2,pgtol=1e-4))

fisher_info<-solve(-OPM$hessian)
prop_sigma<-sqrt(diag(fisher_info))
k<-diag(prop_sigma)
SS<-t(k)
n <- NROW(mydata)
# t-values
t_stat <- (OPM$par)/prop_sigma
upper<-OPM$par+1.96*(diag(SS)/sqrt(n)) 
lower<-OPM$par-1.96*(diag(SS)/sqrt(n))
interval<-data.frame(Betai=OPM$par,Standard_Error=prop_sigma,t_stat, upper=upper, lower=lower)
print(interval)




mle <- maxLik( logLik = LL, start = start,control = c(list(iterlim = 1000)),method = "SANN")

mle2 <- maxBFGS(LL, grad = NULL, hess=NULL, start, fixed = NULL,
        print.level = 0, iterlim = 200, constraints = NULL,
        tol = 1e-08, reltol=tol,
        finalHessian=TRUE,
        parscale=rep(1, length=length(start)))

# SANN, NM,BHHH,BFGS
summary(mle)
G <- solve(-mle$hessian) * mle$gradient * solve(-mle$hessian)
V <- solve(G)
Max_Sandwich <- sqrt(diag(V))
interval2 <- data.frame(betai2=OPM$par,Standard_Er2=Max_Sandwich)
print(interval2)
summary( mle )

# Estimated Parameters
parameter <- mle$estimate

hhh <- mle$hessian

std_err <- sqrt(-diag(solve(hhh)))

# t-values
t_stat <- parameter/std_err

# Initial Log-likelihood
LL0 <- NROW(x)*log(1/3)

# Converged Log-likelihood
LL1 <- OPM$value

# MacFadden's Rho Square
rho <- 1-(LL1/LL0)
rho.adj <- 1-((LL1-length(parameter))/LL0)  

# Display all estimation results
results <- cbind((parameter),(std_err),(t_stat)) #cbind(t(rownames),parameter,std_err, t_stat)

rownames <- c("Constant1          ","PrefRoad_dum       ","PrefRoad_dum2      ","Major_PrefRoad_dum ","Others_dum         ","speed_Limit1       ","speed_Limit2       ","speed_Limit3       ","speed_Limit4       ","speed_Limit5       ","rw_3_less          ","rw_3_55            ","rw_5_13            ","lnsTV12h           ","stV12h_dum         ","Constant2          ","PrefRoad_dum       ","PrefRoad_dum2      ","Major_PrefRoad_dum ","Others_dum         ","speed_Limit1       ","speed_Limit2       ","speed_Limit3       ","speed_Limit4       ","speed_Limit5       ","rw_3_less          ","rw_3_55            ","rw_5_13            ","lnsTV12h           ","stV12h_dum         ","Constant3          ","PrefRoad_dum       ","PrefRoad_dum2      ","Major_PrefRoad_dum ","Others_dum         ","speed_Limit1       ","speed_Limit2       ","speed_Limit3       ","speed_Limit4       ","speed_Limit5       ","rw_3_less          ","rw_3_55            ","rw_5_13            ","lnsTV12h           ","stV12h_dum         ","Frank1         ","Frank2         ","Frank3         ")
 
Goodness_of_fit <- cbind(LL0,LL1,rho,rho.adj)
rownames(Goodness_of_fit) <- c("GoF")
print(results)
print(Goodness_of_fit)




#######################################################################
# Expected Crash Funcation for Young Drivers #
Expect_1= exp(parameter[1]
              +parameter[2]*PrefRoad_dum2            
              +parameter[3]*Major_PrefRoad_dum                      
              +parameter[4]*Others_dum        
              +parameter[5]*speed_Limit1         
              +parameter[6]*speed_Limit2         
              +parameter[7]*speed_Limit3
              +parameter[8]*speed_Limit4         
              +parameter[9]*speed_Limit5         
              +parameter[10]*rw_3_less
              +parameter[11]*rw_3_55         
              +parameter[12]*rw_5_13         
              +parameter[13]*lnsTV12h
              +parameter[14]*stV12h_dum);  

Expect_2= exp(parameter[15]
              +parameter[16]*PrefRoad_dum2            
              +parameter[17]*Major_PrefRoad_dum                      
              +parameter[18]*Others_dum        
              +parameter[19]*speed_Limit1         
              +parameter[20]*speed_Limit2         
              +parameter[21]*speed_Limit3
              +parameter[22]*speed_Limit4         
              +parameter[23]*speed_Limit5         
              +parameter[24]*rw_3_less
              +parameter[25]*rw_3_55         
              +parameter[26]*rw_5_13         
              +parameter[27]*lnsTV12h
              +parameter[28]*stV12h_dum);

Expect_3= exp(parameter[29]
              +parameter[30]*PrefRoad_dum2            
              +parameter[31]*Major_PrefRoad_dum                      
              +parameter[32]*Others_dum        
              +parameter[33]*speed_Limit1         
              +parameter[34]*speed_Limit2         
              +parameter[35]*speed_Limit3
              +parameter[36]*speed_Limit4         
              +parameter[37]*speed_Limit5         
              +parameter[38]*rw_3_less
              +parameter[39]*rw_3_55         
              +parameter[40]*rw_5_13         
              +parameter[41]*lnsTV12h
              +parameter[42]*stV12h_dum);
#######################################################################
summary(cbind(Expect_1,Expect_2,Expect_3))

a1u = CDFPG(Young, Expect_1 ,1);
a1l  = CDFPG(Young, Expect_1  ,0);

a2u=CDFPG(Middle_age,Expect_2,1);
a2l=CDFPG(Middle_age,Expect_2,0);

a3u=CDFPG(Senior,Expect_3,1);
a3l=CDFPG(Senior,Expect_3,0);


theta1 =parameter[43];
theta2 =parameter[44];
theta3 =parameter[45];

Prob12  =  Frank(a1u,a1l,a2u,a2l,theta1);
Prob13  =  Frank(a1u,a1l,a3u,a3l,theta2);
Prob23  =  Frank(a2u,a2l,a3u,a3l,theta3);

summary(cbind(t(a1u),t(a1l),t(a2u),t(a2l)))
summary(cbind(t(Prob12),t(Prob23),t(Prob23)))


# warnings(1:50)







maxBFGS(fn, grad = NULL, hess=NULL, start, fixed = NULL,
        print.level = 0, iterlim = 200, constraints = NULL,
        tol = 1e-08, reltol=tol,
        finalHessian=TRUE,
        parscale=rep(1, length=length(start)), ... )
maxCG(fn, grad = NULL, hess = NULL, start, fixed = NULL,
      print.level = 0, iterlim = 500, constraints = NULL,
      tol = 1e-08, reltol=tol,
      finalHessian=TRUE,
      parscale = rep(1, length = length(start)),
      alpha = 1, beta = 0.5, gamma = 2, ...)
maxSANN(fn, grad = NULL, hess = NULL, start, fixed = NULL,
        print.level = 0, iterlim = 10000, constraints = NULL,
        tol = 1e-08, reltol=tol,
        finalHessian=TRUE,
        cand = NULL, temp = 10, tmax = 10,
        parscale = rep(1, length = length(start)),
        random.seed = 123, ... )
maxNM(fn, grad = NULL, hess = NULL, start, fixed = NULL,
      print.level = 0, iterlim = 500, constraints = NULL,
      tol = 1e-08, reltol=tol,
      finalHessian=TRUE,
      parscale = rep(1, length = length(start)),
      alpha = 1, beta = 0.5, gamma = 2, ...)


















































# Working on the Empirical MVPG Model

lmy1=mean(RE);
lmy2=mean(SS);
ytotal=RE+SS;
LL <- function(x) {
  e <- x[1] # Define the Dispersion Parameter
  # The Bivariate NBII probability density function
  # Defined as the log-likelihood function
  LL12=(lgamma(e+ytotal)-lfactorial(RE)-lfactorial(SS)-lgamma(e)
        +(RE*log(lmy1))-(RE*log(lmy1+lmy2+e))
        +(SS*log(lmy2))-(SS*log(lmy1+lmy2+e))
        +(e*log(e))-(e*log(lmy1+lmy2+e)))
  
  # Log-likelihood function
  L <- sum(LL12)
  return(L)
}

stv <- 0.7709   # The Start value for the dispersion parameter
OPM <- optim(stv,LL,method="BFGS",hessian=TRUE,control=list(maxit=10000, fnscale=-1))
## Estimated parameters
parameter <- OPM$par
## Hessian  (for t-values)
hhh <- OPM$hessian
## t-values
t_stat <- parameter/sqrt(-diag(solve(hhh)))


#########################################################################
# Estiamtion using the library maxlik function
#########################################################################
library("maxLik")

logLikFun <- function(param) {
  e <- param[1]
  LL12=(lgamma(e+ytotal)-lfactorial(RE)-lfactorial(SS)-lgamma(e)
        +(RE*log(lmy1))-(RE*log(lmy1+lmy2+e))
        +(SS*log(lmy2))-(SS*log(lmy1+lmy2+e))
        +(e*log(e))-(e*log(lmy1+lmy2+e)))
  sum(LL12)
}
mle <- maxLik( logLik = logLikFun, start = c( e = 2.3) )
summary( mle )

