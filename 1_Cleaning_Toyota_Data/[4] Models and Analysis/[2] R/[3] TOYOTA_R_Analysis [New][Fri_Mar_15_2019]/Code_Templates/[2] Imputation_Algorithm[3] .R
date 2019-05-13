##########################################################################
dev.off(dev.list()["RStudioGD"]) # clean the Graph Area
rm(list=ls())                    # clean the Workspace (dataset)
cat("\014")                      # clean the console area
graphics.off()                   # close graphics windows (For R Script)
#########################################################################
#library(tcltk)
#X <- read.csv(tk_choose.files(caption = "Choose X"))
Data <- read.csv(file.choose())
library(tmvtnorm)
# Random number generation
set.seed(123)

#Data Input
Gender= Data[,2]
RDVAR = Data[,3]  # Reported distance
mu1   = Data[,4]
mu2   = Data[,5]

mu_male  =  c(6.45,0.51)
mu_femal =  c(6.25,0.32)
Draws = 1000  # Number of draws from the bivariate normal distribution
VCMatrix= matrix(c(0.51, 0.56, 0.56, 1.00), 2, 2)
#X = matrix(0,length(RDVAR),Draws)

# MUD1 = matrix(0,length(RDVAR),1)
# MUD2 = matrix(0,length(RDVAR),1)
D1upper = matrix(0,length(RDVAR),1)
D1lower = matrix(0,length(RDVAR),1)
D2upper = matrix(0,length(RDVAR),1)
D2lower = matrix(0,length(RDVAR),1)
MUD1    = matrix(0,length(RDVAR),1)
MUD2    = matrix(0,length(RDVAR),1)
# Using a 3D array to store in FF
# FF<-array(0,dim=c(length(RDVAR),Draws,2))
#   #print (Gender[q])
#   for (q in 1:length(RDVAR)){
#     #print(cbind(Gender[q],MUD1[q],MUD2[q]))
#     
#   if((RDVAR[q] %% 100 == 0) & (RDVAR[q] %% 500 != 0)){
#     #-----------------------------MOD of 100-------------------------------#
#     
#     D1upper[q] = RDVAR[q]+50 
#     D1lower[q] = RDVAR[q]-50
#     D2upper[q] = 0
#     D2lower[q] = -Inf
#     MUD1[q] = Data[q,4]
#     MUD2[q] = Data[q,5]
#     #print (c(q,"MOD of 100",MUD1[q],MUD2[q]))
#     #X[q,1:1000] 
#     tmp <- rtmvnorm(n=Draws, mean=c(MUD1[q],MUD2[q]),
#                    sigma=VCMatrix, lower=c(log(D1lower[q]), D2lower[q]), upper=c(log(D1upper[q]),D2upper[q]),
#                    algorithm="gibbs")
#     for(i in 1:Draws){
#       for(j in 1:2){
#         #print(c(q,i,j))
#         FF[q,i,j] = tmp[i,j]
#       }
#     }
#     #----------------------------------------------------------------------#
#   } else if((RDVAR[q] %% 500 == 0) & (RDVAR[q] %% 1000 != 0)){
#     
#     D1upper[q] = RDVAR[q]+250 
#     D1lower[q] = RDVAR[q]-250
#     D2upper[q] = 1.63
#     D2lower[q] = -Inf
#     MUD1[q] = Data[q,4]
#     MUD2[q] = Data[q,5]
#     #print (c(q,"MOD of 500",MUD1[q],MUD2[q]))
#     tmp2 <- rtmvnorm(n=Draws, mean=c(MUD1[q],MUD2[q]),
#                     sigma=VCMatrix, lower=c(log(D1lower[q]),D2lower[q]), upper=c(log(D1upper[q]),D2upper[q]),
#                     algorithm="gibbs")
#     for(i in 1:Draws){
#       for(j in 1:2){
#         #print(c(q,i,j))
#         FF[q,i,j] = tmp2[i,j]
#       }
#     }
#   }
#     else if (RDVAR[q] %%1000 ==0){
#       D1upper[q] = RDVAR[q]+500 
#       D1lower[q] = RDVAR[q]-500
#       D2upper[q] = Inf
#       D2lower[q] = -Inf
#       MUD1[q] = Data[q,4]
#       MUD2[q] = Data[q,5]
#       #print (c(q,"MOD of 1000",MUD1[q],MUD2[q]))
#       tmp3 <- rtmvnorm(n=Draws, mean=c(MUD1[q],MUD2[q]),
#                       sigma=VCMatrix, lower=c(log(D1lower[q]), D2lower[q]), upper=c(log(D1upper[q]),D2upper[q]),
#                       algorithm="gibbs")
#       for(i in 1:Draws){
#         for(j in 1:2){
#           #print(c(q,i,j))
#           FF[q,i,j] = tmp3[i,j]
#         }
#       }
#     }
#     #print(c(q,Gender[q],RDVAR[q],MUD1[q],MUD2[q],D1upper[q],D1lower[q],D2upper[q],D2lower[q]))
#     #write.csv(FF[q,,], paste(c("/Users/Ghasak/Desktop/All_Individual_Dataset/",q,".csv"), collapse = ''),append = T)
# }
# 
# 
# 
# 
# 
# 
# 
# # Draw case 1 2 and 3
# 
# k1 <- FF[1,,]
# k2 <- FF[500,,]
# k3 <- FF[972,,]
# hist(exp(k1[,1]))
# hist(exp(k2[,1]))
# hist(exp(k3[,1]))


# #===========================================================================================
# # This to check existed matrix and see if it bounded
# #===========================================================================================
# 
# # Testing the while loop
# Q500 <- FF[500,1:10,]
# DD = 10 # Number of draws
# count <- 1
# 
# YS = as.matrix(exp(Q500[,1]),nrow(Q500[,1]),1)
# ZS  = as.matrix(exp(Q500[,2]),nrow(Q500[,1]),1)
# #SS =  matrix(0,nrow(YS),2)
# 
# 
# for (q in 1:length(RDVAR)){
# while (count < DD){
#   if(ZS[q]>0){
#     if ((YS[q]<(450)) &(YS[q]>550)){
#       SS = rtmvnorm(n=1, mean=c(MUD1[500],MUD2[500]),
#                     sigma=VCMatrix, lower=c(log(D1lower[500]),D2lower[500]), upper=c(log(D1upper[500]),D2upper[500]),
#                     algorithm="gibbs")
#       SS1[q,,]=SS
#       print(count)
#       
#       
#     }
#   }
#   
#   
#   count = count+1
# }
# }
# 


# 
# #===========================================================================================
# # Lets try here to do the real draw not to check the existed one
# #===========================================================================================
# 
# # Testing the while loop
# Q500 <- FF[500,1:10,]
# DD = 10 # Number of draws
# count <- 1
# 
# YS = as.matrix(exp(Q500[,1]),nrow(Q500[,1]),1)
# ZS  = as.matrix(exp(Q500[,2]),nrow(Q500[,1]),1)
# SS =  0
# 
# 
# 
# Draws =10
# YZS = array(0,dim=c(length(RDVAR),Draws,2))
# SS1 = array(0,dim=c(length(RDVAR),Draws,2))
# #array(0,dim=c(length(Draws),Draws,2))
# 
# i = 1
# 
#         for (q in 1:length(RDVAR)){
#             if((RDVAR[q] %% 500 == 0) & (RDVAR[q] %% 1000 != 0)){
# 
#                 D1upper[q] = RDVAR[q]+250 
#                 D1lower[q] = RDVAR[q]-250
#                 D2upper[q] = 1.63
#                 D2lower[q] = -Inf
#                 MUD1[q] = Data[q,4]
#                 MUD2[q] = Data[q,5]
#                       while (count < Draws){
# 
#                         SS = rtmvnorm(n=1, mean=c(MUD1[q],MUD2[q]),
#                                       sigma=VCMatrix, lower=c(log(D1lower[q]),D2lower[q]), upper=c(log(D1upper[q]),D2upper[q]),
#                                       algorithm="gibbs")
#                         
#                               if((SS[2]>0)&&(SS[2]<D2upper[q])){
# 
#                                     if ((exp(SS[1])<(RDVAR[q]-50)) && (exp(SS[1]>RDVAR[q]+50))){
#                                     #set.seed(123)
#                                      
#                                       #print(c(q,i,j))
#                                       SS1[q,i,1] = SS[1]
#                                       SS1[q,i,2] = SS[2]
#                                       i = i +1
#                                               
#                                     
#                                     #   
#                                     # 
#                                     # SS1[q,,]=SS
#                                     print(count)
#                                     count = count+1
#                                     }
#                               }
#                             
#                       }
#             }
#         }
# 
# 
# #===========================================================================================
# # Checking how to sample of one value at a time compared to DDD times at once
# # this comparison is working only when there is a zero covariance (Independent events).
# # Fri Dec 14th 17:31 
# #===========================================================================================
# 
# DDD=1000
# GH1=matrix(0,DDD,1)
# GH2=matrix(0,DDD,1)
# #VCMatrix= matrix(c(0.51, 0.56, 0.56, 1.00), 2, 2)
# VCMatrix2= matrix(c(1, 0, 0, 1.00), 2, 2)
# # Draw 1 with loop from the same function
# for (k in 1:DDD){
# 
# GH =rtmvnorm(n=1, mean=c(MUD1[500],MUD2[500]),
#                   sigma=VCMatrix2, lower=c(-Inf,-Inf), upper=c(Inf,Inf),
#                   algorithm="gibbs")
#           # rtmvnorm(n=1, mean=c(MUD1[500],MUD2[500]),
#           #                     sigma=VCMatrix, lower=c(log(D1lower[500]),D2lower[500]), upper=c(log(D1upper[500]),D2upper[500]),
#           #                     algorithm="rejection")
# GH1[k]=GH[1]
# GH2[k]=GH[2]
# }
# 
# cbind(GH1,GH2)
# 
# JHN =0
#  # drawing DDD at once from the function as suggested by Jahn Sensei
# JHN = rtmvnorm(n=DDD, mean=c(MUD1[500],MUD2[500]),
#                     sigma=VCMatrix2, lower=c(-Inf,-Inf), upper=c(Inf,Inf),
#                     algorithm="gibbs")
#           # rtmvnorm(n=DDD, mean=c(MUD1[500],MUD2[500]),
#           #          sigma=VCMatrix, lower=c(log(D1lower[500]),D2lower[500]), upper=c(log(D1upper[500]),D2upper[500]),
#           #          algorithm="gibbs")
# print ("=======Original Values==============")
# print(cbind(MUD1[500],MUD2[500]))
# print(VCMatrix)
# print ("=======Mean=========================")
# print(cbind(mean(GH1),mean(GH2)))
# print(cbind(mean(JHN[,1]),mean(JHN[,2])))
# print ("=======Standard Devation============")
# print(cbind(sd(GH1),sd(GH2)))
# print(cbind(sd(JHN[,1]),sd(JHN[,2])))
# 
# ===========================================================================================
# I will try here to run the same program for the observation of 500 only
# to element any confusion about all individuals
# 
# ===========================================================================================

drawx=1000
#VCMatrix= matrix(c(0.51, 0.56, 0.56, 1.00), 2, 2)
VCMatrix2= matrix(c(0.51, 0.56, 0.56, 1.00), 2, 2)
# Draw 1 with loop from the same function
FF<-array(0,dim=c(length(RDVAR),drawx,2))
for (q in 1:length(RDVAR)){
  cat("\014") 
  print(c("Indivdiual ",q))

  if((RDVAR[q] %% 100 == 0) & (RDVAR[q] %% 500 != 0)){
        #-----------------------------MOD of 100-------------------------------#

        D1upper[q] = RDVAR[q]+50
        D1lower[q] = RDVAR[q]-50
        D2upper[q] = 0
        D2lower[q] = -Inf
        MUD1[q] = Data[q,4]
        MUD2[q] = Data[q,5]
        #print (c(q,"MOD of 100",MUD1[q],MUD2[q]))
        #X[q,1:1000]
        tmp <- rtmvnorm(n=drawx, mean=c(MUD1[q],MUD2[q]),
                       sigma=VCMatrix, lower=c(log(D1lower[q]), D2lower[q]), upper=c(log(D1upper[q]),D2upper[q]),
                       algorithm="gibbs")
        for(i in 1:drawx){
          for(j in 1:2){
            #print(c(q,i,j))
            FF[q,i,j] = tmp[i,j]
          }
        }

        #-----------------------------MOD of 500-------------------------------#
 }else if((RDVAR[q] %% 500 == 0) & (RDVAR[q] %% 1000 != 0)){

  GH1=matrix(0,drawx,1)
  GH2=matrix(0,drawx,1)
  D1upper[q] = RDVAR[q]+250
  D1lower[q] = RDVAR[q]-250
  D2upper[q] = 1.63
  D2lower[q] = -Inf
  MUD1[q] = Data[q,4]
  MUD2[q] = Data[q,5]

  count=1
  while (count <= drawx){

    GH =rtmvnorm(n=1, mean=c(MUD1[q],MUD2[q]),
                 sigma=VCMatrix, lower=c(log(D1lower[q]),D2lower[q]), upper=c(log(D1upper[q]),D2upper[q]),
                 algorithm="gibbs")
    # rtmvnorm(n=1, mean=c(MUD1[500],MUD2[500]),
    #                     sigma=VCMatrix, lower=c(log(D1lower[500]),D2lower[500]), upper=c(log(D1upper[500]),D2upper[500]),
    #                     algorithm="rejection")

    # Accept and reject Sampling

    if ((GH[2]<0) && (exp(GH[1])>(RDVAR[q]-50)) && (exp(GH[1])<(RDVAR[q]+50))){
      GH1[count]=GH[1]
      GH2[count]=GH[2]
      #print(count)
      count = count+1
    } else if ((GH[2]>0) && (GH[2]<1.63)){
      GH1[count]=GH[1]
      GH2[count]=GH[2]
      count = count+1
    }
  }
  U1 = as.matrix(cbind(GH1,GH2),drawx,2)
  FF[q,,]=U1
 }

  #-----------------------------MOD of 1000-------------------------------#
  else if (RDVAR[q] %%1000 ==0){
          D1upper[q] = RDVAR[q]+500
          D1lower[q] = RDVAR[q]-500
          D2upper[q] = Inf
          D2lower[q] = -Inf
          MUD1[q] = Data[q,4]
          MUD2[q] = Data[q,5]
          count=1
          while (count <= drawx){

            GH =rtmvnorm(n=1, mean=c(MUD1[q],MUD2[q]),
                         sigma=VCMatrix, lower=c(log(D1lower[q]),D2lower[q]), upper=c(log(D1upper[q]),D2upper[q]),
                         algorithm="gibbs")


            # Accept and reject Sampling

            if ((GH[2]<0) && (exp(GH[1])>(RDVAR[q]-50)) && (exp(GH[1])<(RDVAR[q]+50))){
              GH1[count]=GH[1]
              GH2[count]=GH[2]
              # print(count)
              count = count+1
            } else if ((GH[2]>0) && (GH[2]<1.63)){
                if ((exp(GH[1])>(RDVAR[q]-250)) && (exp(GH[1])<(RDVAR[q]+250))){
                  GH1[count]=GH[1]
                  GH2[count]=GH[2]
                  count = count+1
                }
            } else if ((GH[2]>1.63)){
              GH1[count]=GH[1]
              GH2[count]=GH[2]
              count = count+1
            }
          }
          U2 = as.matrix(cbind(GH1,GH2),drawx,2)
          FF[q,,]=U2
  }

}
print(" Case One===== indivdiual 1")
hist(exp(FF[1,,1]),border="blue", col="green",xlim=c(50,200), ylim=c(0,300),
                 breaks=10,prob = F)
print(" Case Two===== indivdiual 500")
hist(exp(FF[500,,1]),border="blue", col="green",xlim=c(0,800), ylim=c(0,300),
     breaks=16,prob = F)
print(" Case Three===== indivdiual 972")
hist(exp(FF[972,,1]),border="blue", col="green",xlim=c(4000,6000), ylim=c(0,300),
     breaks=10,prob = F)

#===========================================================================================
# Loop to printing the results into one single file
#===========================================================================================
# require(reshape2)
# Collection2 =melt(FF)
# Converting a matrix in 3D into 2D dimensions
Collection3 =matrix(FF,972000,2)
lnyD1 = exp(Collection3[,1])
# There is another way to change 3D matrix to a 2D matrix using loops
      # B = matrix(0,972000,2)
      # for (q in 1:NROW(RDVAR)){
      #   for (i in 1:drawx){
      #     for (j in 1:2){
      #       B[(q-1)*(2)+i,j]=FF[q,i,j]
      #     }
      #   }
      # }

#===========================================================================================
# Draw the travel distance by each individual -Density Plot 
#===========================================================================================

h <- hist(lnyD1, breaks = seq(0,6000,100), plot=FALSE#,border="black", col="lightblue",freq=F #probability = F #freq=T
          
          )  # You can set breaks=seq(0,6000,50) or breaks=50

h$counts=h$counts/sum(h$counts)   #h$mids,h$counts
plot(h,border="black", col="lightblue"
      ,xlim = c(0,4000)#range(h$mids)* 0.9      # , xlim = c(0,3000)
      ,ylim = c(0,0.2)#(max(h$counts)+max(h$counts)/1))
               # , ylim = c(0,0.2)
     #, axis(side=1, at=c(0,6000))      # c(-4, 0, 4)
     ,cex.lab=1.2, cex.axis=1.2, cex.main=1.2, cex.sub=1.2
     ,main="Histogram for Distance Traveled in m"
     ,xlab="Distance (m)"
     ,ylab="Probability"
     ,xaxs="i", yaxs="i" # meaning that 4% of the axis value is left on each side. To set this to 0: xaxs="i". See the xaxs section in ?par for more information.
     ,lwd = 2 # axes line width
     # ,par(lwd=1.2)
     ,axes = FALSE
     ,ann=FALSE, xaxt="n", yaxt="n"
     )

#grid(24, 24, lwd = 1,col ='black')
#And then we can also add a legend, so it will be easy to tell which line is which.

abline(v=seq(0, 5000, 500), col="gray48",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
abline(v=seq(0, 5000, 100), col="darkgray",lty = 4,lwd = 1.2) # To add horizantl line simply add h=0.001,
abline(h=seq(0,(0.2),0.01), col="darkgray",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
abline(h=c(0.05,0.1,0.15,0.2), col="gray48",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
#abline(h=0.15, col="darkgray",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
box(lty = 5, col = 'red',font = 50, font.lab = 7, font.axis = 20
    ,cex.lab=1.2, cex.axis=1.2, cex.main=1.2, cex.sub=1.2
    ,lwd = 3)


# generate the plot again to come to the front
plot(h,add=TRUE,col="lightblue",axes = FALSE,ann=FALSE, xaxt="n", yaxt="n"
     )

#axis(1, h$breaks, labels = seq(0,5500,100), tick = TRUE, padj= -1.5)  #h$breaks

# adjust the axes to fit your data range
axis(1, at=h$mids, tick = TRUE, padj= -0.4,cex.axis = 1.2)  #h$breaks  # seq(0,6000,500), labels = seq(0,6000,500)
axis(2,labels = TRUE, tick = TRUE, padj= -0.1,cex.axis = 1.2)  #h$breaks

# Draw lables of the axeses
mtext(side = 1, text = "Distance (m)", line = 3,padj= -1.5, cex=1.2) 
mtext(side = 2, text = "Probability", line = 3,padj= 0.8, cex=1.2) 
# Title for the graph 
title(main="Histogram for Distance Traveled in m")
# Draw the lognormal distribution curve
lines(seq(0, 5000, by=0.1), (100*dlnorm(seq(0, 5000, by=0.1),
                                        mean(log(lnyD1)), sd(log(lnyD1)))), col="blue",lwd = 2,
      font = 5, font.lab = 7, font.axis = 7)

# abline(v=767.0267, col="black",lty = 5,lwd = 5) # To add horizantl line simply add h=0.001,
# abline(v=602.1982, col="red",lty = 5,  lwd = 5) # To add horizantl line simply add h=0.001,
# abline(v=759.7315, col="blue",lty = 5, lwd = 5) # To add horizantl line simply add h=0.001,

abline(v=c(mean(lnyD1)) #,mean(RDVAR),exp(MUD1[1]))
       , col = c("chartreuse4", "royalblue", "red","blue")
       , lty = c(4,5,5)
       ,lwd = c(2,1.2,1.2))

legend(x = "right", # location of legend within plot area
       c("Mean", "Density","logNormal distribution"),
       col = c("chartreuse4", "coral1", "blue","red"),
       lwd = c(2, 2, 2,3),
       fill = c("chartreuse4", "coral1", "blue","red")
       ,title="Line types"
       ,text.font=2
       ,bg='white')

# Draw density function
#lines(density(lnyD1), col="red")
den_gh =density(lnyD1,na.rm=T)
den_ghx = den_gh$x
den_ghy = den_gh$y*100  # 100 scale is for matching our y-axis new scale which show probability not density
                        # Remember that probability =(density in y)*(base of the bar) (the base of each bar for 50 breaks is 100 m unit)

lines(den_ghx,den_ghy, # density plot
      lwd = 2, # thickness of line
      col = "coral1"
      )

#Next we???ll add a line for the mean:
# 
# abline(v = mean(RDVAR),
#        col = "royalblue",
#        lwd = 2)
# #And a line for the median:
# 
# abline(v = median(RDVAR),
#        col = "red",
#        lwd = 2)



#===========================================================================================
# Draw the travel distance by each individual -Frequency Plot 
#===========================================================================================

h2 <- hist(lnyD1, breaks = seq(0,6000,100), plot=FALSE#,border="black", col="lightblue",freq=F #probability = F #freq=T
          )
SS =max(h2$counts)+max(h2$counts)/3
h2 <- hist(lnyD1, breaks = 50, plot=T,freq=T
           ,xlim = c(0,4000)#range(h$mids)* 0.9      # , xlim = c(0,3000)
           ,ylim = c(0,SS)#(max(h$counts)+max(h$counts)/1))
           ,xaxs="i", yaxs="i"
           ,axes = FALSE
           ,ann=FALSE, xaxt="n", yaxt="n"
        
)


#grid(24, 24, lwd = 1,col ='black')
#And then we can also add a legend, so it will be easy to tell which line is which.

abline(v=seq(0, 5000, 500), col="gray48",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
abline(v=seq(0, 5000, 100), col="darkgray",lty = 4,lwd = 1.2) # To add horizantl line simply add h=0.001,
abline(h=seq(0,SS+83646.67,10000), col="darkgray",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
abline(h=c(50000,100000,150000,200000), col="gray48",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
#abline(h=0.15, col="darkgray",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
box(lty = 5, col = 'red',font = 50, font.lab = 7, font.axis = 20
    ,cex.lab=1.2, cex.axis=1.2, cex.main=1.2, cex.sub=1.2
    ,lwd = 3)


# generate the plot again to come to the front
plot(h2,add=TRUE,col="lightblue",axes = FALSE,ann=FALSE, xaxt="n", yaxt="n"
)

#axis(1, h$breaks, labels = seq(0,5500,100), tick = TRUE, padj= -1.5)  #h$breaks

# adjust the axes to fit your data range
axis(1,at=h$mid, tick = TRUE, padj= -0.4,cex.axis = 1.2)  #h$breaks  seq(0,6000,500), labels = seq(0,6000,500)
axis(2,labels = TRUE, tick = TRUE, padj= -0.1,cex.axis = 1.2)  #h$breaks

# Draw lables of the axeses
mtext(side = 1, text = "Distance (m)", line = 3,padj= -1.5, cex=1.2) 
mtext(side = 2, text = "Frequency", line = 3,padj= 0.8, cex=1.2) 
# Title for the graph 
title(main="Histogram for Distance Traveled in m")

abline(v=c(mean(lnyD1)) #,mean(RDVAR),exp(MUD1[1]))
       , col = c("chartreuse4", "royalblue", "red","blue")
       , lty = c(4,5,5)
       ,lwd = c(2,1.2,1.2))

legend(x = "right", # location of legend within plot area
       c("Mean"),
       col = c("chartreuse4", "coral1", "blue","red"),
       lwd = c(2, 2, 2,3),
       fill = c("chartreuse4", "coral1", "blue","red")
       ,title="Line types"
       ,text.font=2
       ,bg='white')

#===========================================================================================
# Draw the travel distance of observed dataset by each individual -Frequency Plot 
#===========================================================================================

h3 <- hist(RDVAR, breaks = 50, plot=FALSE#,border="black", col="lightblue",freq=F #probability = F #freq=T
)
SS2 =max(h3$counts)+max(h3$counts)/3
h3 <- hist(RDVAR, breaks = 50, plot=T,freq=T
           ,xlim = c(0,4000)#range(h$mids)* 0.9      # , xlim = c(0,3000)
           ,ylim = c(0,SS2)#(max(h$counts)+max(h$counts)/1))
           ,xaxs="i", yaxs="i"
           ,axes = FALSE
           ,ann=FALSE, xaxt="n", yaxt="n"
           
)


#grid(24, 24, lwd = 1,col ='black')
#And then we can also add a legend, so it will be easy to tell which line is which.

abline(v=seq(0, 5000, 500), col="gray48",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
abline(v=seq(0, 5000, 100), col="darkgray",lty = 4,lwd = 1.2) # To add horizantl line simply add h=0.001,
abline(h=seq(0,SS+83646.67,10000), col="darkgray",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
abline(h=c(50000,100000,150000,200000), col="gray48",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
#abline(h=0.15, col="darkgray",lty = 5,lwd = 1.2) # To add horizantl line simply add h=0.001,
box(lty = 5, col = 'red',font = 50, font.lab = 7, font.axis = 20
    ,cex.lab=1.2, cex.axis=1.2, cex.main=1.2, cex.sub=1.2
    ,lwd = 3)


# generate the plot again to come to the front
plot(h3,add=TRUE,col="lightblue",axes = FALSE,ann=FALSE, xaxt="n", yaxt="n"
)

#axis(1, h$breaks, labels = seq(0,5500,100), tick = TRUE, padj= -1.5)  #h$breaks

# adjust the axes to fit your data range
axis(1, seq(0,6000,500), labels = seq(0,6000,500), tick = TRUE, padj= -0.4,cex.axis = 1.2)  #h$breaks
axis(2,labels = TRUE, tick = TRUE, padj= -0.1,cex.axis = 1.2)  #h$breaks

# Draw lables of the axeses
mtext(side = 1, text = "Distance (m)", line = 3,padj= -1.5, cex=1.2) 
mtext(side = 2, text = "Probability", line = 3,padj= 0.8, cex=1.2) 
# Title for the graph 
title(main="Histogram for Distance Traveled in m")

abline(v=c(mean(RDVAR)) #,mean(RDVAR),exp(MUD1[1]))
       , col = c("chartreuse4", "royalblue", "red","blue")
       , lty = c(4,5,5)
       ,lwd = c(2,1.2,1.2))

legend(x = "right", # location of legend within plot area
       c("Mean"),
       col = c("chartreuse4", "coral1", "blue","red"),
       lwd = c(2, 2, 2,3),
       fill = c("chartreuse4", "coral1", "blue","red")
       ,title="Line types"
       ,text.font=2
       ,bg='white')
 ## now shrink the window (in x- and y-direction) and observe the axis labels drawn
#===========================================================================================
# Checking on Mond Dec 17th 18:27 with Jahn sensei about the imputation
#===========================================================================================
# drawx=1000
# 
# 
# #VCMatrix= matrix(c(0.51, 0.56, 0.56, 1.00), 2, 2)
# VCMatrix2= matrix(c(0.51, 0.56, 0.56, 1.00), 2, 2)
# # Draw 1 with loop from the same function
# FF<-array(0,dim=c(length(RDVAR),drawx,2))
# 
# 
#   if((RDVAR[500] %% 100 == 0) & (RDVAR[500] %% 500 != 0)){
#     #-----------------------------MOD of 100-------------------------------#
# 
#     D1upper[500] = RDVAR[500]+50
#     D1lower[500] = RDVAR[500]-50
#     D2upper[500] = 0
#     D2lower[500] = -Inf
#     MUD1[500] = Data[500,4]
#     MUD2[500] = Data[500,5]
#     #print (c(q,"MOD of 100",MUD1[q],MUD2[q]))
#     #X[q,1:1000]
#     tmp <- rtmvnorm(n=drawx, mean=c(MUD1[500],MUD2[500]),
#                     sigma=VCMatrix, lower=c(log(D1lower[500]), D2lower[500]), upper=c(log(D1upper[500]),D2upper[500]),
#                     algorithm="gibbs")
#     for(i in 1:drawx){
#       for(j in 1:2){
#         #print(c(q,i,j))
#         FF[q,i,j] = tmp[i,j]
#       }
#     }
# 
#     #-----------------------------MOD of 100-------------------------------#
#   }else if((RDVAR[500] %% 500 == 0) & (RDVAR[500] %% 1000 != 0)){
# 
#     GH1=matrix(0,drawx,1)
#     GH2=matrix(0,drawx,1)
#     D1upper[500] = RDVAR[500]+250
#     D1lower[500] = RDVAR[500]-250
#     D2upper[500] = 1.63
#     D2lower[500] = -Inf
#     MUD1[500] = Data[500,4]
#     MUD2[500] = Data[500,5]
# 
#     count=1
#     item1 =1
#     item2 =1
#     while (count <= drawx){
#       
#      
# 
#       GH =rtmvnorm(n=1, mean=c(MUD1[500],MUD2[500]),
#                    sigma=VCMatrix, lower=c(log(D1lower[500]),D2lower[500]), upper=c(log(D1upper[500]),D2upper[500]),
#                    algorithm="rejection")
#       # rtmvnorm(n=1, mean=c(MUD1[500],MUD2[500]),
#       #                     sigma=VCMatrix, lower=c(log(D1lower[500]),D2lower[500]), upper=c(log(D1upper[500]),D2upper[500]),
#       #                     algorithm="rejection")
# 
#       # Accept and reject Sampling
# 
#       if ((GH[2]<0) && (exp(GH[1])>(RDVAR[500]-50)) && (exp(GH[1])<(RDVAR[500]+50))){
#         GH1[count]=GH[1]
#         GH2[count]=GH[2]
#         #print(cbind("condition 1 occure",count))
#         count = count+1
#         item1=item1+1
#       } else if ((GH[2]>1000) && (GH[2]<3000)){
#         GH1[count]=GH[1]
#         GH2[count]=GH[2]
#         count = count+1
#         item2=item2+1
#         #print(cbind("condition 2 occure",count))
#       }
#       
#     }
#     
#  
#   }
# U = as.matrix(cbind(GH1,GH2),drawx,2)
# FF[500,,]=U
# 
#       print(cbind("first condition occure",item1/count))
#       print(cbind("second condition occure",item2/count))
# 
#       hist(exp(FF[500,,1]),border="blue", col="green",xlim=c(400,600), ylim=c(0,150),
#            breaks=10,prob = F)

      