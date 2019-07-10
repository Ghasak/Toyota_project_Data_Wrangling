import excel "/Users/ghasak/Desktop/Toyota_Project_Data_Wrangling/3_Toyota_Data_Modeling/DATASET/Final_DataSet.xlsx", sheet("DataSet") firstrow
// Cleaning Some Variables and converate them from string to int or float
destring Radius_of_arm_3_and_arm_4_, replace force float percent dpcomma
destring Radius_of_arm_3_and_arm_4_, replace force float percent dpcomma
destring Width_of_central_strip_of_first_, replace force float percent dpcomma
destring Width_of_central_strip_of_first_, replace force float percent dpcomma


// Crash Count for Total and each age category:
summarize  Crash_count Driver_Young Driver_Middle_age Driver_Senior

// General-Intersection Road Type location of Intersection.
summarize  High_speed General_national_road Major_prefectural_road Minor_prefectural_road Narrow_road Prefectural_Dummy_new

// 
