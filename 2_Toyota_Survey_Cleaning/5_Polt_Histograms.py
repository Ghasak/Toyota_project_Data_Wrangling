import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

Pivot_table1 = pd.read_excel("/Users/Ghasak/Desktop/MPDATA/Projects/Toyota_project_Data_Wrangling/2_Toyota_Survey_Cleaning/Toyota_Survey_Sheetfiles/4_Refine_Dataframe/refined_df.xlsx", sheet_name=0)
# Resources: https://matplotlib.org/tutorials/text/text_intro.html
# ==================================================#
#      Distribution Layout of each Driver age
# ==================================================#

fig = plt.figure(figsize=(12, 10))
# fig.suptitle('bold figure suptitle', fontsize=20, fontweight='normal')  # 'bold'

bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
font_var = 20
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 18}
plt.rc('font', **font)
plt.rcParams['axes.labelsize'] = 25
plt.rcParams['axes.labelweight'] = 'normal'
# ================== Total Crash Count ========================
ax = fig.add_subplot(221)
# ax.set_title('Crash_count')
ax.set_xlabel('Total crash counts \n [a]')  # , fontsize=font_var
ax.set_ylabel('No. of intersections')  # . , fontsize=font_var
plt.ylim(0, 300, 10)
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')
P1 = Pivot_table1['Crash_count'].hist(alpha=0.8,
                                      bins=bins,
                                      align='left',
                                      color='#607c8e',
                                      edgecolor='black',
                                      linewidth=1.2)  # ,fc="None"
# removing top and right borders
plt.rcParams['patch.force_edgecolor'] = False
#plt.rcParams['patch.facecolor'] = 'b'
plt.rcParams['axes.labelsize'] = 25
plt.rcParams['axes.labelweight'] = 'normal'
P1.spines['top'].set_color('black')
P1.spines['bottom'].set_color('black')
P1.spines['right'].set_color('black')
P1.spines['left'].set_color('black')
max_total = Pivot_table1['Crash_count'].max()
mean_total = Pivot_table1['Crash_count'].mean()
#P1.text(2, 150, r'$\lambda={:10.3f}, Max={}$'.format(mean_total, max_total))
P1.set_xticks(bins[:-1])


# ================== Young Crash Count ========================
ax = fig.add_subplot(222)
# ax.set_title('Driver_Young')
ax.set_xlabel("Young drivers' crash counts\n [b]")
ax.set_ylabel('No. of intersections')
plt.ylim(0, 300, 10)
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')
P2 = Pivot_table1['Driver_Young'].hist(alpha=0.8,
                                       bins=bins,
                                       align='left',
                                       color='#607c8e',
                                       edgecolor='black',
                                       linewidth=1.2)
# removing top and right borders
plt.rcParams['patch.force_edgecolor'] = True
#plt.rcParams['patch.facecolor'] = 'b'
plt.rcParams['axes.labelsize'] = 25
plt.rcParams['axes.labelweight'] = 'normal'
P2.spines['top'].set_color('black')
P2.spines['bottom'].set_color('black')
P2.spines['right'].set_color('black')
P2.spines['left'].set_color('black')
max_young = Pivot_table1['Driver_Young'].max()
mean_young = Pivot_table1['Driver_Young'].mean()
#P1.text(10, 150, r'$\lambda={:10.3f}, Max={}$'.format(mean_young, max_young))
P2.set_xticks(bins[:-1])
# ================== Middle age Crash Count ========================
ax = fig.add_subplot(223)
# ax.set_title('Driver_Middle_age')
ax.set_xlabel("Middle aged drivers' crash counts\n [c]")
ax.set_ylabel('No. of intersections')
plt.ylim(0, 300, 10)
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')
P3 = Pivot_table1['Driver_Middle_age'].hist(alpha=0.8,
                                            bins=bins,
                                            align='left',
                                            color='#607c8e',
                                            edgecolor='black',
                                            linewidth=1.2)
# removing top and right borders
plt.rcParams['patch.force_edgecolor'] = True
#plt.rcParams['patch.facecolor'] = 'b'
plt.rcParams['axes.labelsize'] = 25
plt.rcParams['axes.labelweight'] = 'normal'
P3.spines['top'].set_color('black')
P3.spines['bottom'].set_color('black')
P3.spines['right'].set_color('black')
P3.spines['left'].set_color('black')
#P3.text(5, 45, r'$\mu=15, b=3$')
P3.set_xticks(bins[:-1])
# ================== Senior Crash Count ========================
ax = fig.add_subplot(224)
# ax.set_title('Driver_Senior')
ax.set_xlabel("Senior drivers' crash counts\n [d]")
ax.set_ylabel('No. of intersections')
plt.ylim(0, 300, 10)
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')
#plt.gca().set_aspect('equal', adjustable='box')
P4 = Pivot_table1['Driver_Senior'].hist(alpha=0.8,
                                        bins=bins,
                                        align='left',
                                        color='#607c8e',
                                        edgecolor='black',
                                        linewidth=1.2)
# removing top and right borders
plt.rcParams['patch.force_edgecolor'] = True
#plt.rcParams['patch.facecolor'] = 'b'
plt.rcParams['axes.labelsize'] = 25
plt.rcParams['axes.labelweight'] = 'normal'
P4.spines['top'].set_color('black')
P4.spines['bottom'].set_color('black')
P4.spines['right'].set_color('black')
P4.spines['left'].set_color('black')
#P4.text(25, 50, r'$\mu=3, b=3$')
P4.set_xticks(bins[:-1])
# plt.rc('xtick', labelsize=20)
# plt.rc('ytick', labelsize=20)
plt.show()
# Pivot_table1['bins'] = pd.cut(Pivot_table1['Crash_count'], [0,5,10,15,20,25,30,35,40,45,50,55])
# Pivot_table1['Driver_Young'].hist(alpha=0.4, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# Pivot_table1['Driver_Middle_age'].hist(alpha=0.4, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# Pivot_table1['Driver_Senior'].hist(alpha=0.4, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# plt.show()
# <2> Using groupby function
# Acc_ID_Final_2.groupby('FilterLess35').aggregate({'traffic_volume':np.max, 'log_traffic_volume':np.max})
# ========= How to see what is have been grouped =======
# # Method[1]
# Acc_ID_Final_2.groupby('FilterLess35').describe()
# # Method[2]
# for key, item in Acc_ID_Final_2.groupby('FilterLess35'):
#     print(key,item)


# plt.figure(figsize=(12, 10))
# # plt.subplot(2,2,1)
# plt.rc('font', **font)
# font = {'family': 'Times New Roman', fontweight: 'normal', 'size': 10}  # normal bold
# plt.subplot(221, xlabel='x \n[a]', ylabel='y', title='title')
# plt.title('Crash_count')

# begone the right, left, top and bottom spines
# P1.spines['bottom'].set_color('red')
# P1.spines['right'].set_visible(True)
# P1.spines['top'].set_visible(True)
# P1.spines['bottom'].set_visible(True)
# P1.spines['left'].set_visible(True)


# Example:
# plt.rcParams["font.weight"] = "normal"
# plt.rcParams["axes.labelweight"] = "normal"

# plt.plot([2, 3, 1], label="foo")
# plt.plot([3, 1, 3], label="bar")

# plt.legend(title="Legend Title")
# plt.xlabel("xLabel")

# plt.show()
