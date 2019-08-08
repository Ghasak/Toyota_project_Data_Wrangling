clear
cls
// Change the scroll buffer size usign the command line
set scrollbufsize 300000
// Input dataset - using excel
import excel "/Users/ghasak/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/STATA/refined_df.xlsx", sheet("DataSet") firstrow

// Selected Variables
// Major_prefectural_road Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume traffic_volume_dummy T_or_staggered_intersection Y_shape_intersection LOG_NO_DRIVE_WAYS LOG_DISTANCE_TO_ADJUST LOG_LONGEST_WIDTH_INTER LOG_SHORTEST_WIDTH_INTER LOG_AVERAGE_RADIUS DIVIDED_NO_CENTRAL_DIVISION DIVIDED_WITH_CENTRAL_DIVISION DIVIDED_NO_PHYSICAL_DIVISION DIVIDED_WITH_PHYSICAL_DIVISION NON_DIVIDED_SINGLE_ROADWAY LOG_NUMBER_OF_LANES NO_OF_LANES_CHANGED LEFT_TURN_EXCLUSIVE_LANE RIGHT_TURN_EXCLUSIVE_LANE LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA LOG_AVERAGE_WIDTH_CENTRAL_STRIP IS_THERE_PHYSICAL_MEDIAN IS_THERE_CENTRAL_STRIP SIGNALIZED_HIGH_LEVEL_SIGNAL SIGNALIZED_REGULAR_SIGNAL OTHERS_SIGNALS FLASHING_GREEN_PED


// Base Mode - Univariate Poisson Model
// The model is used as a base-model for selecting the most significant variables, later we will introduce the error-term following log-norm

// Total Crush count
// To move to second line in the do-coding use (///)

poisson Crash_count Major_prefectural_road Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume


/**
 Not-Significant variables:
 - General_national_road

*/
// Step-2- Adding the variables of intersection geometry
poisson Crash_count Major_prefectural_road Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume  T_or_staggered_intersection Y_shape_intersection LOG_NO_DRIVE_WAYS LOG_DISTANCE_TO_ADJUST LOG_SHORTEST_WIDTH_INTER LOG_AVERAGE_RADIUS

// Step-3- Adding variables of intersection layout (combine all arms in single variable each)

poisson Crash_count Major_prefectural_road Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume  T_or_staggered_intersection Y_shape_intersection LOG_NO_DRIVE_WAYS LOG_DISTANCE_TO_ADJUST LOG_SHORTEST_WIDTH_INTER   NON_DIVIDED_SINGLE_ROADWAY  LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED


poisson Crash_count Major_prefectural_road Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume  T_or_staggered_intersection Y_shape_intersection LOG_NO_DRIVE_WAYS  LOG_SHORTEST_WIDTH_INTER   NON_DIVIDED_SINGLE_ROADWAY  LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED  LEFT_TURN_EXCLUSIVE_LANE  LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA   IS_THERE_CENTRAL_STRIP   SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED

poisson Crash_count Major_prefectural_road Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume  T_or_staggered_intersection Y_shape_intersection LOG_NO_DRIVE_WAYS  LOG_SHORTEST_WIDTH_INTER   NON_DIVIDED_SINGLE_ROADWAY  LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED  LEFT_TURN_EXCLUSIVE_LANE  LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA   IS_THERE_CENTRAL_STRIP   SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED

// For total number of accidents - The mode we will use so far:
poisson Crash_count  Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume    IS_IT_THREE_ARMS LOG_NO_DRIVE_WAYS  LOG_SHORTEST_WIDTH_INTER   NON_DIVIDED_SINGLE_ROADWAY  LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED  LEFT_TURN_EXCLUSIVE_LANE  LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA   IS_THERE_CENTRAL_STRIP   SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED

estat ic
estimates store Poisson_Total_Crash
// Using NBII mode we get:
nbreg Crash_count Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume    IS_IT_THREE_ARMS LOG_NO_DRIVE_WAYS  LOG_SHORTEST_WIDTH_INTER   NON_DIVIDED_SINGLE_ROADWAY  LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED  LEFT_TURN_EXCLUSIVE_LANE  LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA   IS_THERE_CENTRAL_STRIP   SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED, dispersion(constant)

estat ic
estimates store NBII_Total_Crash
predict NBII_TOTAL_CRASH
summarize NBII_TOTAL_CRASH Crash_count
// Estimate the Log-likelhood Ratio Test between the two models
lrtest (Poisson_Total_Crash) (NBII_Total_Crash), stats dir force
// hausman test for parameter equality -
hausman NBII_Total_Crash Poisson_Total_Crash, force
disp("There is a difference in coefficients and it is systematic")

//======================================================================================
//                  Univariate NBII Model - Total Number of Crashes
//======================================================================================
/**
    - Selecting Most Siginifcant using Method C
        - Total number of crashes is the baseline.
        - add all the variables and start trimming one by one.
        - Select the most significant variables.
*/
summarize Crash_count Driver_Young Driver_Middle_age Driver_Senior  Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume IS_IT_THREE_ARMS LOG_SHORTEST_WIDTH_INTER LOG_NO_DRIVE_WAYS LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED IS_THERE_SKEWNESS NON_DIVIDED_SINGLE_ROADWAY    LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA  IS_THERE_CENTRAL_STRIP    SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED

poisson Crash_count  Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume IS_IT_THREE_ARMS LOG_SHORTEST_WIDTH_INTER LOG_NO_DRIVE_WAYS LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED IS_THERE_SKEWNESS NON_DIVIDED_SINGLE_ROADWAY    LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA  IS_THERE_CENTRAL_STRIP    SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED
estimates store poisson_final_total


nbreg Crash_count  Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume IS_IT_THREE_ARMS LOG_SHORTEST_WIDTH_INTER LOG_NO_DRIVE_WAYS LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED IS_THERE_SKEWNESS NON_DIVIDED_SINGLE_ROADWAY    LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA  IS_THERE_CENTRAL_STRIP    SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED  , dispersion(constant)
estimates store nbII_final_total

//  ----------------------------------------------------------
//  --------------- Calculate the Incident Ratio -------------
//  ----------------------------------------------------------
nbreg, irr
disp("Notice that the results is similar if you take: exp(bi)")
disp("Read here: https://stats.idre.ucla.edu/stata/dae/negative-binomial-regression/")
//  ----------------------------------------------------------
//  --------------- Calculate the Marginal Effect ------------
//  ----------------------------------------------------------

margins, dydx(_all) atmeans


// Estimate the Log-likelhood Ratio Test between the two models
lrtest (poisson_final_total) (nbII_final_total), stats dir force

// hausman test for parameter equality -
hausman nbII_final_total poisson_final_total, force
disp("There is not that big difference in coefficients and it is not systematic")
// Non-Sig Variables across all drivers types
/*
General_national_road
Major_prefectural_road
LOG_NO_DRIVE_WAYS
LOG_DISTANCE_TO_ADJUST
LOG_MAX_RADIUS
LOG_MIN_RADIUS
LOG_AVERAGE_RADIUS
LEFT_TURN_EXCLUSIVE_LANE

*/

/**
        - After finishing all significant variables now we go to Conclusion:

            LOG_LONGEST_WIDTH_INTER: This variable more significant to Young Drivers compare to the Senior Drivers
                which means Young drivers either travel alot inside intersection labled as
*/

/*
The user-written fitstat command (as well as Stata’s estat commands) can be used to obtain additional model fit information that may be helpful if you want to compare models.  You can type search fitstat to download this program (see How can I use the search command to search for programs and get additional help? for more information about using search).
search fitstat
download:
                    fitstat from http://fmwww.bc.edu/RePEc/bocode/f
                        'FITSTAT': module to compute fit statistics for single equation regression
                        models / fitstat is a post-estimation command that computes a variety of /
                        measures of fit for many kinds of regression models. It works / after the
                        following: clogit, cnreg, cloglog, intreg, logistic, / logit, mlogit,

*/
 fitstat


//======================================================================================
//                  Univariate Count Model - Young Drivers Crashes
//======================================================================================


poisson Driver_Young Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume IS_IT_THREE_ARMS LOG_SHORTEST_WIDTH_INTER LOG_NO_DRIVE_WAYS LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED IS_THERE_SKEWNESS NON_DIVIDED_SINGLE_ROADWAY    LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA  IS_THERE_CENTRAL_STRIP    SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED
estimates store Poisson_Young_Drivers


nbreg Driver_Young Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume IS_IT_THREE_ARMS LOG_SHORTEST_WIDTH_INTER LOG_NO_DRIVE_WAYS LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED IS_THERE_SKEWNESS NON_DIVIDED_SINGLE_ROADWAY    LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA  IS_THERE_CENTRAL_STRIP    SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED, dispersion(constant)
estimates store NBII_Young_Drivers

//  ----------------------------------------------------------
//  ----- Log-Likelihood between Poisson and NBII ------------
//  ----- Young Dirvers
//  ----------------------------------------------------------
// Estimate the Log-likelhood Ratio Test between the two models
lrtest (Poisson_Young_Drivers) (NBII_Young_Drivers), stats dir force
//  ----------------------------------------------------------
//  ----- Hausman test   between Poisson and NBII ------------
//  ----- Young Dirvers
//  ----------------------------------------------------------
// hausman test for parameter equality -
hausman NBII_Young_Drivers Poisson_Young_Drivers, force
disp("There is a difference in coefficients and it is systematic")


//======================================================================================
//                  Univariate Count Model - Middle Aged Drivers Crashes
//======================================================================================

poisson Driver_Middle_age Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume IS_IT_THREE_ARMS LOG_SHORTEST_WIDTH_INTER LOG_NO_DRIVE_WAYS LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED IS_THERE_SKEWNESS NON_DIVIDED_SINGLE_ROADWAY    LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA  IS_THERE_CENTRAL_STRIP    SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED
estimates store Poisson_Middle_Aged_Drivers


nbreg Driver_Middle_age Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume IS_IT_THREE_ARMS LOG_SHORTEST_WIDTH_INTER LOG_NO_DRIVE_WAYS LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED IS_THERE_SKEWNESS NON_DIVIDED_SINGLE_ROADWAY    LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA  IS_THERE_CENTRAL_STRIP    SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED, dispersion(constant)
estimates store NBII_Middle_Aged_Drivers

//  ----------------------------------------------------------
//  ----- Log-Likelihood between Poisson and NBII ------------
//  ----- Young Dirvers
//  ----------------------------------------------------------
// Estimate the Log-likelhood Ratio Test between the two models
lrtest (Poisson_Middle_Aged_Drivers) (NBII_Middle_Aged_Drivers), stats dir force
//  ----------------------------------------------------------
//  ----- Hausman test   between Poisson and NBII ------------
//  ----- Young Dirvers
//  ----------------------------------------------------------
// hausman test for parameter equality -
hausman NBII_Middle_Aged_Drivers Poisson_Middle_Aged_Drivers, force
disp("There is a difference in coefficients and it is systematic")


//======================================================================================
//                  Univariate Count Model - Senior Drivers Crashes
//======================================================================================

poisson Driver_Senior Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume IS_IT_THREE_ARMS LOG_SHORTEST_WIDTH_INTER LOG_NO_DRIVE_WAYS LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED IS_THERE_SKEWNESS NON_DIVIDED_SINGLE_ROADWAY    LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA  IS_THERE_CENTRAL_STRIP    SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED
estimates store Poisson_Senior_Drivers


nbreg Driver_Senior Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume IS_IT_THREE_ARMS LOG_SHORTEST_WIDTH_INTER LOG_NO_DRIVE_WAYS LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED IS_THERE_SKEWNESS NON_DIVIDED_SINGLE_ROADWAY    LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA  IS_THERE_CENTRAL_STRIP    SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED, dispersion(constant)
estimates store NBII_Senior_Drivers

//  ----------------------------------------------------------
//  ----- Log-Likelihood between Poisson and NBII ------------
//  ----- Young Dirvers
//  ----------------------------------------------------------
// Estimate the Log-likelhood Ratio Test between the two models
lrtest (Poisson_Senior_Drivers) (NBII_Senior_Drivers), stats dir force
//  ----------------------------------------------------------
//  ----- Hausman test   between Poisson and NBII ------------
//  ----- Young Dirvers
//  ----------------------------------------------------------
// hausman test for parameter equality -
hausman NBII_Senior_Drivers Poisson_Senior_Drivers, force
disp("There is a difference in coefficients and it is systematic")
