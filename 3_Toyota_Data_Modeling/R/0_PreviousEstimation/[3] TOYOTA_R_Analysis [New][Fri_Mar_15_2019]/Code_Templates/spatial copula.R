# spatial copula
# final@2018-1-30
# This version is for testing
#----------------------------------------------#
# add negative binomial calculation function
#----------------------------------------------#

library(MASS)
#library(copula)
library(graphics) # for Negative Binomial 2 density function
library(readxl)


#--------------------data preparation------------------------#
mydata <- read_excel("C:/Users/lyy90/OneDrive/Documents/spatial data/20171002area level.xlsx")

# assign the position of variable
VAR_DEP <<- c(7,8)
VAR_LAMBDA1 <<- c(9:12)
VAR_LAMBDA2 <<- c(9:12)
VAR_DISP1 <<- c(20:22)
VAR_DISP2 <<- c(20:22)

COUNT_OBS <<- nrow(mydata)
COUNT_LAMBDA1 <<- length(VAR_LAMBDA1)
COUNT_LAMBDA2 <<- length(VAR_LAMBDA2)
COUNT_DISP1 <<- length(VAR_DISP1)
COUNT_DISP2 <<- length(VAR_DISP2)
COUNT_ZERO <<- 2 # Not necessary
COUNT_PAIR <<- 2 # the parameter assigned to exp(ldisp) for fatigue and nonfatigue


# import weight identified matrix
weightIdenMat <- as.matrix(read.table(file = "C:/Users/lyy90/OneDrive/Documents/spatial data/weightMat.txt",sep = ","))	# import adjacent matrix
#weightIdenMat <- as.matrix(read.table(file = "F:/weightMat.txt",sep = ","))	# import adjacent matrix
weightIdenMat <- weightIdenMat[1:COUNT_OBS,1:COUNT_OBS]
colnames(weightIdenMat) <- c(1:COUNT_OBS)
rownames(weightIdenMat) <- c(1:COUNT_OBS)

weightIdenMat <- weightIdenMat + diag(COUNT_OBS) # add an identification matrix to the original weightIndMat
weightIdenMat[lower.tri(weightIdenMat)]=0 # make weightIdenMat upper triangle matrix
countWeight <<- sum(sum(weightIdenMat))
COUNT_CORR <<- (countWeight - COUNT_OBS)
#print(COUNT_CORR)
countVar <<- COUNT_LAMBDA1 + COUNT_LAMBDA2 + COUNT_DISP1 + COUNT_DISP2 + COUNT_PAIR + 4*COUNT_CORR + COUNT_OBS
#countVar <<- COUNT_LAMBDA1 + COUNT_LAMBDA2 + COUNT_DISP1 + COUNT_DISP2 + COUNT_ZERO + 4*COUNT_CORR + COUNT_OBS

# transform data
names(mydata)[c(4,8:13)] <- c("name","nfatigue","highway","national","province","urban","county")
mydata$highway[mydata$highway < 1] <- 1
mydata$national[mydata$national < 1] <- 1
mydata$province[mydata$province < 1] <- 1
mydata$urban[mydata$urban < 1] <- 1
mydata$county[mydata$county < 1] <- 1

mydata$lhigh <- log(mydata$highway)
mydata$lnation <- log(mydata$national)
mydata$lprov <- log(mydata$province)
mydata$lurban <- log(mydata$urban)
mydata$lcounty <- log(mydata$county)
mydata$lpop <- log(mydata$`resident(ren)`)
mydata$lgdp <- log(mydata$`gdp(wan)`/10000)

#--------------------functions: insure upperbound larger than lowerbound---------------------------#
insureBoundary <- function(Upper, Lower){
	for(i in 1:COUNT_OBS){
		if(Upper[i] > Lower[i]){
			next
		} else if(is.nan(Upper[i])==TRUE | is.nan(Lower[i])==TRUE) {
			stop("upper or lower is NaN")
		} else if(Upper[i] < Lower[i]){
			stop("Lower > Upper")
		}
	}
}

#----------threshold function: NB2--------------------#
calculateNegativeBinomial <- function(parameter, xLambda, xDisp, dependentVar){
	xLambda = as.matrix(xLambda)	# parameter for conditional mean
	xDisp   = as.matrix(xDisp)	# parameter for dispersion variable
	upperY = as.matrix(dependentVar) # n*1 matrix
	lowerY = upperY - 1
	#print(cbind(upperY, lowerY))

	countLambda = ncol(xLambda)	# number of variable for conditional mean
	countDisp = ncol(xDisp)	# number of variable for dispersion variable
	countPair = 1 # fixed coefficent count to 1

	# coefficent
	coefLambda = parameter[1:countLambda] # setting space for estimated parameters of Lambda
	coefDisp = parameter[(countLambda + 1):(countLambda + countDisp)]
	coefPair = parameter[(countLambda + countDisp + countPair)]

	ldisp = xDisp %*% coefDisp	# theta (n*1) & disp>=0
	disp = coefPair * exp(ldisp)
	## FIX ME: lambda is too large!!!!
	lambda = exp(xLambda %*% coefLambda) # calculate conditinal mean (n*1)
	dispU = 1/disp
	prob  = dispU/(dispU+lambda)

	print(cbind(upperY,lowerY,disp,lambda,prob))
	#break
	#--------===---------------------#
	# dnbinom function
	# x = dependentVar
	# size = theta
	# prob = lambda/(lambda + theta)
	#--------------------------------#
	#retUpper = dnbinom(upperY, disp, prob, log=FALSE)
	#retLower = dnbinom(lowerY, disp, prob, log=FALSE)
	
	retUpper = pnbinom(upperY, size=disp, mu=lambda)
	retLower = pnbinom(lowerY, size=disp, mu=lambda)

	#retUpper = pnbinom(upperY, size=disp, prob=prob)
	#retLower = pnbinom(lowerY, size=disp, prob=prob)
	insureBoundary(Upper=retUpper, Lower=retLower)

	# when upperY is zero
	#psi = exp(parameter[countLambda+countDisp+1])*exp(disp)
	#rpsi = 1/psi
	#retZero = rpsi^rpsi/(upperY+rpsi)^rpsi
	#print(psi)
	#print(cbind(upperY, retUpper, retZero)) 

	#retUpper = ifelse(upperY>0, retUpper, retZero)
	#retLower = ifelse(upperY>0, retLower, 0)
 
	retList = data.frame(retUpper,retLower)
	#print(upperY)
	#print(cbind(retList,upperY))
	return(retList)
}

#--------------------copula function-------------------#
# mu1 and mu2: lower limit for y1 and y2
# phi1 and phi2: upper limit for y1 and y2
# xCorrp: the correlation matrix
#------------------------------------------------------#
gumbelCopula <- function(dataset, xCorrP){
	ram = 1e-8
	upper1 = dataset[,1]
	lower1 = dataset[,2]
	upper2 = dataset[,3]
	lower2 = dataset[,4]
	copula = ( exp(((-log(uppe1  + ram))^xCorrP + (-log(upper2 + ram))^xCorrP)^(1/xCorrP)) )
			-( exp(((-log(upper1 + ram))^xCorrP + (-log(lower2 + ram))^xCorrP)^(1/xCorrP)) )
    		-( exp(((-log(lower1 + ram))^xCorrP + (-log(upper2 + ram))^xCorrP)^(1/xCorrP)) )
			+( exp(((-log(lower1 + ram))^xCorrP + (-log(lower2 + ram))^xCorrP)^(1/xCorrP)) )
	
	return(copula)
}

# TODO: bivariate
frankCopula <- function(upper1, lower1, upper2, lower2, xCorrp){
	copula = (-1/xCorrp) * log( 1 + ( (exp(-xCorrp*upper1) - 1) * (exp(-xCorrp*upper2) - 1) ) / (exp(-xCorrp) - 1) )
			-(-1/xCorrp) * log( 1 + ( (exp(-xCorrp*upper1) - 1) * (exp(-xCorrp*lower2) - 1) ) / (exp(-xCorrp) - 1) )
			-(-1/xCorrp) * log( 1 + ( (exp(-xCorrp*lower1) - 1) * (exp(-xCorrp*upper2) - 1) ) / (exp(-xCorrp) - 1) )
			+(-1/xCorrp) * log( 1 + ( (exp(-xCorrp*lower1) - 1) * (exp(-xCorrp*lower2) - 1) ) / (exp(-xCorrp) - 1) )

	return(copula)
}

#-----------------function to converge imput vector in to correlation matrix------#
# parameter: imput parameter matirx
# retCor: pre-defined arrat to store result
# weightIndMat: to identify whether area i and area j is corrlated or not
#---------------------------------------------------------------------------------#
convergeCorrMat <- function(parameter, retCor,  weightIndMat){
	parCross = parameter[1:COUNT_OBS]
	parRho1  = parameter[(COUNT_OBS+1):(COUNT_OBS+COUNT_CORR)]
	parRho2  = parameter[(COUNT_OBS+COUNT_CORR+1):(COUNT_OBS+2*COUNT_CORR)]
	parRho3  = parameter[(COUNT_OBS+2*COUNT_CORR+1):(COUNT_OBS+3*COUNT_CORR)]
	parRho4  = parameter[(COUNT_OBS+3*COUNT_CORR+1):(COUNT_OBS+4*COUNT_CORR)]

	for(i in 1:COUNT_OBS){
		for(j in 1:COUNT_OBS){
			if(i == j){
				retCor[i,j,1] = parCross[i]
			}else{
			 	retCor[i,j,1] = ifelse(weightIndMat[i,j] == 1, parRho1[i], NaN)
				retCor[i,j,2] = ifelse(weightIndMat[i,j] == 1, parRho2[i], NaN)
				retCor[i,j,3] = ifelse(weightIndMat[i,j] == 1, parRho3[i], NaN)
				retCor[i,j,4] = ifelse(weightIndMat[i,j] == 1, parRho4[i], NaN)
			}
		#j = j+1	
		}
	#i = i+1	
	}
	return(retCor)
	#print(retCor)
}

#----------------------Component Maximum Likelihood------------------#
# This function is for calculating bivariate spatial NB2 copula model 
# likelihood function.
# parameter: starting value for xCorrp;
# dataset: the original dataset for NB2
#--------------------------------------------------------------------#
#retProbMat <- matrix(rep(0, COUNT_OBS*COUNT_OBS), COUNT_OBS, COUNT_OBS)  # generate a matrix to store the probability of copula function for [i,j]
#retCor <<- array(rep(NaN, 120*120*4), c(120, 120, 4))

calculateSpatialCopula <- function(parameter, dataset, weightIdenMat){
	# STEP1-negative binomial 2
	xLambda1 = dataset[,VAR_LAMBDA1] # FIXME
	xLambda2 = dataset[,VAR_LAMBDA2] # FIXME
	xDisp1 = dataset[,VAR_DISP1]
	xDisp2 = dataset[,VAR_DISP2]
	dependentVar = dataset[,VAR_DEP]

	#parameter = rep(0, countVar)
	parLambda1 = parameter[1:COUNT_LAMBDA1]
	parLambda2 = parameter[(COUNT_LAMBDA1+1):(COUNT_LAMBDA1+COUNT_LAMBDA2)]
	parDisp1  = parameter[(COUNT_LAMBDA1+COUNT_LAMBDA2+1):(COUNT_LAMBDA1+COUNT_LAMBDA2+COUNT_DISP1)]
	parDisp2  = parameter[(COUNT_LAMBDA1+COUNT_LAMBDA2+COUNT_DISP1+1):(COUNT_LAMBDA1+COUNT_LAMBDA2+COUNT_DISP1+COUNT_DISP2)]
	parPair1 = parameter[(COUNT_LAMBDA1+COUNT_LAMBDA2+COUNT_DISP1+COUNT_DISP2 + 1)]
	parPair2 = parameter[(COUNT_LAMBDA1+COUNT_LAMBDA2+COUNT_DISP1+COUNT_DISP2 + 2)]
	#parZero    = parameter[(COUNT_LAMBDA1+COUNT_LAMBDA2+COUNT_DISP1+COUNT_DISP2+1):(COUNT_LAMBDA1+COUNT_LAMBDA2+COUNT_DISP1+COUNT_DISP2+2)]
	parCorr = parameter[(COUNT_LAMBDA1+COUNT_LAMBDA2+COUNT_DISP1+COUNT_DISP2+3):countVar]

	parY1 = c(parLambda1, parDisp1, parPair1)
	parY2 = c(parLambda2, parDisp2, parPair1)
	y1 = calculateNegativeBinomial(parY1, xLambda1, xDisp1, dependentVar[,1])
	y2 = calculateNegativeBinomial(parY2, xLambda2, xDisp2, dependentVar[,2])
	print(cbind(y1,y2))
	
	#stop()
	# STEP2-copula function
	upper1 = y1[,1]
	lower1 = y1[,2]
	upper2 = y2[,1]
	lower2 = y2[,2]

	# weight matrix import and identification
	retCor = array(rep(NaN, COUNT_OBS*COUNT_OBS*4), c(COUNT_OBS, COUNT_OBS, 4))
	#print(retCor)
	xCorrp = convergeCorrMat(parCorr, retCor, weightIdenMat)
	retProbMat = matrix(rep(0, COUNT_OBS*COUNT_OBS), COUNT_OBS, COUNT_OBS)  # generate a matrix to store the probability of copula function for [i,j]
	


  # STEP3-Likelihood function
  for(i in 1:COUNT_OBS){
    for(j in 1:COUNT_OBS){
      # when j>= i, skip (upper triangle)
      if(j < i) {
        next}
      # if weight==0, skip
      if(weightIdenMat[i,j] != 1){
        retProbMat[i,j] = 0
        next
      }
      # if i = j
      if(i == j){
        innerProb = frankCopula(upper1[i], lower1[i], upper2[i], lower2[i], xCorrp[i,i,1]) # y1i, y2i
        innerProb = ifelse(innerProb!=0, innerProb, 0.000000001)
        innerProb = log(innerProb)
        #innerProb = innerProb + log(innerProb)
        #print(innerProb)
        retProbMat[i,j] = innerProb
      }else{ 
      # if i != j
        outerProb1 = frankCopula(upper1[i], lower1[i], upper1[j], lower1[j], xCorrp[i,j,1]) # y1i, y1j
        outerProb2 = frankCopula(upper1[i], lower1[i], upper2[j], lower2[j], xCorrp[i,j,2]) # y1i, y2j
        outerProb3 = frankCopula(upper2[i], lower2[i], upper1[j], lower1[j], xCorrp[i,j,3]) # y2i, y1j
        outerProb4 = frankCopula(upper2[i], lower2[i], upper2[j], lower2[j], xCorrp[i,j,4]) # y2i, y2j
        #outerProb = c(outerProb1, outerProb2, outerProb3, outerProb4)
        outerProb = c(log(outerProb1), log(outerProb2), log(outerProb3), log(outerProb4))
        print(outerProb)
        outerProb = sum(outerProb)
        outerProb = ifelse(outerProb!=0, outerProb, 0.000000001)
        retProbMat[i,j] = outerProb
        #browser()
      }
      #print(retProbMat)
      #browser()
    }
  }
	
	llk = sum(sum(retProbMat))
	#print(llk)
	#stop("checking")
}

# starting value
# order for starting value: (lambda1, lambda2, theta1, theta2, zero(when upperY==0), corr)
#lengthPar <- COUNT_LAMBDA1 + COUNT_LAMBDA2 + COUNT_DISP1 + COUNT_DISP2 + 2 + 4*COUNT_CORR + COUNT_OBS


# starting value for estimation
startValue_Lambda1 <- rep(0.001, COUNT_LAMBDA1)
startValue_Lambda2 <- rep(0.0001, COUNT_LAMBDA2)
startValue_Disp1   <- rep(0.5, COUNT_DISP1)
startValue_Disp2   <- rep(0.5, COUNT_DISP2)
startValue_Pair    <- c(0.1, 0.1)
startValue_Corr    <- rep(0.6, COUNT_OBS)
startValue_Rho1    <- rep(0.5, COUNT_CORR)
startValue_Rho2    <- rep(0.5, COUNT_CORR)
startValue_Rho3    <- rep(0.5, COUNT_CORR)
startValue_Rho4    <- rep(0.5, COUNT_CORR)
#startValue <- c(startValue_Lambda1, startValue_Lambda2, startValue_Disp1, startValue_Disp2,
#	startValue_Zero, startValue_Corr, startValue_Rho1, startValue_Rho2, startValue_Rho3, 
#	startValue_Rho4)
startValue <- c(startValue_Lambda1, startValue_Lambda2, startValue_Disp1, startValue_Disp2, startValue_Pair,
	startValue_Corr, startValue_Rho1, startValue_Rho2, startValue_Rho3, startValue_Rho4)
#startValue <- c(rep(0.01,lengthPar))

estimationLower <- c(rep(-2^5, countVar))
estimationUpper <- c(rep( 2^5, countVar)) 

set.seed(123515)
getEstimationResult <- optim(startValue, calculateSpatialCopula, 
							method="L-BFGS-B", hessian=TRUE,
							control=list(fnscale=-1,trace=3),
							dataset=mydata,
							weightIdenMat = weightIdenMat,
							lower=estimationLower,
							upper=estimationUpper)

#------------print the result---------------------#
print(getEstimationResult)
	
#degreeFreedom  <- COUNT_OBS - length(getEstimationResult$par) # degree of freedom
#standardError  <- sqrt(diag(abs(solve(getEstimationResult$hessian))))  # standard error
#tValue   <- getEstimationResult$par/standardError # t value
#pValue   <- (1-pt(abs(tValue),degreeFreedom))*1.96 # p value

#displayResult <- cbind(getEstimationResult$par, standardError, tValue, pValue)
#print(displayResult, digits = 3) # Displays the coefficients and standard errors of the parameters
