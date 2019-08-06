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
nbreg Crash_count   Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume    IS_IT_THREE_ARMS LOG_NO_DRIVE_WAYS  LOG_SHORTEST_WIDTH_INTER   NON_DIVIDED_SINGLE_ROADWAY  LOG_NUMBER_OF_LANES  NO_OF_LANES_CHANGED  LEFT_TURN_EXCLUSIVE_LANE  LOG_AVERAGE_WIDTH_PHYSICAL_MEDIA   IS_THERE_CENTRAL_STRIP   SIGNALIZED_HIGH_LEVEL_SIGNAL FLASHING_GREEN_PED, dispersion(constant)

estat ic
estimates store NBII_Total_Crash

// Estimate the Log-likelhood Ratio Test between the two models
lrtest (Poisson_Total_Crash) (NBII_Total_Crash), stats dir force
// hausman test for parameter equality -
hausman NBII_Total_Crash Poisson_Total_Crash, force
disp("There is a difference in coefficients and it is systematic")

