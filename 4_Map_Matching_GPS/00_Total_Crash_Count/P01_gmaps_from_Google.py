"""
=========================================================
          Creating Dummies for and
            arrange your dataset
            Tue Jun. 19th 2019
                 17:03:00,
=========================================================
    - We will create dummies using the pandas package to
        make all categorical variables dummies.
    - We will remove the non-necessary columns/variables
        from our Survey dataset as we don't need them
    -
"""
# ==================================================#
#           Import Libraries
# ==================================================#
# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import os
CURRENT_PATH = os.getcwd()

print(CURRENT_PATH)
os.chdir(CURRENT_PATH)
CURRENT_PATH = os.getcwd()
# # print(f"This is the relative path {os.path.abspath(os.getcwd())}")
# # print(f"This is the full path {os.path.dirname(os.path.abspath(__file__))}")

# df = pd.read_excel(CURRENT_PATH + "/inner_joint_Int.xlsx",
#                                  sheet_name="inner_joint_Int" , index = "Unnamed: 0")


with open('api_key.txt') as f:
    api_key = f.readline()
    f.close

print(api_key)
import gmaps
gmaps.configure(api_key=api_key)


from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13)

# Polygon
golden_gate_park_lats, golden_gate_park_lons = zip(*[
    (37.771269, -122.511015),
    (37.773495, -122.464830),
    (37.774797, -122.454538),
    (37.771988, -122.454018),
    (37.773646, -122.440979),
    (37.772742, -122.440797),
    (37.771096, -122.453889),
    (37.768669, -122.453518),
    (37.766227, -122.460213),
    (37.764028, -122.510347),
    (37.771269, -122.511015)
    ])
gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=10)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
    (37.769901, -122.498331),
    (37.768645, -122.475328),
    (37.771478, -122.468677),
    (37.769867, -122.466102),
    (37.767187, -122.467496),
    (37.770104, -122.470436)
    ])
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)

# Marker
hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("ghasak_my_map.html")
