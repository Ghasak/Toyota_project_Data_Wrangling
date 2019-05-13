########### Ordered Probit Model ########
#### for Car Ownership in Hanoi city in 2011#####
        ##### Household Unit ######
##### Sample size: 508 HHs #####
## Y=0 (419 HHs - 82.48%); Y=1 (74 HHs - 14.56%); Y= 2+ (15 HHs - 2.95%)

#<<<first step>>>
##### Data Reading from csv file #####
  data <- read.csv("HHandBEadd.csv")
  names(data)
  summary(data)
#<<<second step>>>
##### Defining the Log-likelihood function #####
  LL <- function(x) {
  Const <- x[1]
  hhi <- x[2]  # Household characteristics
  mhi <- x[3]
  nsm <- x[4]
  nc <- x[5]
  nws <- x[6]
  ncd <- x[7]
  ruc <- x[8]  # Residential characteristics
  rsb <- x[9]
  bst <- x[10]
  bli <- x[11]   
  thr1 <- x[12]
 
# Dummies
  Dhhi <- ifelse(data$hinc >= 20,1,0)  #whether high income or not
  Dhow <- ifelse(data$hown == 1,1,0) #whether own house or not
  Dcow <- ifelse(data$Cown == 1,0,1) #whether own car or not
  Dmhi <- ifelse(data$hinc >5 & data$hinc <20,1,0) #whether middle income or not
  Dcwc <- ifelse(data$hcom == 3,1,0) #whether couple with children
  Dlhi <- ifelse(data$hinc <= 5,1,0) #whether low income or not
  Druc <- ifelse(data$code == 1,1,0) #whether residence is located in urban core or not
  Drsb <- ifelse(data$code == 3,1,0) #whether residence is located in suburban or not
# Utility function
      Uco <- Const + hhi*Dhhi + mhi*Dmhi + nsm*data$hsm + nc*data$hc + nws*data$hws + ncd*data$hcld +
                 ruc*Druc + rsb*Drsb + bst*data$dbs + bli*data$dbl
                  
# Choice Probabilites
      PP0 <- pnorm(-Uco)
      PP1 <- pnorm(thr1*thr1-Uco)- pnorm(-Uco)
      PP2 <- 1 - pnorm(thr1*thr1-Uco)
# Dummies for choice
  Dzero <- ifelse(data$Cown == 1,1,0)     #no car#
  Done <- ifelse(data$Cown == 2,1,0)      #one car#
  Dtwo <- ifelse(data$Cown >= 3,1,0)      #two or more cars#
 
# Log-likelihood function
  L <- sum(Dzero*log(PP0) + Done*log(PP1) + Dtwo*log(PP2))
  return(L)
}

#<<<third step>>>
##### Model Estimation #####
   stv <- c(0,0,0,0,0,0,0,0,0,0,0,1)
   OPM <- optim(stv,LL,method="BFGS",hessian=TRUE,control=list(maxit=10000, fnscale=-1))

#<<<fourth step>>>
## Estimated parameters
  parameter <- OPM$par
## Hessian  (for t-values)
  hhh <- OPM$hessian
## t-values
  t_stat <- parameter/sqrt(-diag(solve(hhh)))
## initial log-likelihood
  a <- c(0,0,0,0,0,0,0,0,0,0,0,parameter[12])
  LL0 <- LL(a)
## converged log-likelihood
  LL1 <- OPM$value
## McFadden's Rho squere
  rho     <- 1-(LL1/LL0)
  rho.adj <- 1-((LL1-length(parameter))/LL0)       
# Display all estimation results
  results <- cbind(parameter,t_stat)
  rownames(results) <- c("Const","hhi","mhi","nsm","nc","nws","ncd","ruc","rsb","bst","bli","thr1")
  Goodness_of_fit <- cbind(LL0,LL1,rho,rho.adj)
  rownames(Goodness_of_fit) <- c("GoF")
  print(results)
  print(Goodness_of_fit)

# Export output
  write.csv(results, file="OPM_Car ownership_508HHs.csv")