
"""
Non-supervised machine learning techniques
less No. 36
MacBook Pro 13''
Tue Aug 21st 2018, 2:24:45
Web-link:
https://pythonprogramming.net/working-with-non-numerical-data-machine-learning-tutorial/
Python version = 4.6
Environment = MacBook_Env
Topic:
Machine Learning - Clustering Introduction
algorithm:
K-Means algorithm (Clustering and Unsupervised machine learning)
"""

"""
Pclass Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
survival Survival (0 = No; 1 = Yes)
name Name
sex Sex
age Age
sibsp Number of Siblings/Spouses Aboard
parch Number of Parents/Children Aboard
ticket Ticket Number
fare Passenger Fare (British pound)
cabin Cabin
embarked Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
boat Lifeboat
body Body Identification Number
home.dest Home/Destination
"""

""" Our goal is to know which one will die and which one will survive
    can we figure out which one will survive and who will die
"""
#########################################################
#       Import the packages (modules)
#########################################################

import matplotlib
matplotlib.use('TkAgg')
# These two commands up you can remove when you use Windows (they are for Mac user)
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing, model_selection   # (model_selection is now instead of cross-validation)
import pandas as pd

#########################################################
#       Import dataset of TITANIC
#########################################################
df = pd.read_excel('/Users/Ghasak/Desktop/1_Cleaning_Toyota_Data/Python_Cleaning/K_Means_ML/titanic.xls')   # you have to use the extension xls which is necessary (xlrd is not define)
# print(df.head())                    # adding df.head() you can see columns as you starch your terminal screen

#########################################################
#       Clean the data
#########################################################
# first you need to remove some columns that cannot be used
# in the feature set (reflect no meaning) or not good
# explanatory variables

df.drop(['body','name',], 1,inplace=True)   # Body identification number has no meaning, also the name whether
# to survive or not
# print(df.head())

df.convert_objects(convert_numeric= True) # convert all the objects in your dataset into numeric numbers (not text)
# pd. to_numeric is not working and here he corrected
df.fillna(0,inplace= True)                # This will fill the (na) values with the 0 instead of removing these data

#########################################################
#       Prepare some function to clean the data
#########################################################
# the core of this segment is to convert the text column values (male/female) or any variable like (big/medium/sma
# or larger than 3 until (infinite) of numbers of groups then you can use this function
# to convert the categorical data column to a numeric ID column (for binary it will be dummy like (0,1)
def handle_non_numerical_data(df):
    columns = df.columns.values  # This is basically every column in your dataset as a list
    for column in columns:
        text_digit_vals = { }     # its an empty dictionary (here for example we will get {'Female':0,'Male':1}
        def convert_to_int(val):
            return text_digit_vals[val]

        # Now checking column by column in the data-frame the data type of the column (if its not text)
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()  # to convert a column in the dataset into a list
            # print(len(column_contents))
            unique_elements = set(column_contents)        # to convert a list into a set {}
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+= 1   # we are populating the dictionary that we created

            df[column] = list(map(convert_to_int,df[column]))   # check panda tutorial for more details on mapping

    return df

df = handle_non_numerical_data(df)
print(df.head())

#########################################################
#       Prepare some function to clean the data
#########################################################
df.drop(['ticket'],1,inplace= True)
X = np.array(df.drop(['survived'],1).astype(float))
X = preprocessing.scale(X)   # Shuffling the dataset
print(df.head())
# The line above is the features and we dropped the column
# survived since its the result that we want to get if we
# include it it seems like cheating, but we will use this
# column later to verify or text our model later.

y = np.array(df['survived'])

clf =KMeans(n_clusters= 2)
clf.fit(X)


correct = 0

for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))    # we can use labels from previous tutorial P.34
    predict_me = predict_me.reshape(-1,len(predict_me))
    prediction =clf.predict(predict_me)
    #print(prediction[0],y[i])

    if prediction[0] == y[i]:
        correct += 1

print(correct/len(X))



