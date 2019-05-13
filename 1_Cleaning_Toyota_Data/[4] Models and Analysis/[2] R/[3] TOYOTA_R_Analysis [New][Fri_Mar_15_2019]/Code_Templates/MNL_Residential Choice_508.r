########## Multinomial Logit Model ##########
##### for Existing Residential Location Choice in Hanoi city in 2011 #####
                ##### Household Unit #####
##### Alternatives: urban core, urban frigne and suburbans/ Sample size: 508 HHs #####

#<<<first step>>>
##### Data Reading from csv file #####
  data <- read.csv("LUandHH.csv") 
  names(data)
  summary(data)
#<<<second step>>>
##### Defining Log-likehood function #####
  LL <- function(x) {
  Cuf <- x[1]
  Csb <- x[2]
  ecl <- x[3]
  int2 <- x[4]
  hla <- x[5]
  int3 <- x[6]
  mrcl <- x[7]
  int4 <- x[8]
  prl <- x[9]
  int5 <- x[10]
  int6 <- x[11]
  tsl <- x[12]
  int7 <- x[13]
  cbl <- x[14]
  int1 <- x[15]
  hi_uf <- x[16]
  hi_sb <- x[17]
  Mow_uf <- x[18]
  Mow_sb <- x[19]
  hs_uf <- x[20]
  hs_sb <- x[21]
 
# Dummies (presence of senior people, children or car)
  Dpsm <- ifelse(data$hsm == 0,0,1)
  Dpc <- ifelse(data$hc == 0,0,1)
  Dcar <- ifelse(data$Cown == 0,0,1)
  Dhow <- ifelse(data$hown == 1,1,0)
# Utility function
  Vuc <- 0    + ecl*data$uc2 + int2*data$uc2*Dpc  + hla*data$uc5 + int3*data$uc5*Dpsm + mrcl*data$uc8 + int4*data$uc8*data$hinc + 
          prl*data$uc10 + int5*data$uc10*Dpsm + int6*data$uc10*data$hinc + tsl*data$uc15 + int7*data$uc15*data$Mown + 
          cbl*data$uc1 + int1*data$uc1*data$hinc 
  Vuf <- Cuf  + ecl*data$uf2 + int2*data$uf2*Dpc  + hla*data$uf5 + int3*data$uf5*Dpsm + mrcl*data$uf8 + int4*data$uf8*data$hinc + 
          prl*data$uf10 + int5*data$uf10*Dpsm + int6*data$uf10*data$hinc + tsl*data$uf15 + int7*data$uf15*data$Mown + 
          cbl*data$uf1 + int1*data$uf1*data$hinc + hi_uf*data$hinc + Mow_uf*data$Mown + hs_uf*data$hsize
  Vsb <- Csb + ecl*data$sb2 + int2*data$sb2*Dpc  + hla*data$sb5 + int3*data$sb5*Dpsm + mrcl*data$sb8 + int4*data$sb8*data$hinc + 
          prl*data$sb10 + int5*data$sb10*Dpsm + int6*data$sb10*data$hinc + tsl*data$sb15 + int7*data$sb15*data$Mown + 
          cbl*data$sb1 + int1*data$sb1*data$hinc + hi_sb*data$hinc + Mow_sb*data$Mown + hs_sb*data$hsize
# Denominator
  Sum <- exp(Vuc) + exp(Vuf) + exp(Vsb)
# Probabilities
  Puc <- exp(Vuc)/Sum
  Puf <- exp(Vuf)/Sum       
  Psb <- exp(Vsb)/Sum
# Dummies for choice
  Duc <- ifelse(data$code == 1,1,0)
  Duf <- ifelse(data$code == 2,1,0)
  Dsb <- ifelse(data$code == 3,1,0)
# Log-likelihood function
  L <- sum(Duc*log(Puc) + Duf*log(Puf) + Dsb*log(Psb))
  return(L)
  }
  
 #<<<third step>>>
##### Model Estimation #####
  syokichi <- array(0, dim=c(nrow=21))
  MNL <- optim(syokichi,LL,method="BFGS",hessian=TRUE,control=list(maxit=10000,fnscale=-1))

#<<<fourth step>>>
##### Confirming estimation results #####
# Estimated Parameters
  parameter <- MNL$par
# Hessian for t-values
  hhh <- MNL$hessian
# t-values
  t_stat <- parameter/sqrt(-diag(solve(hhh)))
# Initial Log-likelihood
  LL0 <- NROW(data)*log(1/3)
# Converged Log-likelihood
  LL1 <- MNL$value
# MacFadden's Rho Square
  rho <- 1-(LL1/LL0)
  rho.adj <- 1-((LL1-length(parameter))/LL0)        
# Display all estimation results
  results <- cbind(parameter,t_stat)
  rownames(results) <- c("Cuf","Csb","ecl","int2","hla","int3","mrcl","int4","prl","int5","int6","tsl","int7", 
                             "cbl","int1","hi_uf", "hi_sb","Mow_uf", "Mow_sb", "hs_uf", "hs_sb")
  Goodness_of_fit <- cbind(LL0,LL1,rho,rho.adj)
  rownames(Goodness_of_fit) <- c("GoF")
  print(results)
  print(Goodness_of_fit)
# Export output
  write.csv(results, file="MNL_Results_508HHs.csv")