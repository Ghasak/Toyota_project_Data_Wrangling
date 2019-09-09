# This program estimates a bivariate binary-ordered probit model
# Commercial and Non-Commercial
# Final@2017-04-03
# By liyanyan

##Note on modifying###
##1.non-commercial vehicle drop insignificant variables(2017-04-03)##

library(MASS)
library(foreign)
library(mvtnorm)
library(optim)
library(maxLik)
#library(ggplot2)

set.seed(12315)

# If TEST_DATA = TRUE, use sample data for model testing
# If TEST_DATA = FALSE, use your own data for model testing
TEST_DATA = TRUE
# If commercial vehicle driver, set COMMERCIAL=TRUE
# If commercial vehicle driver, set COMMERCIAL=FALSE
COMMERCIAL = TRUE

#Generating data to test the model
if(TEST_DATA == TRUE){
	
	n <- 1000								
	x1 <- rnorm(n)
	x2 <- rnorm(n)
	sig <- diag(2)
	sig[1,2] <- sig[2,1] <- .5
	mu <- c(0,0)

	e <- rmvnorm(n,mu,sig)
	a <- .5
	b <- .2
	c <- -.2
	d <- -.9

	y1 <- b*x1+e[,1]
	y2 <- c+d*x2+e[,2]

	y1 <- (y1 <= 0)*1 + (y1 > 0 & y1 <= 1)*2  + (y1 > 1)*3
	y2 <- (y2 <= 0)*0 + (y2 > 0)*1

	mydata <- cbind(y1,y2,x1,x2)
	mydata <- as.data.frame(mydata)
	#write.dta(mydata, file="/Users/tiernay/Desktop/probit/bioprobit_r.dta")

	y1.start <- as.factor(y1)
	y2.start <- as.factor(y2)

} else {

	mydata <- read.csv("D:/road_safety/fatigue/20170301data.csv")
	#mydata <- read.csv("C:/Users/liyanyan/Desktop/matlab/fatigue/20170301data.csv")
	if(COMMERCIAL==TRUE){
		mydata <- subset(mydata, mydata$ope_y==1)
		y1 <- mydata[,1]    # inj
		y2 <- mydata[,2]    # fatig
		x1 <- mydata[,c(3:21)]   # variable for inj
		x2 <- mydata[,c(22:31)]  # variable for fatig
		x1 <- x1[,c(-5,-8:-12,-16)] #drop ope_y variable
		x2 <- x2[,c(-1,-3,-6:-8)] #drop ope_y variable
		
	}else{
		mydata <- subset(mydata, mydata$ope_y==0)
		#mydata <- mydata[1:2000,]
		# Data preperation
		y1 <- mydata[,1]    # inj
		y2 <- mydata[,2]    # fatig
		x1 <- mydata[,c(3:21)]   # variable for inj
		x2 <- mydata[,c(22:31)]  # variable for fatig
		x1 <- x1[,c(-5,-15)] #drop ope_y variable
		x2 <- x2[,c(-2,-3,-5,-6,-7,-8)] #drop ope_y variable
	}
	

}

names(x1)
names(x2)

# starting time
begin_time <- Sys.time()

iterate_time <<- 0


# The bivariate ordered probit function
log.lik <- function(par , X1 , X2 , Y1 , Y2) {
	start_time <- Sys.time()
	#X1 <- cbind(1,X1)
	X1 <- as.matrix(X1)
	X2 <- as.matrix(cbind(1,X2))

	Beta1 <- par[1:ncol(X1)]		#parameters for the first equation
	Beta2 <- par[(ncol(X1)+1):(ncol(X1)+ncol(X2))]   #parameters for the second equation
	
	# set threshold for first equation
	if(TEST_DATA==TRUE){
		cut1 <- par[ncol(X1) + ncol(X2) + 1]	#Second cut point for the first equation
		cut2 <- par[ncol(X1) + ncol(X2) + 2]
		gamma <- par[ncol(X1) + ncol(X2) + 3]	
	}else{
		cut1 <- par[ncol(X1) + ncol(X2) + 1]	#Second cut point for the first equation
		cut2 <- par[ncol(X1) + ncol(X2) + 2]
		cut3 <- par[ncol(X1) + ncol(X2) + 3]
		gamma <- par[ncol(X1) + ncol(X2) + 4]	  #parameter for the correlation coefficient
	}
	
	

	#multiply gamma by a column of 1's, and then transform: (exp(rho)-1)/(1+exp(rho))
	rho <- (exp(gamma) - 1) / (1 + exp( gamma)) 

	mu1 <- as.matrix(X1) %*% Beta1
	mu2 <- as.matrix(X2) %*% Beta2
	
	llik <- 0

	if(TEST_DATA==TRUE){
		cut_y1 <- c(-10000, as.double(cut1), as.double(cut2), 10000)
		cut_y2 <- c(-10000, 0, 10000)
	}else{
		cut_y1 <- c(-10000, as.double(cut1), as.double(cut2), as.double(cut3), 10000)
		cut_y2 <- c(-10000, 0, 10000)
	}

	
	for (i in 1:nrow(mu1)){
		Sigma <- matrix(c(1, rho, rho, 1), 2, 2) 
		cut_left <- cut_y1[Y1[i]]
		cut_right <- cut_y1[Y1[i]+1]
		cut_down <- cut_y2[Y2[i]+1]
		cut_up <- cut_y2[Y2[i]+2]
		#print(pmvnorm(lower = c(cut_left, cut_down), upper = c(cut_right, cut_up), mean = c(mu1[i,], mu2[i,]), corr = Sigma))
		llik <- llik + log(pmvnorm(lower = c(cut_left, cut_down), upper = c(cut_right, cut_up), mean = c(mu1[i,], mu2[i,]), corr = Sigma))
		#print(llik)
	}
	
	
	time_taken <<- Sys.time() - start_time
	
	if(iterate_time %% 10 == 0){
		print(llik)
	}
	iterate_time <<- iterate_time + 1
	print(iterate_time)
	print(time_taken)
	
	return(llik)
}
 





# Generate starting values with an ordinary probit
if(TEST_DATA==TRUE){
	op.result1 <- polr(y1.start ~ x1, method=c("probit"))
	#op.result2 <- polr(y2.start ~ x2, method=c("probit"))
	op.result2 <- glm(y2.start ~ x2, family=binomial(link="probit"), data=mydata)
	start.val <- c(op.result1$coef[1],op.result2$coef,op.result1$zeta,0) 
	
}else{

	if(COMMERCIAL==TRUE){
		op.result1 <- polr(as.factor(inj1) ~ iso_y + ins + lic_no + terrain_head +  light_ngt_y + light_ngt_n + form_tag + form_head + form_side + roadtype_exp + roadtype_u + fatig, data=mydata, method = "probit")

		op.result2 <- glm(fatig ~  terrain_head.1  + time0006 + time0708 + roadtype_exp.1 + roadtype_u.1, family=binomial(link="probit"), data=mydata)
		
		start.val <- c(op.result1$coefficients, op.result2$coef, op.result1$zeta, -0.5)
	}else{
		# drop form_side in 'injury equation'
		op.result1 <- polr(as.factor(inj1) ~ iso_y + ins + lic_no + terrain_head +  light_ngt_y + light_ngt_n + age2635 + age4655 + age5665 + age6600 + gender_m + form_tag + form_head + driexp0002 + roadtype_exp + roadtype_u + fatig, data=mydata, method = "probit")
		# drop terrain_head, time 0708, time1719, light_*
		op.result2 <- glm(fatig ~ ins.1 + time0006 + roadtype_exp.1 + roadtype_u.1, family=binomial(link="probit"), data=mydata)
		
		start.val <- c(op.result1$coefficients, op.result2$coef, op.result1$zeta, -0.5)
	}
	
}

if(TEST_DATA==TRUE){

	lower_1 = c(-Inf, -Inf, -Inf, -2, -2, -2)
	upper_1 = c(Inf, Inf, Inf, 3, 3, 2)

}else{
	if(COMMERCIAL==TRUE){
		lower_1 = c(rep(-Inf, 26), -2, -2, -2, -2)
		upper_1 = c(rep(10, 26), 3, 3, 3, 2)
		
	}else{
		#lower_1 = c(rep(-Inf, 26), -2, -2, -2, -2)
		lower_1 = rep(-3, 26)
		#upper_1 = c(rep(3, 26), 3, 3, 3, 2)
		upper_1 = rep(3, 26)
	}
	

}


res <- optim(start.val, log.lik, method = "L-BFGS-B", hessian = TRUE, control = list(fnscale = -1, maxit = 500, factr=1e-2,pgtol=1e-4), X1 = x1, X2 = x2, Y1 = y1, Y2 = y2, lower = lower_1, upper = upper_1) 
#res <- maxLik(log.lik, start = start.val, control = c(list(iterlim = 100)), X1 = x1, X2 = x2, Y1 = y1, Y2 = y2) 

# End time
end_time <- Sys.time()
iteration_time <- end_time - begin_time

print(res)

#calculate rho
rho.convert <- function(gamma){
	rho <- (exp(gamma) - 1) / (1 + exp( gamma)) 
	return(rho)
}

if(COMMERCIAL==TRUE){
	rho <- rho.convert(res$par[4])	 	# Return the correlation coefficint
}else{
	rho <- rho.convert(res$par[26])	 	# Return the correlation coefficint
}

	
df  <- length(mydata$inj1) - length(res$par) # degree of freedom
se  <- sqrt(diag(abs(solve(res$hessian))))  # standard error
t   <- res$par/se # t value
p   <- (1-pt(abs(t),df))*1.96 # p value

# calculate AIC
# AIC = - 2*llk + 2 * length(par)
# BIC = - 2*llk + log(n) * length(par)
AIC <- -2*res$value + 2 * (length(res$par) + 2)
BIC <- -2*res$value + log(length(mydata)) * (length(res$par) + 2)

# display all the results
display1 <- cbind(res$par, se, t, p)
display1 <- rbind (display1)
display2 <- c(rho, AIC, BIC, res$value)
print(display1, display2, digits = 3) # Displays the coefficients and standard errors of the parameters
print(iteration_time)
eigen(-res$hessian)
