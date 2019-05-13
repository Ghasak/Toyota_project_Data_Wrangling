"""
    We will Run now the program again this time we would do:
        - We will try to use the Piovt table tool to obtain the intersections.
"""
# ==================================================#
#           Import Libraries
# ==================================================#
# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
sns.set_style('darkgrid')
import os
Current_Path = os.getcwd()
# ==================================================#
#           Import Toyota Data Using Panda
# ==================================================#
# This time we will use the Excel Import Data where we can get all information in Japanese to clean them later.
Acc_ID_Final = pd.read_excel("3_Acc_ID_Final.xlsx", sheet_name=0)
# ==================================================#
#           Accessing Data in Panda
# ==================================================#
Acc_ID_Final = Acc_ID_Final.set_index(['Acc_ID'])  #set_index(['Acc_ID', 'Year'])
# Acc_ID_Final['Year'] = pd.to_datetime(Acc_ID_Final['Year'])
# ==================================================#
#     Cleaning Data and Preparing for Pivoting
# ==================================================#
# ---[variable No. (1)]-------------------"Weather"-------------------------
# 晴 Sunny   5004
# 曇 Cloudy  1074
# 雨 Rain    851
# 雪 Snow    14
# 霧 Fog     4
Acc_ID_Final['Weather'].value_counts()
cleanup_nums0_0 = {'晴':'Sunny','曇':'Cloud','雨':'Rain', '雪':'Snow', '霧': 'Fog'}
Acc_ID_Final['Weather1']= Acc_ID_Final["Weather"].replace(cleanup_nums0_0)
Acc_ID_Final['Weather1'].value_counts()
cleanup_nums0_1 = {'晴':1,'曇':2,'雨':3, '雪':4, '霧': 5}
Acc_ID_Final['Weather2']= Acc_ID_Final["Weather"].replace(cleanup_nums0_1)
Acc_ID_Final['Weather2'].value_counts()
# ---[variable No. (2)]-------------------"Accident Information内容"-------------------------
# We will start with the variable of the Severity_level
# Lets check the sample size of each Severity level
# 軽傷事故 Severity Level [1] meaning: Minor injury accident      sample size: 6655
len(Acc_ID_Final["Accident Information内容"][Acc_ID_Final["Accident Information内容"] == '軽傷事故'])
# 重傷事故 Severity Level [2] meaning: Serious injury accident    sample size: 257
len(Acc_ID_Final["Accident Information内容"][Acc_ID_Final["Accident Information内容"] == '重傷事故'])
# 死亡事故 Severity Level [3] meaning: Fatal Accident             sample size: 35
len(Acc_ID_Final["Accident Information内容"][Acc_ID_Final["Accident Information内容"] == '死亡事故'])
# Or simply use
Acc_ID_Final["Accident Information内容"].value_counts()
# <Method 1> Here we will replace the existing column [variable] entirly
# Now we will converate the column to these codes above or given them a name
# cleanup_nums = {"Accident Information内容":{'軽傷事故':1,'重傷事故':2,'死亡事故':3}}
# Acc_ID_Final.replace(cleanup_nums)
#<Method 2> Here we will create a new variable and add it to the data
# Drop the index of (Year) as it cause a problem here,
cleanup_nums1 = {'軽傷事故':'light_injury','重傷事故':'Serious_injury','死亡事故':'Fatal_injury'}
Acc_ID_Final['Severity_level1']= Acc_ID_Final["Accident Information内容"].replace(cleanup_nums1)
Acc_ID_Final['Severity_level1'].value_counts()
cleanup_nums2 = {'軽傷事故':1,'重傷事故':2,'死亡事故':3}
Acc_ID_Final['Severity_level2']= Acc_ID_Final["Accident Information内容"].replace(cleanup_nums2)
Acc_ID_Final['Severity_level2'].value_counts()
# ---[variable No. (3)]-------------------"Accident type"-------------------------
Acc_ID_Final['Accident type'].value_counts()
# 出合頭       # collision         3465
# その他       # Other             2966
# 横断中       # In transit        442  # for pederstrain with vehicle
# 車両単独      # Vehicle alone     56   # Only the vehicle make accident
# 正面衝突      # Frontal collision 18   # Frontal collision
cleanup_nums3_1 = {'出合頭':'Collision','その他':'Other','横断中':'In_transit', '車両単独':'Vehicle_alone','正面衝突':'Frontal_collision'}
Acc_ID_Final["Accident type1"]= Acc_ID_Final["Accident type"].replace(cleanup_nums3_1)
Acc_ID_Final['Accident type1'].value_counts()
cleanup_nums3_2 = {'出合頭':1,'その他':2,'横断中':3, '車両単独':4,'正面衝突':5}
Acc_ID_Final["Accident type2"]= Acc_ID_Final["Accident type"].replace(cleanup_nums3_2)
Acc_ID_Final['Accident type2'].value_counts()
# ---[variable No. (4)]-------------------"Accident type"-------------------------
Acc_ID_Final['Actor type'].value_counts()

# 普通乗用車        Regular passenger car      4476
# 軽乗用車          Light passenger car       1477
# 普通貨物車        Normal freight car         428
# 軽貨物車          Light truck                423
# 大型貨物車        Large cargo truck          79
# 中型貨物車        Medium-size freight car    38
# 中型乗用車        Medium-sized passenger car 14
# 大型乗用車        Large car                  10
# ミニカー          Minicar                    1
# 大型特殊車        Large special car          1
cleanup_nums4_1 = { '普通乗用車' :  'Regular_pass_car',
                    '軽乗用車'   :  'Light_pass_car',
                    '普通貨物車' :  'Normal_freight_car',
                    '軽貨物車'   :  'Light_truck',
                    '大型貨物車' :  'Large_cargo_truck',
                    '中型貨物車' :  'Medium_size_freight_car',
                    '中型乗用車' :  'Medium_size_pass_car',
                    '大型乗用車' :  'large_car',
                    'ミニカー'   :  'Minicar',
                    '大型特殊車' :  'Large_special_car'
                      }
Acc_ID_Final['Actor type1']= Acc_ID_Final['Actor type'].replace(cleanup_nums4_1)
Acc_ID_Final['Actor type1'].value_counts()
cleanup_nums4_2 = { '普通乗用車' :  1,
                    '軽乗用車'   :  2,
                    '普通貨物車' :  3,
                    '軽貨物車'   :  4,
                    '大型貨物車' :  5,
                    '中型貨物車' :  6,
                    '中型乗用車' :  7,
                    '大型乗用車' :  8,
                    'ミニカー'   :  9,
                    '大型特殊車' :  10
                      }
Acc_ID_Final['Actor type2']= Acc_ID_Final['Actor type'].replace(cleanup_nums4_2)
Acc_ID_Final['Actor type2'].value_counts()
# ---[variable No. (5)]-------------------"Transportation"-------------------------
Acc_ID_Final['Transportation'].value_counts()
cleanup_nums5 = {'自動車':'Automobile'}
Acc_ID_Final['Transportation1']= Acc_ID_Final["Transportation"].replace(cleanup_nums5)
Acc_ID_Final['Transportation1'].value_counts()
# ---[variable No. (6)]-------------------"1st_Actor_Transportation"-------------------------
Acc_ID_Final['1st_Actor_Transportation'].value_counts()
cleanup_nums6 = {'自動車':'Automobile'}
Acc_ID_Final['1st_Actor_Transportation1']= Acc_ID_Final["1st_Actor_Transportation"].replace(cleanup_nums6)
Acc_ID_Final['1st_Actor_Transportation1'].value_counts()
# ---[variable No. (7)]-------------------"2nd_Actor_Transportation"-------------------------
Acc_ID_Final['2nd_Actor_Transportation'].value_counts()
# 自動車       Automobile               3521
# 二輪車       Two wheeled vehicle      2804
# 歩行者       Pedestrian               564
# 不明・物件等  Unknown · Property etc.  56
cleanup_nums7_1 = {'自動車': 'Automobile',
                  '二輪車':'Two_wheeled_vehicle',
                  '歩行者':'pedestrain',
                  '不明・物件等':'Property_Damage'}
Acc_ID_Final['2nd_Actor_Transportation1']= Acc_ID_Final["2nd_Actor_Transportation"].replace(cleanup_nums7_1)
cleanup_nums7_2 = {'自動車': 1,
                  '二輪車':2,
                  '歩行者':3,
                  '不明・物件等':4}
Acc_ID_Final['2nd_Actor_Transportation2']= Acc_ID_Final["2nd_Actor_Transportation"].replace(cleanup_nums7_2)
Acc_ID_Final['2nd_Actor_Transportation'].value_counts()
Acc_ID_Final['2nd_Actor_Transportation1'].value_counts()
Acc_ID_Final['2nd_Actor_Transportation2'].value_counts()
# ---[variable No. (8)]-------------------"Vehicle_shape"-------------------------
Acc_ID_Final['Vehicle_shape'].value_counts()
# 乗用車      Passenger car    5978
# 貨物車      Cargo car        968
# 対象外当事者 Outside parties  1
cleanup_nums8_1 = {'乗用車': 'Pass_car',
                  '貨物車':'Cargo_car',
                  '対象外当事者':'Others'}
Acc_ID_Final['Vehicle_shape1']= Acc_ID_Final["Vehicle_shape"].replace(cleanup_nums8_1)
cleanup_nums8_2 = {'乗用車': 1,
                  '貨物車':2,
                  '対象外当事者':3}
Acc_ID_Final['Vehicle_shape2']= Acc_ID_Final["Vehicle_shape"].replace(cleanup_nums8_2)
Acc_ID_Final['Vehicle_shape'].value_counts()
Acc_ID_Final['Vehicle_shape1'].value_counts()
Acc_ID_Final['Vehicle_shape2'].value_counts()
# ---[variable No. (9)]-------------------"Use"-------------------------
Acc_ID_Final['Use'].value_counts()
# 自家用 Private use     6724
# 事業用 For business    219
# その他 Other           4
cleanup_nums9_1 = {'自家用': 'Private_use',
                  '事業用':'For_business',
                  'その他':'Other'}
Acc_ID_Final['Use1']= Acc_ID_Final["Use"].replace(cleanup_nums9_1)
cleanup_nums9_2 = {'自家用':1,
                  '事業用':2,
                  'その他':3}
Acc_ID_Final['Use2']= Acc_ID_Final["Use"].replace(cleanup_nums9_2)
Acc_ID_Final['Use'].value_counts()
Acc_ID_Final['Use1'].value_counts()
Acc_ID_Final['Use2'].value_counts()
# ---[variable No. (10)]-------------------"Road_form"-------------------------
Acc_ID_Final['Road_form'].value_counts()
cleanup_nums10 = {'交差点内':1}     # it means inside the intersection
Acc_ID_Final['Road_form1']= Acc_ID_Final["Road_form"].replace(cleanup_nums10)
Acc_ID_Final['Road_form1'].value_counts()
# ---[variable No. (11)]-------------------"Road_alignments"-------------------------
Acc_ID_Final['Road_alignments'].value_counts()
# 直線        Line                  6904
# カーブ・屈折 Curve · Refraction     43
cleanup_nums11_1 = {'直線':'Line','カーブ・屈折':'Curve'}
Acc_ID_Final['Road_alignments1']= Acc_ID_Final["Road_alignments"].replace(cleanup_nums11_1)
cleanup_nums11_2 = {'直線':1,'カーブ・屈折':0}
Acc_ID_Final['Road_alignments2']= Acc_ID_Final["Road_alignments"].replace(cleanup_nums11_2)
Acc_ID_Final['Road_alignments'].value_counts()
Acc_ID_Final['Road_alignments1'].value_counts()
Acc_ID_Final['Road_alignments2'].value_counts()
# ---[variable No. (12)]-------------------"Road_width"-------------------------
Acc_ID_Final['Road_alignments'].value_counts()
#  5.5ｍ以上     5.5 m or more 3700
#  3.5ｍ以上     3.5 m or more 1923
#  9.0ｍ以上     9.0 m or more 680
#  13.0ｍ以上    13.0 m or more 495
#  3.5ｍ未満     Less than 3.5 m 85
#  19.5ｍ以上    19.5 m or more 64
cleanup_nums12_1 = {'5.5ｍ以上':'5.5_m_or_more',
                    '3.5ｍ以上':'3.5_m_or_more',
                    '9.0ｍ以上':'9.0_m_or_more',
                    '13.0ｍ以上':'13.0_or_more',
                    '3.5ｍ未満':'Less_than_3.5_m',
                    '19.5ｍ以上':'19.5_m_or_more'}
Acc_ID_Final['Road_width1']= Acc_ID_Final["Road_width"].replace(cleanup_nums12_1)
cleanup_nums12_2 = {'5.5ｍ以上': 1,
                    '3.5ｍ以上': 2,
                    '9.0ｍ以上': 3,
                    '13.0ｍ以上':4,
                    '3.5ｍ未満': 5,
                    '19.5ｍ以上':6}
Acc_ID_Final['Road_width2']= Acc_ID_Final["Road_width"].replace(cleanup_nums12_2)
Acc_ID_Final['Road_width'].value_counts()
Acc_ID_Final['Road_width1'].value_counts()
Acc_ID_Final['Road_width2'].value_counts()
# New calss used here to referct:
# [1]#  3.5ｍ以上     3.5 m or more 1923 and #  3.5ｍ未満     Less than 3.5 m 85
# [2]#  5.5ｍ以上     5.5 m or more 3700
# [3]#  9.0ｍ以上     9.0 m or more 680
# [4]#  13.0ｍ以上    13.0 m or more 495
# [4]#  19.5ｍ以上    19.5 m or more 64
cleanup_nums12_3 = {'5.5ｍ以上': '5.5_m_or_more',
                    '3.5ｍ以上': 'Between_Less3.5_and_5.5m',
                    '9.0ｍ以上': '9.0_m_or_more',
                    '13.0ｍ以上':'13.0_or_more',
                    '3.5ｍ未満': 'Between_Less3.5_and_5.5m',
                    '19.5ｍ以上':'13.0_or_more'}
Acc_ID_Final['Road_width3']= Acc_ID_Final["Road_width"].replace(cleanup_nums12_3)
Acc_ID_Final['Road_width3'].value_counts(normalize=True)
"""
   One possible configuration as follow:
      - Narrow_road           road width 3.5 m or less
      - One_lane              road width larger than 3.5 m
      - Two_to_Three_lanes    road width 5.5m to less than 13.0 m
      - Four_to_Five_lanes    road width 13.m and less than 19.m
"""
cleanup_nums12_4 = {'5.5ｍ以上': 'Two_to_Three_lanes',
                    '3.5ｍ以上': 'One_lane',
                    '9.0ｍ以上': 'Two_to_Three_lanes',
                    '13.0ｍ以上':'larger_than_Four_lanes',
                    '3.5ｍ未満': 'Narrow_road',
                    '19.5ｍ以上':'larger_than_Four_lanes'}
Acc_ID_Final['Road_width4']= Acc_ID_Final["Road_width"].replace(cleanup_nums12_4)
Acc_ID_Final['Road_width4'].value_counts(normalize=True)


# ---[variable No. (13)]-------------------"Condition"-------------------------
Acc_ID_Final['Condition'].value_counts()
# 乾燥    Drying      6075
# 湿潤    Wet         859
# 凍結    Frozen      7
# 積雪    Snow cover  6
cleanup_nums13_1 = {'乾燥':'Drying',
                    '湿潤':'Wet',
                    '凍結':'Frozen',
                    '積雪':'Snow cover'
                    }
Acc_ID_Final['Condition1']= Acc_ID_Final["Condition"].replace(cleanup_nums13_1)
cleanup_nums13_2 = {'乾燥':1,
                    '湿潤':2,
                    '凍結':3,
                    '積雪':4
                    }
Acc_ID_Final['Condition2']= Acc_ID_Final["Condition"].replace(cleanup_nums13_2)

# ---[variable No. (14)]-------------------"Speed_limit"-------------------------
Acc_ID_Final['Speed_limit'].value_counts()
#  40km/h以下    40 km / h or less       2501
#  50km/h以下    50 km / h or less 1800  1800
#  規制なし等     No regulation etc.      1734
#  60km/h以下    60 km / h or less       651
#  30km/h以下    30 km / h or less       261
cleanup_nums14_1 = {'40km/h以下':'40kmh_orless',
                    '50km/h以下':'50kmh_orless',
                    '規制なし等' :'No_regulation',
                    '60km/h以下':'60kmh_orless',
                    '30km/h以下':'30kmh_orless',
                    }
Acc_ID_Final['Speed_limit1']= Acc_ID_Final["Speed_limit"].replace(cleanup_nums14_1)
cleanup_nums14_2 = {'40km/h以下':1,
                    '50km/h以下':2,
                    '規制なし等' :3,
                    '60km/h以下':4,
                    '30km/h以下':5,
                    }
# New scale to match my dataset in TRB
# [1]#  30km/h以下    30 km / h or less       261
# [2]#  40km/h以下    40 km / h or less       2501
# [3]#  50km/h以下    50 km / h or less 1800  1800 and #  60km/h以下    60 km / h or less       651#
# [4]#  規制なし等     No regulation etc.      1734

Acc_ID_Final['Speed_limit2']= Acc_ID_Final["Speed_limit"].replace(cleanup_nums14_2)
cleanup_nums14_3 = {'40km/h以下':'Medium_speed_limit',
                    '50km/h以下':'High_speed_limit',
                    '規制なし等' :'No_regulation',
                    '60km/h以下':'High_speed_limit',
                    '30km/h以下':'Low_speed_limit',
                    }
Acc_ID_Final['Speed_limit3']= Acc_ID_Final["Speed_limit"].replace(cleanup_nums14_3)
Acc_ID_Final['Speed_limit'].value_counts(normalize = True)
Acc_ID_Final['Speed_limit1'].value_counts(normalize = True)
Acc_ID_Final['Speed_limit2'].value_counts(normalize = True)
Acc_ID_Final['Speed_limit3'].value_counts(normalize = True)
# ---[variable No. (15)]-------------------"Age_Group"-------------------------
Acc_ID_Final['Age_Group'].value_counts(normalize = False)
# 一般     General         0.671945           4668
# 若者     Youth           0.166403           1156
# 高齢者   Elderly people  0.161653            1123

cleanup_nums15_1 = {'一般'   :'Middle_age',
                    '若者'   :'Young',
                    '高齢者' :'Senior'}
Acc_ID_Final['Age_Group1']= Acc_ID_Final["Age_Group"].replace(cleanup_nums15_1)
cleanup_nums15_2 = {'一般'   :1,
                    '若者'   :2,
                    '高齢者' :3}
Acc_ID_Final['Age_Group2']= Acc_ID_Final["Age_Group"].replace(cleanup_nums15_2)
Acc_ID_Final['Age_Group'].value_counts(normalize = True)
Acc_ID_Final['Age_Group1'].value_counts(normalize = True)
Acc_ID_Final['Age_Group2'].value_counts(normalize = True)
# ---[variable No. (16)]-------------------"Sex"-------------------------
Acc_ID_Final['Sex'].value_counts(normalize = False)
# 男   male   4421
# 女   female 2526
cleanup_nums16_1 = {'男'   :'male',
                    '女'   :'female'}
Acc_ID_Final['Sex1']= Acc_ID_Final["Sex"].replace(cleanup_nums16_1)
cleanup_nums16_2 = {'男'   :0,
                    '女'   :1}
Acc_ID_Final['Sex2']= Acc_ID_Final["Sex"].replace(cleanup_nums16_2)
Acc_ID_Final['Sex'].value_counts(normalize = True)
Acc_ID_Final['Sex1'].value_counts(normalize = True)
Acc_ID_Final['Sex2'].value_counts(normalize = True)
# ---[variable No. (17)]-------------------"Road_type_code"-------------------------
# The origional variable here is a categorical numerical variable.
Acc_ID_Final['Road_type_code'].value_counts(normalize = False)
# [1]# 高速自動車国道                         High-speed car national road
# [3]# 一般国道                              General national road
# [4]# 主要地方道(都道府県道)                  Major regional road (prefectural road)
# [6]# 一般都道府県道                         Minor prefectural road
# [9]# その他の道路                           Other roads
# Before their names were:
# [1]# Default case (4 cases only)
# [3]# General National Road National road (managed by the government)
# [4]# Major regional roads (prefectural roads) managed by local government
# [6]# General prefectural road minor road managed by the local government
# [9]# Other roads others

cleanup_nums17_1 = {1 : '高速自動車国道',
                    3 : '一般国道',
                    4 : '主要地方道(都道府県道)',
                    6 : '一般都道府県道',
                    9 : 'その他の道路',
                    }
Acc_ID_Final['Road_type_code1']= Acc_ID_Final["Road_type_code"].replace(cleanup_nums17_1)

"""
The configureation that we would like to obtain are:
<Configuration [1]> [Base Case 高速自動車国道 (High-speed car national road)]
      - Prefectural road dummy（県道ダミー）】→主要地方道（都道府県）＋一般都道府県  : which means [3]+[4]
      - Minor prefectural road                                              : which means [6]# 一般都道府県道
      - 【Narrow street dummy（細街路ダミー）】→その他道路                       : which means [9]
"""
cleanup_nums17_3 = {1 : 'High-speed',
                    3 : 'Prefectural_road',
                    4 : 'Prefectural_road',
                    6 : 'Minor_prefectural_road',
                    9 : 'Narrow_road',
                    }
Acc_ID_Final['Road_type_code3']= Acc_ID_Final["Road_type_code"].replace(cleanup_nums17_3)
Acc_ID_Final['Road_type_code3'].value_counts()
"""
<Configuration [2]> [Base Case 高速自動車国道 (High-speed car national road)]
      - [3]# 一般国道                    General national road
      - [4]# 主要地方道(都道府県道)        Major regional road (prefectural road)
      - [6]# 一般都道府県道               Minor prefectural road
      - [9]# その他の道路                 Other roads
                          [9]    3925
                          [3]    1325
                          [6]    1031
                          [4]     661
                          [1]       5
"""
cleanup_nums17_2 = {1 : 'High-speed',
                    3 : 'General_national_road',
                    4 : 'Major_prefectural_road',
                    6 : 'Minor_prefectural_road',
                    9 : 'Narrow_road',
                    }
Acc_ID_Final['Road_type_code2']= Acc_ID_Final["Road_type_code"].replace(cleanup_nums17_2)
Acc_ID_Final['Road_type_code2'].value_counts()
# Or the default one:
Acc_ID_Final['Road_type_code'].value_counts()
# ---[variable No. (18)]-------------------"Road_width_code"-------------------------
# [Road_width_code] This variable is obtained from matching the ITARDA Road Digital Map (RDM)
# The default variable is categorical numerical variable.
Acc_ID_Final['Road_width_code'].value_counts(normalize = False)
# [1]# 幅員13.0m以上            Width 13.0 m or more                    Sample Size =  [642]
# [2]# 幅員 5.5m以上~13.0m未満   Width 5.5 m or more to less than 13.0 m Sample Size =  [5852]
# [3]# 幅員 3.0m以上~ 5.5m未満   Width 3.0 m or more to less than 5.5 m  Sample Size =  [441]
# [4]# 幅員 3.0m未満            Width 3.0 m or less                     Sample Size =  [12]

cleanup_nums18_1 = {1 : '幅員13.0m以上',
                    2 : '幅員5.5m以上_13.0m未満',
                    3 : '幅員3.0m以上_5.5m未満',
                    4 : '幅員3.0m未満'
                    }
Acc_ID_Final['Road_width_code1']= Acc_ID_Final["Road_width_code"].replace(cleanup_nums18_1)
Acc_ID_Final['Road_width_code1'].value_counts(normalize = False)

cleanup_nums18_2 = {1 : 'Width_13.0m_or_more',
                    2 : 'Width_5.5m_and_less_13.0m',
                    3 : 'Width3.0m_and_less_5.5m',
                    4 : 'Width3.0m_or_less'
                    }
Acc_ID_Final['Road_width_code2']= Acc_ID_Final["Road_width_code"].replace(cleanup_nums18_2)
Acc_ID_Final['Road_width_code2'].value_counts(normalize = False)
# ---[variable No. (19)]-------------------"12h_traffic_volume（100台）"-------------------------
Acc_ID_Final['12h_traffic_volume（100台）'].value_counts(normalize = False)
# Setting the Log of traffic volume
Acc_ID_Final['log_12h_traffic_volume（100台）'] = np.where(Acc_ID_Final['12h_traffic_volume（100台）']>0,
                                                 np.log(Acc_ID_Final['12h_traffic_volume（100台）']), 0)
# Setting the Dummy of intersections with unobserved traffic volume
Acc_ID_Final['Unobserved_traffic_volume'] = np.where(Acc_ID_Final['12h_traffic_volume（100台）']>0 ,1, 0)
# ---[Using Map]-------------------"Test"-------------------------
# Notice everything above except setting the dummy for the traffic can be achieved using map as
# From above we get
Acc_ID_Final['Weather'].value_counts()
Acc_ID_Final['Weather1'].value_counts()
test = {'晴':'Sunny','曇':'Cloud','雨':'Rain', '雪':'Snow', '霧': 'Fog'}
Acc_ID_Final['Weatherx'] = Acc_ID_Final['Weather'].map(test)
Acc_ID_Final['Weatherx'].value_counts()
# ==================================================#
#     Rearrange the columns for better tracing
# ==================================================#
# Here I will chagne the order of my Dataset to make it more clear where is the new variables are inserted
# Using <Acc_ID_Final.columns.values> to get them as a list.
Acc_ID_Final= Acc_ID_Final[['Actor Number',
                            'Hour',
                            'Weather',
                            'Weather1',
                            'Weather2',
                            'Accident Information内容',
                            'Severity_level1',
                            'Severity_level2',
                            'Accident type',
                            'Accident type1',
                            'Accident type2',
                            'Actor type',
                            'Actor type1',
                            'Actor type2',
                            'Transportation',
                            'Transportation1',
                            '1st_Actor_Transportation',
                            '1st_Actor_Transportation1',
                            '2nd_Actor_Transportation',
                            '2nd_Actor_Transportation1',
                            '2nd_Actor_Transportation2',
                            'Vehicle_shape',
                            'Vehicle_shape1',
                            'Vehicle_shape2',
                            'Use',
                            'Use1',
                            'Use2',
                            'Road_form',
                            'Road_form1',
                            'Road_alignments',
                            'Road_alignments1',
                            'Road_alignments2',
                            'Road_width',
                            'Road_width1',
                            'Road_width2',
                            'Road_width3',
                            'Road_width4',
                            'Condition',
                            'Condition1',
                            'Condition2',
                            'Speed_limit',
                            'Speed_limit1',
                            'Speed_limit2',
                            'Speed_limit3',
                            'Age_Group',
                            'Age_Group1',
                            'Age_Group2',
                            'Sex',
                            'Sex1',
                            'Sex2', 'Latitude（base-60）',
                            'Longitude（base-60）', 'Latitudex', 'Longitudex', '2nd_Mesh', '全道路Node1',
                            '全道路Node2', 'LinkLength(m)', 'Traffic_regulation_code',
                            'Road_type_code1',
                            'Road_type_code3',
                            'Road_type_code2',
                            'Road_type_code',
                            'Road_width_code',
                            'Road_width_code1',
                            'Road_width_code2',
                            'Administration_code',
                            'RoadLine_code', '対応基本道路Node1', '対応基本道路Node2', 'NearestLinkDistance(m)',
                            'DRM_Node1_Lat', 'DRM_Node1_Lon', 'DRM_Node2_Lat', 'DRM_Node2_Lon',
                            '12h_traffic_volume（100台）',
                            'log_12h_traffic_volume（100台）',
                            'Unobserved_traffic_volume',
                            'ITARDA_crossing_ID', 'Filter10',
                            'Filter20', 'Filter30', 'Filter50', 'Filter75', 'Filter100',
                            'Intersection1', 'Intersection2', 'Intersection3', 'Intersection4',
                            'Intersection5', 'Distance1', 'Distance2', 'Distance3', 'Distance4',
                            'Distance5', 'FilterLess35', 'FilterLess50']]

# ==================================================#
#          Qureies and Digging in our Data
# ==================================================#
# Crashes happened per each age group
Acc_ID_Final['Age_Group1'].value_counts() # Age_Group1 is a column created above
# How many Accidents caused by the Senior drivers
Acc_ID_Final.query("Age_Group1== 'Senior'").count()['Age_Group1']
# How many accidents caused by male in our dataset
Acc_ID_Final.query("Sex1== 'male'").count()['Sex1']

# ==================================================#
#        Select only the variables of interest
# ==================================================#
"""
  You have to do the folloiwng:
    - All variables should be coded and no Japanese, or English
    - Selection based on the Maximum Likelihood host function later.
"""
Acc_ID_Final_2= Acc_ID_Final[['Actor Number',
                            'Severity_level1',
                            'Accident type2',
                            'Actor type2',
                            'Vehicle_shape2',
                            'Use2',
                            'Road_form1',
                            'Road_alignments2',
                            'Road_width',
                            'Road_width1',
                            'Road_width2',
                            'Road_width3',
                            'Road_width4',
                            'Speed_limit',
                            'Speed_limit1',
                            'Speed_limit2',
                            'Speed_limit3',
                            'Age_Group1',
                            'Sex2',
                            'Road_type_code',
                            'Road_type_code2',
                            'Road_type_code3',
                            'Road_width_code',
                            'Road_width_code1',
                            'Road_width_code2',
                            '12h_traffic_volume（100台）',
                            'log_12h_traffic_volume（100台）',
                            'Unobserved_traffic_volume',
                            'FilterLess35']]

# ==================================================#
#  Checking for Missing values and Getting Dummies
# ==================================================#
"""
  You have to do the folloiwng:
    - Check every row if there is a Nan
    - Drop any row with Nan values
    - Create a dummy variables form the Group above (converate categorical variable to a set of dummy variables)
"""
# getting an overview of our data
print("Our data has {0} rows and {1} columns".format(Acc_ID_Final.shape[0], Acc_ID_Final.shape[1]))
# checking for missing values
print("Are there missing values? {}".format(Acc_ID_Final.isnull().any().any()))
Acc_ID_Final.describe()

# Now we will get the Dummies out of the categorical variables.
Acc_ID_Final['Age_Group2']
test = pd.get_dummies(Acc_ID_Final['Age_Group2']).rename(columns = {1:'Middle_age',2:'Young',3:'Senior'})
print(f"The value calculated by Normalize the categorical variable is = \n{Acc_ID_Final['Age_Group2'].value_counts(normalize=True)}")
print("------------------------------------------")
print(f"While the value caculated from the dummy variable is = \n{test.sum()/len(test)}")

#test = pd.get_dummies(Acc_ID_Final_2['Severity_level1'])
# if you already defined your categorical variable then columns will be automatic
# Since the dummies is another table (pandas object) then you can append it to your original table (indecies will be automatic if they are same)
#Acc_ID_Final_2.join(test)

# If you want to change a dummies to categorical variable then simply sue
# https://stackoverflow.com/questions/26762100/reconstruct-a-categorical-variable-from-dummies-in-pandas
# Road_Type1.idxmax(axis=1)  < you need a pandas dataframe of all dummies> then you use idxmax

# =============================================================#
#     Variables of Interests and coverate them to dummies
# =============================================================#
"""
        We will converate some variables to a dummies here prior to the pivot table:
            - As we will aggreate later each dummy then we create another dummy to our dataset.
            - The values will refect if the variable of interest existed or not.
"""
# -----Exoginous Variables-----------------------
# [Variable <1>] RoadType
# -----------------------------------------------
Road_Type1_dummies = pd.get_dummies(Acc_ID_Final_2['Road_type_code2']) # Configuration <1>
Road_Type1_dummies['Prefectural_Dummy_new'] = Road_Type1_dummies['General_national_road']+Road_Type1_dummies['Major_prefectural_road']#Configuration <2>
# Road types are four classes [ ]
# To check the combination we get
(Road_Type1_dummies[['Major_prefectural_road','General_national_road']].sum()/len(Road_Type1_dummies)).sum()
Road_Type1_dummies[['Prefectural_Dummy_new']].sum()/len(Road_Type1_dummies)
# -----------------------------------------------
# [Variable <2>] RoadWidth
# RoadWidth [1] # From Police Report
Acc_ID_Final_2[['Road_width','Road_width1','Road_width2', 'Road_width3', 'Road_width4']]  # All Road width variables from Police
Road_width_dummies_1 = pd.get_dummies(Acc_ID_Final_2['Road_width1'],prefix='conf1') # <Configuration [1]>
Road_width_dummies_2 = pd.get_dummies(Acc_ID_Final_2['Road_width3'],prefix='conf2') # <Configuration [2]>
Road_width_dummies_3 = pd.get_dummies(Acc_ID_Final_2['Road_width4'],prefix='conf3') # <Configuration [3]>
# Check these configuration
print((Road_width_dummies_1.sum()/len(Road_width_dummies_1)),'\n',
      (Road_width_dummies_2.sum()/len(Road_width_dummies_2)),'\n',
      (Road_width_dummies_3.sum()/len(Road_width_dummies_3)))
# RoadWidth [2] # From ITARDA Map Matching (DRM) Digital-Road-Mapping.
Acc_ID_Final_2[['Road_width_code','Road_width_code1','Road_width_code2']]
# We will use only the Road_width_code2
Road_width_DRM_dummies_1 = pd.get_dummies(Acc_ID_Final_2['Road_width_code2']) # <Configuration [1]>
# Check between the catageorical and dummies configuration
a = (Road_width_DRM_dummies_1.sum()/len(Road_width_DRM_dummies_1)).sort_values(ascending =False)
b =  Acc_ID_Final_2['Road_width_code2'].value_counts(normalize =True)
print(f"The value of catageorical variable normalized are =\n{a}\n\nwhile for Dummies are =\n{b}")
# -----------------------------------------------
# [Variable <3>] Speed_Limit
Acc_ID_Final_2[['Speed_limit','Speed_limit1','Speed_limit2','Speed_limit3']]
# Speed limit configuration [1]
Speed_limit_dummies_1 = pd.get_dummies(Acc_ID_Final_2['Speed_limit1'], prefix = 'conf1')
# Check this configuration as:
a1 = (Speed_limit_dummies_1.sum()/len(Speed_limit_dummies_1)).sort_values(ascending =False)
b1 = Acc_ID_Final_2['Speed_limit1'].value_counts(normalize=True)
print(f"The value of catageorical variable normalized are =\n{a1}\n\nwhile for Dummies are =\n{b1}")
# Speed limit configuration [2]
Speed_limit_dummies_2 = pd.get_dummies(Acc_ID_Final_2['Speed_limit3'],prefix = 'conf2')
a2 = (Speed_limit_dummies_2.sum()/len(Speed_limit_dummies_2)).sort_values(ascending =False)
b2 = Acc_ID_Final_2['Speed_limit3'].value_counts(normalize=True)
print(f"The value of catageorical variable normalized are =\n{a2}\n\nwhile for Dummies are =\n{b2}")
# -----------------------------------------------
# [Variable <4>] Traffic Volume
Acc_ID_Final_2[['12h_traffic_volume（100台）','log_12h_traffic_volume（100台）','Unobserved_traffic_volume']]
# I will change the name since there is a space and Japanese letter in the above
Acc_ID_Final_2[['12h_traffic_volume（100台）','log_12h_traffic_volume（100台）','Unobserved_traffic_volume']].columns


Acc_ID_Final_2.rename(columns={'12h_traffic_volume（100台）':'traffic_volume',
                               'log_12h_traffic_volume（100台）':'log_traffic_volume',
                               'Unobserved_traffic_volume':'traffic_volume_dummy'},inplace=True)
Acc_ID_Final_2['log_traffic_volume_2'] =np.where(Acc_ID_Final_2['traffic_volume']>0,
                                        np.log(Acc_ID_Final_2['traffic_volume']*100), 0)
# -----Endeginous Variables-----------------------
Driver_Age = pd.get_dummies(Acc_ID_Final_2['Age_Group1'],prefix='Driver')
Severity   = pd.get_dummies(Acc_ID_Final_2['Severity_level1'],prefix='Level')

# ==================================================#
#   Join your dataset to complete all configuration
#                     [Printing]
# ==================================================#
# -----------------------------------------------
# Join the database that you created, as: # As you added a prefix (conf1,2,3) the column names become unique (join will work)
Acc_ID_Final_2 = Acc_ID_Final_2.join(Severity).join(Driver_Age).join(Road_Type1_dummies).join(Road_width_dummies_1).join(Road_width_dummies_2).join(Road_width_dummies_3).join(Road_width_DRM_dummies_1).join(Speed_limit_dummies_1).join(Speed_limit_dummies_2)

# Save this dataset to run in in Excel-sheet for cross-validation
Acc_ID_Final_2.to_excel(Current_Path + "/Results3/Acc_ID_Final_2.xlsx", sheet_name="Acc_ID_Final_2")

# ==================================================#
#       Prepareing for Piovt table aggregation
# ==================================================#
"""
  It seems we only need some variables to aggregate them based on the filter we created before
  then we apply the pivot for these ID, (ITARDA) intersection id, (namely: FilterLess35)
      The variables we will need are:
Intersection Index
 Count of FilterLess35
 Sum of Driver_Young
 Sum of Driver_Middle_age
 Sum of Driver_Senior
 Sum of High-speed
 Sum of General_national_road
 Sum of Major_prefectural_road
 Sum of Minor_prefectural_road
 Sum of Narrow_road
 Sum of Prefectural_Dummy_new
 Sum of conf1_13.0_or_more
 Sum of conf1_19.5_m_or_more
 Sum of conf1_3.5_m_or_more
 Sum of conf1_5.5_m_or_more
 Sum of conf1_9.0_m_or_more
 Sum of conf1_Less_than_3.5_m
 Sum of conf2_13.0_or_more
 Sum of conf2_5.5_m_or_more
 Sum of conf2_9.0_m_or_more
 Sum of conf2_Between_Less3.5_and_5.5m
 Sum of conf3_Narrow_road
 Sum of conf3_One_lane
 Sum of conf3_Two_to_Three_lanes
 Sum of conf3_larger_than_Four_lanes
 Sum of Width3.0m_and_less_5.5m
 Sum of Width3.0m_or_less
 Sum of Width_13.0m_or_more
 Sum of Width_5.5m_and_less_13.0m
 Sum of conf1_30kmh_orless
 Sum of conf1_40kmh_orless
 Sum of conf1_50kmh_orless
 Sum of conf1_60kmh_orless
 Sum of conf1_No_regulation
 Sum of conf2_High_speed_limit
 Sum of conf2_Low_speed_limit
 Sum of conf2_Medium_speed_limit
 Sum of conf2_No_regulation
 Max of traffic_volume
 Max of log_traffic_volume
 Sum of traffic_volume_dummy
"""

# --------------------------------------------------
"""
        As we proced with the data analysis we will conduct an anaylsis using Pandas Pivot_table:
            - Construct here the Cross-sectional Dataset with considering the indexing
"""
print("Our data has {0} rows and {1} columns".format(Acc_ID_Final_2.shape[0], Acc_ID_Final_2.shape[1]))
# checking for missing values
print("Are there missing values? {}".format(Acc_ID_Final_2.isnull().any().any()))
Acc_ID_Final_2.describe().T

# -------------Cross Sectional Analysis------------------
# <1> Using Pivot_table
pd.pivot_table(Acc_ID_Final_2, index=["FilterLess35"])

# How to apply columns to your data

"""
    Notes on Pivot table with better control
      - If you want to pass aggfunc over all values use list as :aggfunc = [function1, function2,..etc]
      - If you want to pass only one function for each values then pass dict. : aggfunc = {'values1':'function1', ..etc}
      - As you piovting the table if you assign an index you cant use it again as a values, instead creat a new column
          that is similar to the pivoting index and then apply the (len) as count variable (namely: Crash_count).
      - If you want to keep the order of your Pivot_table columns then you need the follwoing suggestion:
          https://stackoverflow.com/questions/36346071/pandas-pivot-table-changing-order-of-non-index-columns
          we have created a column_order for this purpose

"""
Acc_ID_Final_2["Crash_count"] = Acc_ID_Final_2["FilterLess35"]
column_order = ['Crash_count',
                'Driver_Young',
                'Driver_Middle_age',
                'Driver_Senior',
                'High-speed',
                'General_national_road',
                'Major_prefectural_road',
                'Minor_prefectural_road',
                'Narrow_road',
                'Prefectural_Dummy_new',
                'conf1_13.0_or_more',
                'conf1_19.5_m_or_more',
                'conf1_3.5_m_or_more',
                'conf1_5.5_m_or_more',
                'conf1_9.0_m_or_more',
                'conf1_Less_than_3.5_m',
                'conf2_13.0_or_more',
                'conf2_5.5_m_or_more',
                'conf2_9.0_m_or_more',
                'conf2_Between_Less3.5_and_5.5m',
                'conf3_Narrow_road',
                'conf3_One_lane',
                'conf3_Two_to_Three_lanes',
                'conf3_larger_than_Four_lanes',
                'Width3.0m_and_less_5.5m',
                'Width3.0m_or_less',
                'Width_13.0m_or_more',
                'Width_5.5m_and_less_13.0m',
                'conf1_30kmh_orless',
                'conf1_40kmh_orless',
                'conf1_50kmh_orless',
                'conf1_60kmh_orless',
                'conf1_No_regulation',
                'conf2_High_speed_limit',
                'conf2_Low_speed_limit',
                'conf2_Medium_speed_limit',
                'conf2_No_regulation',
                'traffic_volume',
                'log_traffic_volume',
                'traffic_volume_dummy',
                'log_traffic_volume_2']
Pivot_table1 = pd.pivot_table(Acc_ID_Final_2, index=["FilterLess35"], #columns=["Age_Group1"],
                           values=['Crash_count',
                                   'Driver_Young',
                                   'Driver_Middle_age',
                                   'Driver_Senior',
                                   'High-speed',
                                   'General_national_road',
                                   'Major_prefectural_road',
                                   'Minor_prefectural_road',
                                   'Narrow_road',
                                   'Prefectural_Dummy_new',
                                   'conf1_13.0_or_more',
                                   'conf1_19.5_m_or_more',
                                   'conf1_3.5_m_or_more',
                                   'conf1_5.5_m_or_more',
                                   'conf1_9.0_m_or_more',
                                   'conf1_Less_than_3.5_m',
                                   'conf2_13.0_or_more',
                                   'conf2_5.5_m_or_more',
                                   'conf2_9.0_m_or_more',
                                   'conf2_Between_Less3.5_and_5.5m',
                                   'conf3_Narrow_road',
                                   'conf3_One_lane',
                                   'conf3_Two_to_Three_lanes',
                                   'conf3_larger_than_Four_lanes',
                                   'Width3.0m_and_less_5.5m',
                                   'Width3.0m_or_less',
                                   'Width_13.0m_or_more',
                                   'Width_5.5m_and_less_13.0m',
                                   'conf1_30kmh_orless',
                                   'conf1_40kmh_orless',
                                   'conf1_50kmh_orless',
                                   'conf1_60kmh_orless',
                                   'conf1_No_regulation',
                                   'conf2_High_speed_limit',
                                   'conf2_Low_speed_limit',
                                   'conf2_Medium_speed_limit',
                                   'conf2_No_regulation',
                                   'traffic_volume',
                                   'log_traffic_volume',
                                   'traffic_volume_dummy',
                                   'log_traffic_volume_2'
                                   ],
                           aggfunc={'Crash_count':len,
                                    'Driver_Young':np.sum,
                                    'Driver_Middle_age':np.sum,
                                    'Driver_Senior':np.sum,
                                    'High-speed': np.sum,
                                    'General_national_road': np.sum,
                                    'Major_prefectural_road': np.sum,
                                    'Minor_prefectural_road': np.sum,
                                    'Narrow_road': np.sum,
                                    'Prefectural_Dummy_new':np.sum,
                                    'conf1_13.0_or_more': np.sum,
                                    'conf1_19.5_m_or_more': np.sum,
                                    'conf1_3.5_m_or_more': np.sum,
                                    'conf1_5.5_m_or_more': np.sum,
                                    'conf1_9.0_m_or_more': np.sum,
                                    'conf1_Less_than_3.5_m': np.sum,
                                    'conf2_13.0_or_more': np.sum,
                                    'conf2_5.5_m_or_more': np.sum,
                                    'conf2_9.0_m_or_more': np.sum,
                                    'conf2_Between_Less3.5_and_5.5m': np.sum,
                                    'conf3_Narrow_road': np.sum,
                                    'conf3_One_lane': np.sum,
                                    'conf3_Two_to_Three_lanes': np.sum,
                                    'conf3_larger_than_Four_lanes': np.sum,
                                    'Width3.0m_and_less_5.5m': np.sum,
                                    'Width3.0m_or_less': np.sum,
                                    'Width_13.0m_or_more': np.sum,
                                    'Width_5.5m_and_less_13.0m': np.sum,
                                    'conf1_30kmh_orless': np.sum,
                                    'conf1_40kmh_orless': np.sum,
                                    'conf1_50kmh_orless': np.sum,
                                    'conf1_60kmh_orless': np.sum,
                                    'conf1_No_regulation': np.sum,
                                    'conf2_High_speed_limit': np.sum,
                                    'conf2_Low_speed_limit': np.sum,
                                    'conf2_Medium_speed_limit': np.sum,
                                    'conf2_No_regulation': np.sum,
                                    'traffic_volume':np.mean,
                                    'log_traffic_volume':np.mean,
                                    'traffic_volume_dummy':np.sum,
                                    'log_traffic_volume_2':np.mean},
                                     fill_value=0)
Pivot_table1 = Pivot_table1.reindex_axis(column_order, axis=1)
# Check usign: Pivot_table1.iloc[0:5,4:10]
# You can perform any calcuation now
Pivot_table1.describe()
# Lets drop the first value of several crashes didnt find nearest intersection, they are labeled as = 0 in the index
Pivot_table1.drop(Pivot_table1.index[0],inplace = True)   # Crash unidentified = 4599 crash # [This should be applied once]
# ==================================================#
#      Distribution Layout of each Driver age
# ==================================================#
plt.figure(figsize = (12,10))
font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 10}  # normal bold
plt.rc('font', **font)
bins =[0,1,2,3,4,5,6,7,8,9,10,11]
#plt.subplot(2,2,1)
plt.subplot(221,xlabel='x \n[a]', ylabel='y', title='title')
plt.title('Crash_count')
plt.ylim(0,300,10)
P1 = Pivot_table1['Crash_count'].hist(alpha=0.5,bins=bins,align='left',color='#607c8e', edgecolor='black', linewidth=1.2) #,fc="None"
#removing top and right borders
plt.rcParams['patch.force_edgecolor'] = True
#plt.rcParams['patch.facecolor'] = 'b'
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['axes.labelweight'] = 'normal'
# begone the right, left, top and bottom spines
#P1.spines['bottom'].set_color('red')
# P1.spines['right'].set_visible(True)
# P1.spines['top'].set_visible(True)
# P1.spines['bottom'].set_visible(True)
# P1.spines['left'].set_visible(True)
P1.spines['top'].set_color('black')
P1.spines['bottom'].set_color('black')
P1.spines['right'].set_color('black')
P1.spines['left'].set_color('black')
P1.text(10, 10, r'$\mu=15, b=3$')
P1.set_xticks(bins[:-1])


plt.subplot(2,2,2)
plt.title('Driver_Young')
plt.ylim(0,300,50)
P2 = Pivot_table1['Driver_Young'].hist(alpha=0.5, bins=bins,align='left',color='#607c8e', edgecolor='black', linewidth=1.2)
P2.text(10, 40, r'$\mu=15, b=3$')
P2.set_xticks(bins[:-1])
plt.subplot(2,2,3)
plt.title('Driver_Middle_age')
plt.ylim(0,300,50)
P3 = Pivot_table1['Driver_Middle_age'].hist(alpha=0.5, bins=bins,align='left',color='#607c8e', edgecolor='black', linewidth=1.2)
P3.text(5, 45, r'$\mu=15, b=3$')
P3.set_xticks(bins[:-1])
plt.subplot(2,2,4)
plt.title('Driver_Senior')
plt.ylim(0,300,50)
#plt.gca().set_aspect('equal', adjustable='box')
P4 = Pivot_table1['Driver_Senior'].hist(alpha=0.5, bins=bins,align='left',color='#607c8e', edgecolor='black', linewidth=1.2)
P4.text(25, 50, r'$\mu=3, b=3$')
P4.set_xticks(bins[:-1])
# plt.rc('xtick', labelsize=20)
# plt.rc('ytick', labelsize=20)
plt.show()
# Pivot_table1['bins'] = pd.cut(Pivot_table1['Crash_count'], [0,5,10,15,20,25,30,35,40,45,50,55])
Pivot_table1['Driver_Young'].hist(alpha=0.4,bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Pivot_table1['Driver_Middle_age'].hist(alpha=0.4,bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Pivot_table1['Driver_Senior'].hist(alpha=0.4,bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
plt.show()
# <2> Using groupby function
# Acc_ID_Final_2.groupby('FilterLess35').aggregate({'traffic_volume':np.max, 'log_traffic_volume':np.max})
# ========= How to see what is have been grouped =======
# # Method[1]
# Acc_ID_Final_2.groupby('FilterLess35').describe()
# # Method[2]
# for key, item in Acc_ID_Final_2.groupby('FilterLess35'):
#     print(key,item)


# # How to apply a filter to your Data
# pd.pivot_table(Acc_ID_Final[Acc_ID_Final['Age_Group'] == '一般'], index=["FilterLess35"],  # columns =["Age_Group"],
#                values=['Traffic'],
#                aggfunc=[len, np.max], fill_value=0)

# ==================================================#
#     Dummies for the Pivot table aggreate data
# ==================================================#
"""
    We will perform a discrete choice set to obtain the following idea:
      - We will use the replace again to obtain the dummies out of the variables of itnersets

"""
# Lets see how many variables in the Pivot_table {Cross-sectional Setting}
Pivot_table1.columns

experment = pd.get_dummies(Acc_ID_Final_2['Age_Group1'],prefix='Driver')
# Roadtype set {test here to see the best way}
# Pivot_table1['High-speed'] = np.where(Pivot_table1['High-speed']>0 ,1, 0)


"""
   Since we want only binary dummies for the existance variable on the intersection we will perform a quick
    indexing over all the colums in our dataset and converate them to a binary:
      - We will use the replace again to obtain the dummies out of the variables of itnersets

"""
# Check the index length and what columns we are expecting.
print(f"We are expecting {len(Pivot_table1.columns)} columns")
print(f"We will except the following columns: \n{Pivot_table1.columns[0:4]}")
print(f"The affected columns are:  \n{Pivot_table1.iloc[:,4:37].columns}")
# Here is the full list of all columns in our table.
Pivot_table1.columns
for i in range (4,37):  # from 4 to 9
  # For every column, 1: means existed, 0: otherwise
  Pivot_table1[Pivot_table1.columns[i]] = np.where(Pivot_table1[Pivot_table1.columns[i]]>0 ,1, 0)
  #---------------------------------------
# We will perform an exception to the traffic volume dummy
Pivot_table1['traffic_volume_dummy'] = np.where(Pivot_table1['traffic_volume_dummy']>0 ,0, 1)
# Instead aggregate teh log_traffic I use the value from the pivot table and scale it out of 100 units.
# this variable already defined above but the pivot takes the mean so I dont use it. I use the one below instead
Pivot_table1['log_traffic_volume_2'] = np.where(Pivot_table1['traffic_volume']>0,
                                       np.log(Pivot_table1['traffic_volume']*100),0)


# 1 means missing traffic volume at that intersection, 0:otherwise

# Lets check the percentage of these variables
Pivot_table1['conf2_No_regulation'].value_counts()

# for i in range(39):
#   print(Pivot_table1[Pivot_table1.columns[i]].value_counts())

# The best way to show all the variables statistics simply by adding the following
Descreptive_Statstic_Table = Pivot_table1.describe().T
# To access each element in this table you can use (iloc, iat,..etc e.g., Pivot_table1.describe().T.iloc[0:3,0:])
# Remember that (iat and at) cant accept slicing like iloc and loc, but they are both faster than the latter.
writer = pd.ExcelWriter(Current_Path + "/Results3/Pivot_table1.xlsx", engine = 'xlsxwriter')
Pivot_table1.to_excel(writer, sheet_name="Pivot_table1")
Descreptive_Statstic_Table.to_excel(writer, sheet_name="Descreptive_Statstic_Table")
writer.save()
# # -------------Panel Sectional Analysis------------------
# # I cant make the years show repreatly the same length, in Excel there is functiont to do so,
# pd.pivot_table(Acc_ID_Final, index=["FilterLess35", "Year"])

# pd.pivot_table(Acc_ID_Final[Acc_ID_Final['Age_Group'] == '一般'], index=["FilterLess35", "Year"],  # columns =["Age_Group"],
#                values=['Traffic'],
#                aggfunc=[len, np.max], fill_value=0,)
# # dropna=False)

# Panel_Data = pd.pivot_table(Acc_ID_Final[Acc_ID_Final['Age_Group'] == '一般'],
#                             index=["FilterLess35", "Year"],  # columns =["Age_Group"],
#                             values=['Traffic'],
#                             aggfunc=[len, np.max], fill_value=0,)
# # dropna=False)


# # Here is the working Method that I tried

# Panel_Data = Panel_Data.unstack()

# # Not sure this method is correct.
# year_index = [2006 + i for i in range(10)]
# Panel_Data.reset_index(inplace=True)
# years_index = pd.DataFrame({'Year_New_Index': year_index}, index=year_index)
# Merge1 = pd.merge(Panel_Data, years_index, left_on='Year', right_on='Year_New_Index')
# Merge1.to_excel(Current_Path + "/Results3/Merge1.xlsx", sheet_name="Merge1")


# # This is a bit easier way to do same
# Panel_Data = Panel_Data.unstack().T.stack()
# # Or this method much better
# Panel_Data = Panel_Data.unstack().T
# # Then
# Panel_Data.unstack().T.melt()
# Panel_Data.to_excel(Current_Path + "/Results3/Panel_Data.xlsx", sheet_name="Panel_Data")
