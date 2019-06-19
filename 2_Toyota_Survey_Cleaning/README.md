# Toyota City Data Cleaning
## Progress of work

We can run the script either using python terminal as

```py
python 3_Creating_Dummies_continued.py
```
or using the **magic** commands such as

```py
%run 3_Creating_Dummies_continued.py
```
## Step -1- Prepare exporting the results
Exported the results in the end of the script as

```py
inner_joint_Int.to_excel(Current_Path + "/Toyota_Survey_Sheetfiles/3_Results_Creating_dummies_cont/inner_joint_Int_Create_D2.xlsx", sheet_name="inner_joint_Int_Create_D2")
```
## Step -2- Here we will add more variables
Classify all the variable based on the characteristic of each arm.

| **Variable Name**  | **Status**   | **Information**
| -------------      | -------------| -------------
|  Intersection Type | Checked      | 12 variables here
|                    |              |

### NOTE
In Pandas (pd), if you want to create a copy of a current database you can use

```py
df.copy(deep=TRUE)
```
this will insure to make a copy of your current dataframe, this is a solution to not use the following

```py
df = df_original
```
which is a reference to your original data frame.
and if you use **inplace =TRUE** it will change both of them. Thus we will use a copy. See here details
https://stackoverflow.com/questions/40661930/make-a-copy-of-dataframe-inside-function-without-changing-original/40661986

