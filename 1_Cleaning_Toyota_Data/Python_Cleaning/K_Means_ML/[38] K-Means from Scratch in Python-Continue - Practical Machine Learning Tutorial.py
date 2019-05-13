
"""
Non-supervised machine learning techniques (Flat Clustering)
less No. 37
MacPro
Thu. Aug. 23rd 2018, 15:40:52
Web-link:
https://www.youtube.com/watch?v=H4JSN_99kig&index=37&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&frags=pl%2Cwn
Python version = 4.6
Environment = MacPro_Env
Topic:
Machine Learning - Clustering Introduction
algorithm:
K-Means algorithm (Clustering and Unsupervised machine learning)

We will take some code from the part .34
"""
"""
Non-supervised machine learning techniques
less No. 38
MacPro
Thu. Aug. 23rd 2018, 15:40:52
Web-link:
https://pythonprogramming.net/machine-learning-clustering-introduction-machine-learning-tutorial/
Python version = 4.6
Environment = MacBook_Env
Topic:
Machine Learning -Clustering Introduction
algorithm:
K-Means algorithm (Clustering and Unsupervised machine learning)
Current Update location :~/Volumes/MacPro [Time Machine]/MEGA/MEGAsync/[8] Programming Cloud/[9] Python_codes/Machine_Learning
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

#########################################################
#       Input the dataset (features)
#########################################################
# x = np.array([[1,2],
#               [1.5,1.8],
#               [5,8],
#               [8,8],
#               [1,0.6],
#               [9,11]])

print("The ID here is =","23-K05867-000")
x = np.array([[35.07110167, 137.147385 ],
                [35.07121056, 137.1518367],
                [35.07203028, 137.1478344],
                [35.07223778, 137.1492817],
                [35.072265  , 137.1502906],
                [35.06836194, 137.1521222],
                [35.06835306, 137.1521222],
                [35.06811833, 137.1513328],
                [35.07166056, 137.1475931],
                [35.07121056, 137.1518478],
                [35.06809139, 137.1512781],
                [35.07222861, 137.1479   ],   
                [35.07222861, 137.1478233],
                [35.07213833, 137.1479111],
                [35.07222917, 137.1519022],
                [35.0721475 , 137.1479439],
                [35.07223806, 137.1518475],
                [35.07209333, 137.1473847],
                [35.07145389, 137.1518256],
                [35.07203917, 137.1478233],
                [35.07217444, 137.1478892],
                [35.07212944, 137.1478781],
                [35.07228333, 137.1518364],
                [35.07202139, 137.1478125]])


x = x.astype(float)

plt.scatter(x[:, 0], x[:, 1], s=20, linewidths=2)
## setting the limits on the x-axis and y-axis

#plt.show()

"""
    - Function to calcuate the distance measuring between two coordinates.
    - Considering the earth curvture.

"""

def measure(lat1,lon1,lat2,lon2):
    # Website :https://stackoverflow.com/questions/639695/how-to-convert-latitude-or-longitude-to-meters
    # Formula :https://en.wikipedia.org/wiki/Haversine_formula
    R = 6378.137        # Radius of Earth in Km
    dlat = (lat2-lat1)*(np.pi/180)
    dlon = (lon2-lon1)*(np.pi/180)
    a = (np.sin(dlat/2)*np.sin(dlat/2))+(np.cos(lat1*np.pi/180)*np.cos(lat2*np.pi/180))*(np.sin(dlon/2)*np.sin(dlon/2))
    c = 2 * np.arctan2(np.sqrt(a),np.sqrt(1-a))
    d = R*c
    return (d*1000)     # distance in meter
    # Tested with 
    # measure(35.07121056, 137.1518367,35.07110167, 137.147385) 
    # measure(x[13][0],x[13][1],x[12][0],x[12][1]) = 12.844 meter


list_distance = []
intersection1 = []
not_included = []
measure_dist = 0
for i in range (len(x)):
    # list_distance.append(measure(x[i+1][0],x[i+1][1],x[i][0],x[i][1]))
    # list_distance.append(measure(x[0,0],x[0,1],x[i,0],x[i,1]))
    measure_dist = measure(x[0,0],x[0,1],x[i,0],x[i,1])
    list_distance.append(measure_dist)
    if measure_dist < (100):
        intersection1.append(measure_dist)
    else:
        not_included.append(measure_dist)







#########################################################
#       Applying your machine learning tech.
#########################################################

colors = 10*["r", "b", "k", "g", "c"]  # green, red , cyan, blue , black, orange


#########################################################
#       Define our Class of K-Means
#########################################################


class K_Means:
#########################################################

    def __init__(self, k=3, tol=0.001, max_iter=300):
        # K: is the number of classes, tolerance and max number of Iter
        self.k = k
        self.tol = tol
        self.max_iter = max_iter
##########################################################

    def fit(self, data):
        self.centroids = {}
        counter = 1

        for i in range(self.k):
            self.centroids[i] = data[i]             # We will select the first two data set as a centroids

        for i in range (self.max_iter):
            self.classifications = {}               # This will change every time to find the real centroids

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:                 # I have changed X to Data which he forgot to do.
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))        # the minimum distances are the classes
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                # To redefine the new centroid for us then.
                # if you remove this loop you will get the initial centroids (first guess)
                # this here will re-iterate to find the real locations of the centroids of the classes.
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            Optimized = True


            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]

                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    # To show the number of iterations to our classifier we can get
                    Iter = (np.sum((current_centroid-original_centroid)/original_centroid*100.0))
                    print("Number of Iterations is = {} of {}".format(counter, Iter))
                    Optimized = False
                    counter += 1


            if Optimized:
                break
##########################################################

    def predict(self,data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))  # the minimum distances are the classes
        return classification


#########################################################
#       Define our Class of K-Means
#########################################################

clf = K_Means()
clf.fit(x)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                marker="o", color="k", s=150, linewidths=5)

for classificiation in clf.classifications:
    color =colors[classificiation]
    for featureset in clf.classifications[classificiation]:
        plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=150, linewidths=5)


# Lets do some prediction here


# unkowns = np.array([[1, 3],
#                     [8, 9],
#                     [0, 3],
#                     [5, 4],
#                     [6, 4], ])

# for unkown in unkowns:
#     classificiation = clf.predict(unkown)
#     plt.scatter(unkown[0], unkown[1], marker="*", color=colors[classificiation], s=150, linewidths=5)

plt.show()






