import excel "/Users/ghasak/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/DATASET/Final_DataSet.xlsx", sheet("DataSet") firstrow
// Cleaning Some Variables and converate them from string to int or float
destring Radius_of_arm_3_and_arm_4_, replace force float percent dpcomma
destring Radius_of_arm_3_and_arm_4_, replace force float percent dpcomma
destring Width_of_central_strip_of_first_, replace force float percent dpcomma
destring Width_of_central_strip_of_first_, replace force float percent dpcomma


// Crash Count for Total and each age category:
summarize  Crash_count Driver_Young Driver_Middle_age Driver_Senior

// General-Intersection Road Type location of Intersection.
summarize  High_speed Prefectural_Dummy_new General_national_road Major_prefectural_road Minor_prefectural_road Narrow_road 

// Road width by a variable collected by the police report - from Usui sensei dataset. 

// First configuration
summarize  conf1_Less_than_35_m conf1_35_m_or_more conf1_55_m_or_more conf1_90_m_or_more conf1_130_or_more conf1_195_m_or_more
// Second configuration
summarize  conf2_Between_Less35_and_55m conf2_55_m_or_more conf2_90_m_or_more conf2_130_or_more
// Third configuration
summarize  conf3_Narrow_road conf3_One_lane conf3_Two_to_Three_lanes conf3_larger_than_Four_lanes

// Road width by Usui sensei calculation using the map matching information
summarize Width30m_or_less Width30m_and_less_55m Width_55m_and_less_130m Width_130m_or_more

// Speed regulation by map matching -Usui sensei data
// First confguration
summarize  conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation
// Second configuration
summarize  conf2_Low_speed_limit conf2_Medium_speed_limit conf2_High_speed_limit conf2_No_regulation

// Traffic Volume information
summarize  traffic_volume log_traffic_volume traffic_volume_dummy log_traffic_volume_2

// ======================================================================================================
// 										Intersection-Survey variables
// ======================================================================================================
// General variables
// Intersection Type (Cross-Intersectin ..etc)
summarize   T_or_staggered_intersection Y_shape_intersection Cross_intersection Intersection_with_more_than_four Other_shapes
// Variables related to intersection geometry
summarize  Number_of_driverways Distance_to_adjacent_intersectio Longest_Width_of_intersection Shortest_Width_of_intersection


// ======================================================================================================


























