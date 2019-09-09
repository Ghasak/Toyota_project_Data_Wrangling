
# OUTPUT -Multivariate Truncated Poisson-LogNorm with Correlation

```R
R version 3.5.2 (2018-12-20) -- "Eggshell Igloo"
Copyright (C) 2018 The R Foundation for Statistical Computing
Platform: x86_64-apple-darwin15.6.0 (64-bit)

R は、自由なソフトウェアであり、「完全に無保証」です。
一定の条件に従えば、自由にこれを再配布することができます。
配布条件の詳細に関しては、'license()' あるいは 'licence()' と入力してください。

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

'demo()' と入力すればデモをみることができます。
'help()' とすればオンラインヘルプが出ます。
'help.start()' で HTML ブラウザによるヘルプがみられます。
'q()' と入力すれば R を終了します。

> # ========================================================================= #
> #  Title :           Traffic Accident Analysis                              #
> #  Project Name:     Toyota City carsh data                                 #
> #  Starting Data:    2019/Sep.l/00                                          #
> #  File Name:        [1] Multivariate Truncated Poisson [First Trail]       #
> #  Version:          V.01                                                   #
> #  Last changed:     2019/Sep./00 00:00:00                                  #
> #  Purpose:          Analysis different driver age groups                   #
> #  Author:           Ghasak Ibrahim                                         #
> #  Copyright:        (C) 2019-Sep.                                          #
> #  Product:                                                                 #
> #  Please see the     note.txt file for more information on this model      #
> #  All other rights reserved.                                               #
> #       Multivaraite Truncated Poisson Model Using Copula and CML           #
> #   parameterizing   expected number of crashes function only,              #
> #   Homoscedastic     model                                                 #
> # ========================================================================= #
> # =========================================================================
> #               Cleaning the background of intialize Space
> # =========================================================================
> while (!is.null(dev.list()))  dev.off(dev.list()["RStudioGD"])
> #dev.off(dev.list()["RStudioGD"]) # clean the Graph Area
> rm(list=ls())                    # clean the Workspace (dataset)
> cat("\014")                      # clean the console area

> graphics.off()                   # close graphics windows (For R Script)
>
> # =========================================================================
> #           Input Data and Intializing the parameter vectors
> # =========================================================================
>
> # Data1 <- read.csv(file.choose())
> directory_location <- "~/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/R/0_DataSet/dataSet.csv"
> #directory_location <- "/Users/ghasak/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/R/0_DataSet/dataSet.csv"
> #directory_location <- paste0(getwd(),'/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/R/0_DataSet/dataSet.csv')
> Data1 <- read.csv(directory_location)
>
> Total       = Data1$Crash_count
> Young       = Data1$Driver_Young
> Middle_age  = Data1$Driver_Middle_age
> Senior      = Data1$Driver_Senior
> # =======================================================================
> #               Data Frame converting our data [Similar to Pandas]
> # =======================================================================
> MinorPrefecturalRoad             <- Data1$Minor_prefectural_road
> OtherRoadTypes                   <- Data1$Narrow_road
> Conf30KmhorLess                  <- Data1$conf1_30kmh_orless
> Conf40KmhorLess                  <- Data1$conf1_40kmh_orless
> Conf50KmhorLess                  <- Data1$conf1_50kmh_orless
> Conf60KmhorLess                  <- Data1$conf1_60kmh_orless
> ConfNoRegulation                 <- Data1$conf1_No_regulation
> LogTrafficVolume                 <- Data1$log_traffic_volume
> IntersTypeThreeArms              <- Data1$IS_IT_THREE_ARMS
> LogShortestWidth                 <- Data1$LOG_SHORTEST_WIDTH_INTER
> LogNoDriveWays                   <- Data1$LOG_NO_DRIVE_WAYS
> LogNoLanes                       <- Data1$LOG_NUMBER_OF_LANES
> NoLanesChanged                   <- Data1$NO_OF_LANES_CHANGED
> IsThereSkewness                  <- Data1$IS_THERE_SKEWNESS
> NonDividedSigleRoadway           <- Data1$NON_DIVIDED_SINGLE_ROADWAY
> LogAverageWidthPhysicalMedian    <- Data1$LOG_AVERAGE_WIDTH_PHYSICAL_MEDIAN
> IsThereCentralStrip              <- Data1$IS_THERE_CENTRAL_STRIP
> SignalizedHighLevelSignal        <- Data1$SIGNALIZED_HIGH_LEVEL_SIGNAL
> PedestrianSignalExisted          <- Data1$FLASHING_GREEN_PED
>
> # =======================================================================
> #               Halton Sequence in R-Using the package randtoolbox
> # =======================================================================
> library(randtoolbox)
 要求されたパッケージ rngWELL をロード中です
This is randtoolbox. For an overview, type 'help("randtoolbox")'.
> dim1 = 3  # How many chains you want to draw
> # You can get Normal distribution if you make normal =TRUE
> n = 130
> ux= halton(n, dim = dim1, init = TRUE, normal = TRUE, usetime = FALSE)
> # sobol(n, dim = 1, init = TRUE, scrambling = 0, seed = 4711, normal = FALSE)
> # torus(n, dim = 1, prime, init = TRUE, mixed = FALSE, usetime = FALSE,normal=FALSE)
>
> # =====================================================================
> #               Run Univariate Poisson to get start values
> # =====================================================================
> require(maxLik)
 要求されたパッケージ maxLik をロード中です
 要求されたパッケージ miscTools をロード中です

Please cite the 'maxLik' package as:
Henningsen, Arne and Toomet, Ott (2011). maxLik: A package for maximum likelihood estimation in R. Computational Statistics 26(3), 443-458. DOI 10.1007/s00180-010-0217-1.

If you have questions, suggestions, or comments regarding the 'maxLik' package, please use a forum or 'tracker' at maxLik's R-Forge site:
https://r-forge.r-project.org/projects/maxlik/
> require(sandwich)
 要求されたパッケージ sandwich をロード中です
> require(foreign)
 要求されたパッケージ foreign をロード中です
> require(ggplot2)
 要求されたパッケージ ggplot2 をロード中です
> require(MASS)
 要求されたパッケージ MASS をロード中です
>
> outcome <- "Total"
> variables <-   c("MinorPrefecturalRoad",
+                  "OtherRoadTypes",
+                  "Conf30KmhorLess",
+                  "Conf40KmhorLess",
+                  "Conf50KmhorLess",
+                  "Conf60KmhorLess",
+                  "ConfNoRegulation",
+                  "LogTrafficVolume",
+                  "IntersTypeThreeArms",
+                  "LogShortestWidth",
+                  "LogNoDriveWays",
+                  "LogNoLanes",
+                  "NoLanesChanged",
+                  "IsThereSkewness",
+                  "NonDividedSigleRoadway",
+                  "LogAverageWidthPhysicalMedian",
+                  "IsThereCentralStrip",
+                  "SignalizedHighLevelSignal",
+                  "PedestrianSignalExisted")
>
> # fully parameterized!
> Total_formula <- as.formula(
+   paste(outcome, paste(variables, collapse = " + "),sep = " ~ "))
> print(Total_formula)
Total ~ MinorPrefecturalRoad + OtherRoadTypes + Conf30KmhorLess +
    Conf40KmhorLess + Conf50KmhorLess + Conf60KmhorLess + ConfNoRegulation +
    LogTrafficVolume + IntersTypeThreeArms + LogShortestWidth +
    LogNoDriveWays + LogNoLanes + NoLanesChanged + IsThereSkewness +
    NonDividedSigleRoadway + LogAverageWidthPhysicalMedian +
    IsThereCentralStrip + SignalizedHighLevelSignal + PedestrianSignalExisted
> # Performing Negative Binomial Model [For fixed theta only (dispersion)]
> mtotal <- glm.nb(Total_formula, link = log)
> #,init.theta = 1.032713156,link = log)
> summary(mtotal)

Call:
glm.nb(formula = Total_formula, link = log, init.theta = 13.66947699)

Deviance Residuals:
    Min       1Q   Median       3Q      Max
-2.2174  -0.6346  -0.2158   0.3041   4.1859

Coefficients:
                              Estimate Std. Error z value Pr(>|z|)
(Intercept)                   -1.49585    0.35941  -4.162 3.15e-05 ***
MinorPrefecturalRoad           0.16050    0.06412   2.503 0.012314 *
OtherRoadTypes                 0.46111    0.09410   4.900 9.57e-07 ***
Conf30KmhorLess                0.39999    0.09397   4.257 2.08e-05 ***
Conf40KmhorLess                0.61858    0.06833   9.052  < 2e-16 ***
Conf50KmhorLess                0.61944    0.07370   8.405  < 2e-16 ***
Conf60KmhorLess                0.29577    0.06778   4.363 1.28e-05 ***
ConfNoRegulation               0.42039    0.06034   6.967 3.23e-12 ***
LogTrafficVolume               0.08956    0.02023   4.427 9.57e-06 ***
IntersTypeThreeArms           -0.21998    0.09068  -2.426 0.015272 *
LogShortestWidth               0.08533    0.06800   1.255 0.209570
LogNoDriveWays                -0.05206    0.03929  -1.325 0.185223
LogNoLanes                     0.54703    0.15712   3.482 0.000498 ***
NoLanesChanged                -0.20197    0.10562  -1.912 0.055858 .
IsThereSkewness                0.03682    0.05749   0.640 0.521916
NonDividedSigleRoadway        -0.14388    0.07315  -1.967 0.049192 *
LogAverageWidthPhysicalMedian  0.09017    0.07565   1.192 0.233307
IsThereCentralStrip           -0.15138    0.09279  -1.631 0.102790
SignalizedHighLevelSignal      0.15863    0.07607   2.085 0.037034 *
PedestrianSignalExisted        0.13507    0.07302   1.850 0.064345 .
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for Negative Binomial(13.6695) family taken to be 1)

    Null deviance: 1178.20  on 433  degrees of freedom
Residual deviance:  326.95  on 414  degrees of freedom
AIC: 1848.4

Number of Fisher Scoring iterations: 1


              Theta:  13.67
          Std. Err.:  2.78

 2 x log-likelihood:  -1806.406
>
> # # Performing Poisson Model
> mtotal_poisson <- glm(Total_formula,family = "poisson")
> # summary(m2)
> # Start_m2 <<- m2$coefficients
> # ===========================Young Drivers=============================
> outcome <- "Young"
> # our modeling effort,
> # fully parameterized!
> Young_formula <- as.formula(
+   paste(outcome, paste(variables, collapse = " + "),sep = " ~ "))
> print(Young_formula)
Young ~ MinorPrefecturalRoad + OtherRoadTypes + Conf30KmhorLess +
    Conf40KmhorLess + Conf50KmhorLess + Conf60KmhorLess + ConfNoRegulation +
    LogTrafficVolume + IntersTypeThreeArms + LogShortestWidth +
    LogNoDriveWays + LogNoLanes + NoLanesChanged + IsThereSkewness +
    NonDividedSigleRoadway + LogAverageWidthPhysicalMedian +
    IsThereCentralStrip + SignalizedHighLevelSignal + PedestrianSignalExisted
> # Performing Negative Binomial Model [For fixed theta only (dispersion)]
> m1 <- glm.nb(Young_formula, link = log)
> #,init.theta = 1.032713156,link = log)
> summary(m1)

Call:
glm.nb(formula = Young_formula, link = log, init.theta = 5.445292076)

Deviance Residuals:
    Min       1Q   Median       3Q      Max
-2.2688  -0.9088  -0.5353   0.4454   2.5121

Coefficients:
                              Estimate Std. Error z value Pr(>|z|)
(Intercept)                   -5.38872    0.79098  -6.813 9.58e-12 ***
MinorPrefecturalRoad           0.02606    0.13837   0.188 0.850587
OtherRoadTypes                 0.39443    0.19844   1.988 0.046847 *
Conf30KmhorLess                0.63313    0.18869   3.355 0.000793 ***
Conf40KmhorLess                0.18409    0.14109   1.305 0.191951
Conf50KmhorLess                0.71358    0.17253   4.136 3.53e-05 ***
Conf60KmhorLess                0.19881    0.14162   1.404 0.160374
ConfNoRegulation               0.43353    0.13151   3.296 0.000979 ***
LogTrafficVolume               0.11645    0.04203   2.771 0.005595 **
IntersTypeThreeArms           -0.22489    0.20881  -1.077 0.281480
LogShortestWidth               0.50450    0.19100   2.641 0.008256 **
LogNoDriveWays                -0.08583    0.08353  -1.028 0.304171
LogNoLanes                     1.15338    0.33012   3.494 0.000476 ***
NoLanesChanged                -0.47556    0.23314  -2.040 0.041368 *
IsThereSkewness               -0.06314    0.12274  -0.514 0.606929
NonDividedSigleRoadway        -0.25774    0.16760  -1.538 0.124090
LogAverageWidthPhysicalMedian  0.17981    0.14558   1.235 0.216784
IsThereCentralStrip           -0.13201    0.20011  -0.660 0.509457
SignalizedHighLevelSignal      0.11728    0.15659   0.749 0.453896
PedestrianSignalExisted       -0.09382    0.15974  -0.587 0.557007
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for Negative Binomial(5.4453) family taken to be 1)

    Null deviance: 683.05  on 433  degrees of freedom
Residual deviance: 397.56  on 414  degrees of freedom
AIC: 1013.1

Number of Fisher Scoring iterations: 1


              Theta:  5.45
          Std. Err.:  2.09

 2 x log-likelihood:  -971.104
> Start_m1 <<- m1$coefficients
> # # Performing Poisson Model
> # m2 <- glm(Total_formula,family = "poisson")
> # summary(m2)
> # Start_m2 <<- m2$coefficients
> #summary(m1)
> Start_m1 <<- m1$coefficients
> # ===========================Middle_age Drivers========================
> outcome <- "Middle_age"
> # our modeling effort,
> # fully parameterized!
> Middle_age_formula <- as.formula(
+   paste(outcome, paste(variables, collapse = " + "),sep = " ~ "))
> print(Middle_age_formula)
Middle_age ~ MinorPrefecturalRoad + OtherRoadTypes + Conf30KmhorLess +
    Conf40KmhorLess + Conf50KmhorLess + Conf60KmhorLess + ConfNoRegulation +
    LogTrafficVolume + IntersTypeThreeArms + LogShortestWidth +
    LogNoDriveWays + LogNoLanes + NoLanesChanged + IsThereSkewness +
    NonDividedSigleRoadway + LogAverageWidthPhysicalMedian +
    IsThereCentralStrip + SignalizedHighLevelSignal + PedestrianSignalExisted
> # Performing Negative Binomial Model [For fixed theta only (dispersion)]
> m2 <- glm.nb(Middle_age_formula, link = log)
> #,init.theta = 1.032713156,link = log)
> summary(m2)

Call:
glm.nb(formula = Middle_age_formula, link = log, init.theta = 14.68741512)

Deviance Residuals:
    Min       1Q   Median       3Q      Max
-2.9757  -0.6891  -0.1175   0.3468   3.1452

Coefficients:
                                Estimate Std. Error z value Pr(>|z|)
(Intercept)                   -1.6818632  0.4131625  -4.071 4.69e-05 ***
MinorPrefecturalRoad           0.1847777  0.0740421   2.496 0.012575 *
OtherRoadTypes                 0.4624017  0.1085645   4.259 2.05e-05 ***
Conf30KmhorLess                0.3240173  0.1078648   3.004 0.002665 **
Conf40KmhorLess                0.7142934  0.0822330   8.686  < 2e-16 ***
Conf50KmhorLess                0.5855832  0.0861548   6.797 1.07e-11 ***
Conf60KmhorLess                0.3465841  0.0778409   4.452 8.49e-06 ***
ConfNoRegulation               0.4509414  0.0704305   6.403 1.53e-10 ***
LogTrafficVolume               0.0875105  0.0234112   3.738 0.000186 ***
IntersTypeThreeArms           -0.2217017  0.1057155  -2.097 0.035980 *
LogShortestWidth               0.0616424  0.0758152   0.813 0.416183
LogNoDriveWays                -0.0418065  0.0452733  -0.923 0.355786
LogNoLanes                     0.4409378  0.1816260   2.428 0.015194 *
NoLanesChanged                -0.1117258  0.1225752  -0.911 0.362038
IsThereSkewness               -0.0004652  0.0662971  -0.007 0.994401
NonDividedSigleRoadway        -0.1233253  0.0851171  -1.449 0.147368
LogAverageWidthPhysicalMedian  0.1011842  0.0837008   1.209 0.226709
IsThereCentralStrip           -0.2084688  0.1070166  -1.948 0.051414 .
SignalizedHighLevelSignal      0.1618768  0.0880261   1.839 0.065921 .
PedestrianSignalExisted        0.1327781  0.0845267   1.571 0.116219
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for Negative Binomial(14.6874) family taken to be 1)

    Null deviance: 1022.1  on 433  degrees of freedom
Residual deviance:  391.4  on 414  degrees of freedom
AIC: 1640.2

Number of Fisher Scoring iterations: 1


              Theta:  14.69
          Std. Err.:  4.32

 2 x log-likelihood:  -1598.192
> Start_m2 <<- m2$coefficients
> # # Performing Poisson Model
> # m2 <- glm(Total_formula,family = "poisson")
> # summary(m2)
> # Start_m2 <<- m2$coefficients
> # ===========================Senior Drivers=============================
> # Only Senior Drivers will be selected as Poisson count model [dispersion is not sig. from STATA]
> outcome <- "Senior"
> # our modeling effort,
> # fully parameterized!
> Senior_formula <- as.formula(
+   paste(outcome, paste(variables, collapse = " + "),sep = " ~ "))
> print(Senior_formula)
Senior ~ MinorPrefecturalRoad + OtherRoadTypes + Conf30KmhorLess +
    Conf40KmhorLess + Conf50KmhorLess + Conf60KmhorLess + ConfNoRegulation +
    LogTrafficVolume + IntersTypeThreeArms + LogShortestWidth +
    LogNoDriveWays + LogNoLanes + NoLanesChanged + IsThereSkewness +
    NonDividedSigleRoadway + LogAverageWidthPhysicalMedian +
    IsThereCentralStrip + SignalizedHighLevelSignal + PedestrianSignalExisted
> # Performing Negative Binomial Model [For fixed theta only (dispersion)]
> m3 <- glm(Senior_formula, family = 'poisson')
> #,init.theta = 1.032713156,link = log)
> summary(m3)

Call:
glm(formula = Senior_formula, family = "poisson")

Deviance Residuals:
    Min       1Q   Median       3Q      Max
-2.2312  -0.9958  -0.6297   0.6023   2.8615

Coefficients:
                              Estimate Std. Error z value Pr(>|z|)
(Intercept)                   -2.26560    0.73779  -3.071  0.00213 **
MinorPrefecturalRoad           0.21704    0.13228   1.641  0.10083
OtherRoadTypes                 0.57485    0.19083   3.012  0.00259 **
Conf30KmhorLess                0.43269    0.18832   2.298  0.02159 *
Conf40KmhorLess                0.72488    0.15119   4.795 1.63e-06 ***
Conf50KmhorLess                0.67797    0.16051   4.224 2.40e-05 ***
Conf60KmhorLess                0.31337    0.14022   2.235  0.02543 *
ConfNoRegulation               0.21465    0.12717   1.688  0.09143 .
LogTrafficVolume               0.09012    0.04192   2.150  0.03158 *
IntersTypeThreeArms           -0.24508    0.19110  -1.282  0.19967
LogShortestWidth              -0.11663    0.12718  -0.917  0.35909
LogNoDriveWays                -0.06486    0.08100  -0.801  0.42324
LogNoLanes                     0.19196    0.32837   0.585  0.55884
NoLanesChanged                -0.21343    0.22575  -0.945  0.34444
IsThereSkewness                0.32590    0.12407   2.627  0.00862 **
NonDividedSigleRoadway        -0.11950    0.15182  -0.787  0.43123
LogAverageWidthPhysicalMedian -0.05859    0.17045  -0.344  0.73107
IsThereCentralStrip           -0.02543    0.19763  -0.129  0.89761
SignalizedHighLevelSignal      0.13555    0.15733   0.862  0.38892
PedestrianSignalExisted        0.32138    0.15426   2.083  0.03722 *
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for poisson family taken to be 1)

    Null deviance: 592.58  on 433  degrees of freedom
Residual deviance: 449.70  on 414  degrees of freedom
AIC: 970.05

Number of Fisher Scoring iterations: 5

> Start_m3 <<- m3$coefficients
> # # Performing Poisson Model
> # m2 <- glm(Total_formula,family = "poisson")
> # summary(m2)
> # Start_m2 <<- m2$coefficients
> # Test for Senior plot
> par(mfrow=c(2,2))
> plot(m3)
> Start_m1 <<- matrix(Start_m1,nrow = NROW(Start_m1),1)
> Start_m2 <<- matrix(Start_m2,nrow = NROW(Start_m2),1)
> Start_m3 <<- matrix(Start_m3,nrow = NROW(Start_m3),1)
>
> Start <<- rbind(Start_m1,Start_m2,Start_m3)
>
> # ===============================================================
> #              Maximum Simulated Likelihood For
> #             Multivariate Indpendent Count Model
> # ===============================================================
> # Now this Model is the one similar to the m1, m2 and m3 above, I will use
> # Negative Binomial Model for Young, Middel_Aged, and Poisson for Senior
>
> LLF2 <- function(b){
+
+   y1 <- Young
+   y2 <- Middle_age
+   y3 <- Senior
+   #========= Define the Varibles for the MSL=================
+   lmx1      <<- matrix(0,NROW(ux),1)
+   lmx2      <<- matrix(0,NROW(ux),1)
+   lmx3      <<- matrix(0,NROW(ux),1)
+   SPrz1     <<- matrix(0,NROW(ux),1)
+   SPrz2     <<- matrix(0,NROW(ux),1)
+   SPrz3     <<- matrix(0,NROW(ux),1)
+   P1        <<- matrix(0,NROW(ux),1)
+   P2        <<- matrix(0,NROW(ux),1)
+   P3        <<- matrix(0,NROW(ux),1)
+   LLT       <<- matrix(0,NROW(Data1),1)   # Probabilit variable for each indivdiual q
+
+     beta1  <-  b[1]
+     beta2  <-  b[2]
+     beta3  <-  b[3]
+     beta4  <-  b[4]
+     beta5  <-  b[5]
+     beta6  <-  b[6]
+     beta7  <-  b[7]
+     beta8  <-  b[8]
+     beta9  <-  b[9]
+     beta10 <-  b[10]
+     beta11 <-  b[11]
+     beta12 <-  b[12]
+     beta13 <-  b[13]
+     beta14 <-  b[14]
+     beta15 <-  b[15]
+     beta16 <-  b[16]
+     beta17 <-  b[17]
+     beta18 <-  b[18]
+     beta19 <-  b[19]
+     beta20 <-  b[20]
+     beta21 <-  b[21]
+     beta22 <-  b[22]
+     beta23 <-  b[23]
+     beta24 <-  b[24]
+     beta25 <-  b[25]
+     beta26 <-  b[26]
+     beta27 <-  b[27]
+     beta28 <-  b[28]
+     beta29 <-  b[29]
+     beta30 <-  b[30]
+     beta31 <-  b[31]
+     beta32 <-  b[32]
+     beta33 <-  b[33]
+     beta34 <-  b[34]
+     beta35 <-  b[35]
+     beta36 <-  b[36]
+     beta37 <-  b[37]
+     beta38 <-  b[38]
+     beta39 <-  b[39]
+     beta40 <-  b[40]
+     beta41 <-  b[41]
+     beta42 <-  b[42]
+     beta43 <-  b[43]
+     beta44 <-  b[44]
+     beta45 <-  b[45]
+     beta46 <-  b[46]
+     beta47 <-  b[47]
+     beta48 <-  b[48]
+     beta49 <-  b[49]
+     beta50 <-  b[50]
+     beta51 <-  b[51]
+     beta52 <-  b[52]
+     beta53 <-  b[53]
+     beta54 <-  b[54]
+     beta55 <-  b[55]
+     beta56 <-  b[56]
+     beta57 <-  b[57]
+     beta58 <-  b[58]
+     beta59 <-  b[59]
+     beta60 <-  b[60]
+
+     f1     <-  b[61]
+     f2     <-  b[62]
+     f3     <-  b[63]
+     f4     <-  b[64]
+     f5     <-  b[65]
+     f6     <-  b[66]
+
+ for (q in 1:NROW(Data1)) {
+     Sumx <<- matrix(0,NROW(ux),1)
+       for (r in 1:NROW(ux)){
+           lmx1[r] = exp(   beta1
+                          + beta2 * MinorPrefecturalRoad[q]
+                          + beta3 * OtherRoadTypes[q]
+                          + beta4 * Conf30KmhorLess[q]
+                          + beta5 * Conf40KmhorLess[q]
+                          + beta6 * Conf50KmhorLess[q]
+                          + beta7 * Conf60KmhorLess[q]
+                          + beta8 * ConfNoRegulation[q]
+                          + beta9 * LogTrafficVolume[q]
+                          + beta10* IntersTypeThreeArms[q]
+                          + beta11* LogShortestWidth[q]
+                          + beta12* LogNoDriveWays[q]
+                          + beta13* LogNoLanes[q]
+                          + beta14* NoLanesChanged[q]
+                          + beta15* IsThereSkewness[q]
+                          + beta16* NonDividedSigleRoadway[q]
+                          + beta17* LogAverageWidthPhysicalMedian[q]
+                          + beta18* IsThereCentralStrip[q]
+                          + beta19* SignalizedHighLevelSignal[q]
+                          + beta20* PedestrianSignalExisted[q]
+                          + f1 * ux[r,1])
+
+           lmx2[r] = exp(   beta21
+                          + beta22* MinorPrefecturalRoad[q]
+                          + beta23* OtherRoadTypes[q]
+                          + beta24* Conf30KmhorLess[q]
+                          + beta25* Conf40KmhorLess[q]
+                          + beta26* Conf50KmhorLess[q]
+                          + beta27* Conf60KmhorLess[q]
+                          + beta28* ConfNoRegulation[q]
+                          + beta29* LogTrafficVolume[q]
+                          + beta30* IntersTypeThreeArms[q]
+                          + beta31* LogShortestWidth[q]
+                          + beta32* LogNoDriveWays[q]
+                          + beta33* LogNoLanes[q]
+                          + beta34* NoLanesChanged[q]
+                          + beta35* IsThereSkewness[q]
+                          + beta36* NonDividedSigleRoadway[q]
+                          + beta37* LogAverageWidthPhysicalMedian[q]
+                          + beta38* IsThereCentralStrip[q]
+                          + beta39* SignalizedHighLevelSignal[q]
+                          + beta40* PedestrianSignalExisted[q]
+                          + f2 * ux[r,1]
+                          + f3 * ux[r,2])
+
+           lmx3[r] = exp(   beta41
+                          + beta42* MinorPrefecturalRoad[q]
+                          + beta43* OtherRoadTypes[q]
+                          + beta44* Conf30KmhorLess[q]
+                          + beta45* Conf40KmhorLess[q]
+                          + beta46* Conf50KmhorLess[q]
+                          + beta47* Conf60KmhorLess[q]
+                          + beta48* ConfNoRegulation[q]
+                          + beta49* LogTrafficVolume[q]
+                          + beta50* IntersTypeThreeArms[q]
+                          + beta51* LogShortestWidth[q]
+                          + beta52* LogNoDriveWays[q]
+                          + beta53* LogNoLanes[q]
+                          + beta54* NoLanesChanged[q]
+                          + beta55* IsThereSkewness[q]
+                          + beta56* NonDividedSigleRoadway[q]
+                          + beta57* LogAverageWidthPhysicalMedian[q]
+                          + beta58* IsThereCentralStrip[q]
+                          + beta59* SignalizedHighLevelSignal[q]
+                          + beta60* PedestrianSignalExisted[q]
+                          + f4 * ux[r,1]
+                          + f5 * ux[r,2]
+                          + f6 * ux[r,3])
+
+         # == Calculate the probability ========
+
+       P1[r] = exp((y1[q])*(log(lmx1[r]))-(lmx1[r])-lfactorial(y1[q]))
+       P2[r] = exp((y2[q])*(log(lmx2[r]))-(lmx2[r])-lfactorial(y2[q]))
+       P3[r] = exp((y3[q])*(log(lmx3[r]))-(lmx3[r])-lfactorial(y3[q]))
+
+       # ========== Probability of Zero ======
+       SPrz1[r] = exp(-lmx1[r])
+       SPrz2[r] = exp(-lmx2[r])
+       SPrz3[r] = exp(-lmx3[r])
+       # ========== Probability of Zero
+       # === It seems that R cant assign matrix to a constant value so you have to
+       # === Define the sum as a vector
+       # === Define the Truncated Probability Function
+       Sumx[r] = (P1[r]*P2[r]*P3[r])/(1-(SPrz1[r]*SPrz2[r]*SPrz3[r]))
+       #browser()
+       }
+     LLT[q] = sum(Sumx)/NROW(ux)
+   }
+   return(log(LLT))
+ }
>
>
> fx <<- matrix(1,6,1)    # Defind the variables of the
> #init_disp <- c((1/m1$theta),(1/m2$theta))
> #sig_vect <<-matrix(1,36,1)
> #=============================Call the function for test==================
> startx1 = c(Start,fx)  #,init_disp,sig_vect
> library(maxLik)
> ML2 <- maxLik(LLF2, start = startx1,method = "bfgs"
+               ,control=list(printLevel=4))
Initial function value: -1922.922
Initial gradient value:
 [1]  -44.757628  -11.905730  -13.851383   -2.832058  -24.607323  -29.543369
 [7]   -8.267229  -17.125656 -128.735495  -17.279764 -142.105939  -36.860840
[13]  -99.811760  -22.692711  -29.158432  -17.192199   -5.090032  -20.398156
[19]   -7.900705  -23.834912  -27.168621   -9.941738   -4.343192   -2.343420
[25]   -9.382725   -7.238741   -2.795040   -1.621885  -68.433970  -20.718212
[31]  -72.704785  -25.971151  -51.540310   -6.718055  -16.813878  -16.741929
[37]   -2.035727   -4.906827    1.526277   -7.392086  -44.871035  -16.269395
[43]  -11.157939   -2.018616  -31.506754  -27.198048   -9.937463  -18.741798
[49] -136.634983  -15.090508 -142.089986  -39.953540 -100.989137  -25.924945
[55]  -26.378166  -14.280105   -5.944095  -23.837054   -8.123629  -24.971909
[61]  -38.493676  -87.740546 -117.530362  -15.137458  -18.258004  -80.039901
initial  value 1922.921584
iter   2 value 1887.621853
iter   3 value 1872.832218
iter   4 value 1864.559233
iter   5 value 1775.524407
iter   6 value 1743.779528
iter   7 value 1725.209832
iter   8 value 1706.973243
iter   9 value 1694.003282
iter  10 value 1691.457720
iter  11 value 1690.198913
iter  12 value 1690.028175
iter  13 value 1689.700978
iter  14 value 1689.523993
iter  15 value 1689.231435
iter  16 value 1688.887029
iter  17 value 1688.473902
iter  18 value 1688.094623
iter  19 value 1687.456148
iter  20 value 1686.755733
iter  21 value 1686.305151
iter  22 value 1686.108681
iter  23 value 1685.608677
iter  24 value 1685.222306
iter  25 value 1684.925262
iter  26 value 1684.711374
iter  27 value 1684.522296

```
