# Binary-Ordered Probit Code
# Final@2017-2-27


library(MASS)
library(foreign)


GENERALIZED_ORDER_PROBIT <- FALSE

# Generate a dataset
# Sample Commit
# Sample Commit 2
# aaa
n <- 5000
e1 <- rnorm(n) #hita
e2 <- rnorm(n) #ksi
e3 <- rnorm(n) #mu
x1 <- matrix(data = rnorm(n),nrow = n, ncol = 1 )
x2 <- matrix(data = rnorm(n),nrow = n, ncol = 1 )
z1 <- matrix(data = rnorm(n),nrow = n, ncol = 1 )
z2 <- matrix(data = rnorm(n),nrow = n, ncol = 1 )

a1 <- 0.5 #alpha
a2 <- 0.2 #alpha
a3 <- 0.8 #theta
a4 <- -0.5 #lambda

b <- 1
c1 <- 0.5
c2 <- -0.5

# Thesholds for BOPROBIT and GBOPROBIT
if(GENERALIZED_ORDER_PROBIT==TRUE){
	m1 <- matrix(data = rnorm(n),nrow = n, ncol = 1 )
	m2 <- matrix(data = rnorm(n),nrow = n, ncol = 1 )
	iota <- 0.5
	gam1 <- 0.2
	gam2 <- -0.5
	
	cut1 <- 0
	cut2 <- cut1 + exp(gam1*m1 + gam2*m2)
	cut3 <- cut2 + exp(gam1*m1 + gam2*m2)
	
	fatig <- b + c1*z1 + c2*z2 + e3 + e2
	y2 <- ifelse(fatig<=0,0,1)
	
	inj <- a1*x1 + a2*x2 + a3*y2 + a4*e3 + e1
	inj <- (inj <= cut1)*1 + (inj > cut1 & inj <= cut2)*2 + (inj > cut2 & inj <= cut3)*3 + (inj > cut3)*4

	fatig <- y2
	
	mydata <- data.frame(inj,fatig,x1,x2,z1,z2,m1,m2)
	
} else {
	cut1 <- 0
	cut2 <- 1
	cut3 <- 2

	fatig <- b + c1*z1 + c2*z2 + e3 + e2
	y2 <- ifelse(fatig<=0,0,1)

	inj <- a1*x1 + a2*x2 + a3*y2 + a4*e3 + e1
	inj <- (inj <= cut1)*1 + (inj > cut1 & inj <= cut2)*2 + (inj > cut2 & inj <= cut3)*3 + (inj > cut3)*4

	fatig <- y2

	mydata <- data.frame(inj,fatig,x1,x2,z1,z2)
}


# Likelihood function
boprobit <- function(param, dat){

	# assign which part of data should be used in this model
	inj <- dat[,1]
	fatig <- dat[,2]
	x <- dat[,c(3:4,2)]
	z <- dat[,5:6]
	
	
	z <- cbind(1, z) # add an constant vector to Eq2
	
	# storage of parameters
	alpha <- as.matrix(param[1:ncol(x)])
	bet <- as.matrix(param[ (ncol(x)+1) : (ncol(x)+3) ])
	ramda <- param[ncol(x)+4]
	
	if(GENERALIZED_ORDER_PROBIT==TRUE){
		m <- dat[,7:8]
		
		iota <- param[ncol(x)+5]
		gam <- as.matrix(param[ (ncol(x)+6) : (ncol(x)+7) ])
		cut1 <- 0
		cut2 <- cut1 + exp( iota + gam[1]*m[,1] + gam[2]*m[,2] )
		cut3 <- cut2 + exp( iota + gam[1]*m[,1] + gam[2]*m[,2] )
		
		cut2 <- as.matrix(cut2)
		cut3 <- as.matrix(cut3)
	} else {
		cut1 <- param[ncol(x)+5]
		cut2 <- param[ncol(x)+6]
		cut3 <- param[ncol(x)+7]
	}
	
	
	# likelihood
	miu <- rnorm(nrow(x),mean = 0, sd = 1) # generate common error term
	#print(x)
	xa  <- as.matrix(x)%*%alpha
	
	inj_star <- xa + ramda*miu
	
	zb  <- as.matrix(z)%*%bet
	fatig <- zb + miu
	
	cut1_inj_star = cut1-inj_star
	cut2_inj_star = cut2-inj_star
	cut3_inj_star = cut3-inj_star
	
	# probability of Eq1
	p11 = pnorm(cut1_inj_star)	# Injury==1
	p12 = pnorm(cut2_inj_star) - pnorm(cut1_inj_star)
	p13 = pnorm(cut3_inj_star) - pnorm(cut2_inj_star)
	p14 = 1 - pnorm(cut3_inj_star)
	
	if(GENERALIZED_ORDER_PROBIT==FALSE){
		if(cut2 <= cut1){ p12 <- -10000 }
		if(cut3 <= cut2){ p13 <- -10000 }
	}
			
	ll_1 <- (inj==1)*log(p11) + (inj==2)*log(p12) + (inj==3)*log(p13) + (inj==4)*log(p14)
	
	
	#probability of Eq2
	p21 <- pnorm(fatig)
	ll_2 <- log(fatig*(p21) + (1-fatig)*(1-p21))
	
	ll <- ll_1 + ll_2
	print(iota)
	
	return(-sum(ll))
}
	

# Set starting value
if(GENERALIZED_ORDER_PROBIT==TRUE){
	ls_inj <- lm(inj ~ x1 + x2 + fatig) # generate initial values for Eq1
	ls_fatig <- lm(fatig ~ z1 + z2) # generate initial values for Eq2
	stval_alpha <- as.matrix(ls_inj$coefficients)[2:3]
	stval_bet <- as.matrix(ls_fatig$coefficients)
	#stval <- c(stval_alpha, 1, stval_bet, 0.5, 0.3, 0.25, 0)
	stval <- c(0.5, 0.1, 0.7, 1, 0, 1, 0, 0, 0, 0)
	print(stval)

} else {
	# oprobit <- polr(inj ~ x1 + x2 + fatig, data = mydata, method="probit", Hess=TRUE)
	# print(o_inj)
	ls_inj <- lm(inj ~ x1 + x2 + fatig) # generate initial values for Eq1
	ls_fatig <- lm(fatig ~ z1 + z2) # generate initial values for Eq2

	#stval <- c(ls_inj$coefficients,1, ls_fatig$coefficients,1,1:3,1)
	stval_alpha <- as.matrix(ls_inj$coefficients)[2:3]
	stval_bet <- as.matrix(ls_fatig$coefficients)
	stval <- c(stval_alpha, 1, stval_bet, 1, 0, 1, 2)
	#stval <- c(0.5, 0.1, 0.7, -0.5, 0, 1, 2, 1, 0.5, -0.5)
}


# use optim to do MLE
result1 <- optim(stval, boprobit, dat = mydata, method="BFGS", hessian = TRUE) # Estimate the model
print(result1)

# display results
df <- length(inj) - length(result1$par) # degree of freedom
se <- sqrt(diag(abs(solve(result1$hessian))))  # standard error
print(se)
t <- result1$par/se # t value
p <- (1-pt(abs(t),df))*1.96 # p value

display1 <- cbind(result1$par,se,t,p)
#display1(colnames) <- c('b', 'se', 't-value', 'p-value')
#display1(rownames) <- c('inj_x1', 'inj_x2', 'fat_con', 'z1', 'z2', 'ramda', 'cu1', 'cut2', 'cut3')
print(display1, digits = 3) # Displays the coefficients and standard errors of the parameters