#Nested Logit model with covariance hecterogeneity
#By Chu Tien Dung
##################################################

#Load the data
setwd('~/Dropbox/Zhengyan/MNL/R')
x = read.csv('~/Dropbox/Zhengyan/MNL/R/dataR.csv',header = TRUE)
attach(x)
names(x)
summary(x)

##### Defining Log-likehood function #####

para <-function(b) {
  Constantdr	<-	b[1]
  Househ	<-	b[2]
  Currentmode	<-	b[3]
  Donotdrive	<-	b[4]	
  Drivethreetimes	<-	b[5]
  Freqgoingshoping	<-	b[6]
  Visithospital	<-	b[7]
  Haveformworkdr	<-	b[8]
  Expcarry	<-	b[9]	
  Constant	<-	b[10]	
  Male	<-	b[11]
  Youngage	<-	b[12]	
  Student	<-	b[13]	
  Agricultrure	<-	b[14]	
  Lowhouseholdincome	<-	b[15]	
  Haveformworkrider	<-	b[16]
  Expride	<-	b[17]	
 	

#Utility function
  V1<- Constantdr + Househ*(ifelse(x[,1]==1,1,0)) + Currentmode*(x[,7]) + Donotdrive*(ifelse(x[,21]==0,1,0)) + Drivethreetimes*(ifelse((x[,21]>=1)&(x[,21]<=2),1,0)) + Freqgoingshoping*(ifelse(x[,22]==2,1,0)) + Visithospital*(ifelse(x[,31]<=2,1,0)) + Haveformworkdr*(ifelse(x[,36]==2,1,0)) + Expcarry*(ifelse(x[,40]==2,1,0))

  V2<- Constant + Male*(ifelse(x[,2]==1,1,0)) + Youngage*(ifelse(x[,3]<65,1,0)) + Student*(ifelse(x[,4]==3,1,0)) + Agricultrure*(ifelse(x[,4]==6,1,0)) + Lowhouseholdincome*(ifelse(x[,5]<=3,1,0)) + Haveformworkrider*(ifelse(x[,36]==2,1,0)) + Expride*(ifelse(x[,49]==2,1,0))

  V3 <- 0

  
  #Probability

  E1 		<- exp(V1)
  E2		<- exp(V2)
  E3 		<- exp(V3)
  sumE  <- E1+E2+E3

  P1 		<- E1/sumE  	#Prob of selecting "want to be driver" of branch 1
  P2 		<- E2/sumE  	#Prob of selecting "want to be rider" of branch 1
  P3 		<- E3/sumE 		#Prob of selecting "Not parcitipate" of branch 2

#Log-likelihood
  LL <- sum((ifelse(x[,58]==2,1,0))*log(P1)+(ifelse(x[,58]==3,1,0))*log(P2)+(ifelse(x[,58]==1,1,0))*log(P3))
  return(LL)
}

#Initial values
start <- matrix(0,nrow=17, ncol = 1)
#start <- array(0, dim=c(nrow=23))

#Run maximum likelihood
res <- optim(start,para,gr=NULL,method="BFGS",hessian=TRUE,control=list(maxit=100000,fnscale=-1))

# Estimated Parameters
parameter <- res$par

hhh <- res$hessian

std_err <- sqrt(-diag(solve(hhh)))

# t-values
t_stat <- parameter/std_err

# Initial Log-likelihood
LL0 <- NROW(x)*log(1/3)

# Converged Log-likelihood
LL1 <- res$value

# MacFadden's Rho Square
rho <- 1-(LL1/LL0)
rho.adj <- 1-((LL1-length(parameter))/LL0)  

# Display all estimation results
results <- cbind(parameter,std_err, t_stat)

rownames(results) <- c("Constantdr","Househ","Currentmode","Donotdrive","Drivethreetimes","Freqgoingshoping","Visithospital","Haveformworkdr","Expcarry","Constant","Male","Youngage","Student","Agricultrure","Lowhouseholdincome","Haveformworkrider","Expride")

Goodness_of_fit <- cbind(LL0,LL1,rho,rho.adj)
rownames(Goodness_of_fit) <- c("GoF")
print(results)
print(Goodness_of_fit)

# Export output
write.csv(results, file='~/Dropbox/Zhengyan/MNL/R/Results1.csv')
