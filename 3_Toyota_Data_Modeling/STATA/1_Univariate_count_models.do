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
summarize  conf1_Less_than_35_m conf1_35_m_or_more conf1_55_m_or_more conf1_90_m_or_more conf1_130_or_more conf1_195_m_or_more

// Road width by Usui sensei calculation using the map matching information
summarize  conf2_Between_Less35_and_55m conf2_55_m_or_more conf2_90_m_or_more conf2_130_or_more
