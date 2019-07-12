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
// intersection radius variables
summarize  Radius_of_arm_1_and_arm_2_ Radius_of_arm_2_and_arm_3_ Radius_of_arm_3_and_arm_4_ Radius_of_arm_4_and_arm_5_ Radius_of_arm_5_and_arm_6_ Radius_of_arm_6_and_arm_7_
// No. of arms for a given intersection (related to the intersection type)
summarize  Three_arms Four_arms Five_arms Six_arms

// ======================================================================================================
// Variables of First Arm
// Road type of first arm
summarize  Arm1_RoadType_Divided_roadway_wi BL BM BN Arm1_RoadType_One_way_street Arm1_RoadType_Single_roadway_wit

// Intersection characteristics-related to approaches
summarize  Arm1_Number_of_lanes_for_first_a Arm1_No_of_lanes_changed_at_the_ Left_turn_only_lane_for_first_ar Right_turn_only_lane_for_first_a Width_of_Pysical_Median_of_first Is_there_Physical_Median_first_a Width_of_central_strip_of_first_ Is_there_centeral_strip_first_ar Skewness_level_of_first_arm_to_t

// Traffic signal characteristics
summarize  Arm1_RedYellow_flashing_signal Arm1_Stop_sign Arm1_Traffic_signal_with_left_or Arm1_Traffic_signal_without_left Arm1_Uncontroled Arm1_Presence_of_pedestrian_traf

// Intersection characteristics-related to pedestrains and bicyclists
// Bicycles
summarize  Arm1_Crossing_path_without_bicyc Arm1_Crosswalk_existed_within_50 Arm1_Crosswalk_path_with_bicycle
// Sidewalk
summarize  Arm1_1stSide_No_sidewalk Arm1_1stSide_Sidewalk_with_curbs Arm1_1stSide_Sidewalk_with_guard Arm1_1stSide_Sidewalk_without_an Arm1_2ndSide_No_sidewalk Arm1_2ndSide_Sidewalk_with_curbs Arm1_2ndSide_Sidewalk_with_guard Arm1_2ndSide_Sidewalk_without_an

// ======================================================================================================
// Variables of Second Arm
// Road type of second arm

summarize  Arm2_Divided_roadway_with_No_Phy CR Arm2_Divided_roadway_with_Physic CT Arm2_One_way_street Arm2_Single_roadway_without_cent

// Intersection characteristics-related to approaches
summarize  Arm2_Number_of_lanes_for_second_ Arm2_No_of_lanes_changed_at_the_ Left_turn_only_lane_for_second_a Right_turn_only_lane_for_second_ Width_of_Pysical_Median_of_secon Is_there_Physical_Median_second_ Width_of_central_strip_of_second Is_there_centeral_strip_second_a Skewness_level_of_second_arm_to_


// Traffic signal characteristics
summarize  Arm2_RedYellow_flashing_signal Arm2_Stop_sign Arm2_Traffic_signal_with_left_or Arm2_Traffic_signal_without_left Arm2_Uncontroled Arm2_Presence_of_pedestrian_traf


// Intersection characteristics-related to pedestrains and bicyclists
// Bicycles
summarize  Arm2_Crossing_path_without_bicyc Arm2_Crosswalk_existed_within_50 Arm2_Crosswalk_path_with_bicycle

// Sidewalk
summarize  Arm2_1stSide_No_sidewalk Arm2_1stSide_Sidewalk_with_curbs Arm2_1stSide_Sidewalk_with_guard Arm2_1stSide_Sidewalk_without_an Arm2_2ndSide_No_sidewalk Arm2_2ndSide_Sidewalk_with_curbs Arm2_2ndSide_Sidewalk_with_guard Arm2_2ndSide_Sidewalk_without_an


// ======================================================================================================
// Variables of Third Arm
// Road type of Third arm

 summarize Arm3_Divided_roadway_with_No_Phy DX Arm3_Divided_roadway_with_Physic DZ Arm3_One_way_street Arm3_Single_roadway_without_cent
// Intersection characteristics-related to approaches
 summarize  Arm3_Number_of_lanes_for_third_a Arm3_No_of_lanes_changed_at_the_ Left_turn_only_lane_for_third_ar Right_turn_only_lane_for_third_a Width_of_Pysical_Median_of_third Is_there_Physical_Median_third_a Width_of_central_strip_of_third_ Is_there_centeral_strip_third_ar  Skewness_level_of_third_arm_to_t


// Traffic signal characteristics
summarize  Arm3_RedYellow_flashing_signal Arm3_Stop_sign Arm3_Traffic_signal_with_left_or Arm3_Traffic_signal_without_left Arm3_Uncontroled Arm3_Presence_of_pedestrian_traf


// Intersection characteristics-related to pedestrains and bicyclists
// Bicycles
summarize  Arm3_PedandBi_Crossing_path_with Arm3_PedandBi_Crosswalk_existed_ Arm3_PedandBi_Crosswalk_path_wit
// Sidewalk
summarize  Arm3_1stSide_No_sidewalk Arm3_1stSide_Sidewalk_with_curbs Arm3_1stSide_Sidewalk_with_guard Arm3_1stSide_Sidewalk_without_an Arm3_2ndSide_No_sidewalk Arm3_2ndSide_Sidewalk_with_curbs Arm3_2ndSide_Sidewalk_with_guard Arm3_2ndSide_Sidewalk_without_an

// ======================================================================================================
// Variables of Fourth Arm
// Road type of Fourth arm
summarize  Arm4_Road_type_Divided_roadway_w FD FE FF Arm4_Road_type_Non_Existed Arm4_Road_type_One_way_street Arm4_Road_type_Single_roadway_wi
// Intersection characteristics-related to approaches
summarize  Arm4_Number_of_lanes_for_fourth_ Arm4_No_of_lanes_changed_at_the_ Left_turn_only_lane_for_fourth_a Right_turn_only_lane_for_fourth_ Width_of_Pysical_Median_of_fourt Is_there_Physical_Median_fourth_ Width_of_central_strip_of_fourth Is_there_centeral_strip_fourth_a Skewness_level_of_fourth_arm_to_
// Traffic signal characteristics
summarize  Arm4_TrafSig_RedYellow_flashing_ Arm4_TrafSig_Stop_sign Arm4_TrafSig_Traffic_signal_with GH Arm4_TrafSig_Uncontroled Arm4_Presence_of_pedestrian_traf
// Intersection characteristics-related to pedestrains and bicyclists
// Bicycles
summarize  Arm4_PedandBic_Crossing_path_wit Arm4_PedandBic_Crosswalk_existed Arm4_PedandBic_Crosswalk_path_wi Arm4_PedandBic_Non_Existed
// Sidewalk
summarize  Arm4_1stSide_No_sidewalk Arm4_1stSide_Sidewalk_with_curbs Arm4_1stSide_Sidewalk_with_guard Arm4_1stSide_Sidewalk_without_an Arm4_2ndSide_No_sidewalk Arm4_2ndSide_Sidewalk_with_curbs Arm4_2ndSide_Sidewalk_with_guard Arm4_2ndSide_Sidewalk_without_an

// ======================================================================================================
// Variables of Fifth and sixth Arm
// Road type of Fifth and sixth arm
summarize  Arm5_6_Road_type_Divided_roadway Arm5_6_Road_type_Non_Existed
// Intersection characteristics-related to approaches
summarize  Arm5_6_Numer_of_lanes_larger_tha Arm5_6_No_of_lanes_changed_large Left_turn_only_lane_larger_than_ Right_turn_only_lane_larger_than Width_of_Physical_Median_larger_ Is_there_Physical_Median_five_ar Width_of_centeral_strip_larger_t Is_there_centeral_strip_five_arm Skewness_level_larger_than_four
// Traffic signal characteristics
 summarize  Arm5_6_TrafSig_UncontroledStop_s Arm5_6_Presence_of_pedestrian_tr
// Intersection characteristics-related to pedestrains and bicyclists
// Bicycles
summarize  Arm5_6_PedandBi_Crossing_path_wi
// Sidewalk
 summarize  Arm5_6_1stSide_No_sidewalk Arm5_6_1stSide_Sidewalk_with_cur Arm5_6_2ndSide_No_sidewalkNo_sid
// ======================================================================================================
//									Variables generated for seeking significance vars.
// ======================================================================================================

// ----------- Minimum radius of intersection -------------
gen minumum_radius = min( Radius_of_arm_1_and_arm_2_, Radius_of_arm_2_and_arm_3_, Radius_of_arm_3_and_arm_4_, Radius_of_arm_4_and_arm_5_, Radius_of_arm_5_and_arm_6_, Radius_of_arm_6_and_arm_7_)
gen log_minimum_radius = log(minumum_radius)
// ----------- Maximum radius of intersection -------------
gen maximum_radius = max( Radius_of_arm_1_and_arm_2_, Radius_of_arm_2_and_arm_3_, Radius_of_arm_3_and_arm_4_, Radius_of_arm_4_and_arm_5_, Radius_of_arm_5_and_arm_6_, Radius_of_arm_6_and_arm_7_)
gen log_maximum_radius = log(maximum_radius)

// ======================================================================================================
//									Univaraite Count Modeling
// ======================================================================================================

// ----------- Univariate NBII Model -------------
nbreg Crash_count Prefectural_Dummy_new Minor_prefectural_road Narrow_road conf1_30kmh_orless conf1_40kmh_orless conf1_50kmh_orless conf1_60kmh_orless conf1_No_regulation log_traffic_volume traffic_volume_dummy T_or_staggered_intersection Y_shape_intersection Intersection_with_more_than_four Cross_intersection (Number_of_driverways) Distance_to_adjacent_intersectio Longest_Width_of_intersection Shortest_Width_of_intersection maximum_radius log_maximum_radius Arm1_RoadType_Divided_roadway_wi BL BM BN Arm1_RoadType_One_way_street Arm1_RoadType_Single_roadway_wit Arm1_Number_of_lanes_for_first_a Arm1_No_of_lanes_changed_at_the_ Left_turn_only_lane_for_first_ar Right_turn_only_lane_for_first_a Width_of_Pysical_Median_of_first Is_there_Physical_Median_first_a Width_of_central_strip_of_first_ Is_there_centeral_strip_first_ar Skewness_level_of_first_arm_to_t Arm1_RedYellow_flashing_signal Arm1_Stop_sign Arm1_Traffic_signal_with_left_or Arm1_Traffic_signal_without_left Arm1_Uncontroled Arm1_Presence_of_pedestrian_traf Arm1_Crossing_path_without_bicyc Arm1_Crosswalk_existed_within_50 Arm1_Crosswalk_path_with_bicycle Arm1_1stSide_No_sidewalk Arm1_1stSide_Sidewalk_with_curbs Arm1_1stSide_Sidewalk_with_guard Arm1_1stSide_Sidewalk_without_an Arm1_2ndSide_No_sidewalk Arm1_2ndSide_Sidewalk_with_curbs Arm1_2ndSide_Sidewalk_with_guard Arm1_2ndSide_Sidewalk_without_an, dispersion(constant)
estat ic

// ======================================================================================================
// Determine which model to use Poisson or NBII by running NBII first and examine the LL of
// likelihood-ratio test, Starting with Total Crash Count-Univaraite non-truncated poisson model
// ======================================================================================================

// ======================================================================================================
// Univariate non-truncated NBII model with constant dispersion
// ======================================================================================================
nbreg Crash_count  General_national_road Major_prefectural_road Minor_prefectural_road Narrow_road , dispersion(constant)

















