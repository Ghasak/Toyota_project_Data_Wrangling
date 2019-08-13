"""
=========================================================
          WORKING WITH BASEMAP - ANALYSIS GPS
                Wed Aug 14th 2019
                   1:03:00 pm,
=========================================================
    - We will create dummies using the pandas package to
        make all categorical variables dummies.
    - We will remove the non-necessary columns/variables
        from our Survey dataset as we don't need them
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
# print(f"This is the relative path {os.path.abspath(os.getcwd())}")
# print(f"This is the full path {os.path.dirname(os.path.abspath(__file__))}")

df = pd.read_excel(CURRENT_PATH + "/inner_joint_Int.xlsx",
                                 sheet_name="inner_joint_Int" , index = "Unnamed: 0")



# df['Altitude'] = df['Altitude'].astype(float)
# df['Longitute'] = df['Longitute'].astype(float)

# lat = df['Altitude'].values
# lon = df['Longitute'].values
# crash = df['Crash_count'].values


# from mpl_toolkits.basemap import Basemap

# fig = plt.figure(figsize = (8,8))
# m   = Basemap(projection = 'tmerc', resolution = 'h', lat_0 = 35.0826, lon_0 = 137.1561, width = 1E6, height = 1.2E6)



# m.shadedrelief()
# m.drawcoastlines(color='gray')
# m.drawcountries(color='gray')
# m.drawstates(color='gray')

# ==================================================#
#           Import Libraries
# ==================================================#
#necessary imports
from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import CARTODBPOSITRON
import pandas as pd
import numpy as np
import math
from ast import literal_eval
from bokeh.palettes import Viridis5
from bokeh.models import ColumnDataSource,ColorBar,BasicTicker
from bokeh.models.mappers import ColorMapper, LinearColorMapper

#function to convert latitude and longitude into mercator projection mapping
def merc(Coords):
	Coordinates = literal_eval(Coords)
	lat = Coordinates[0]
	lon = Coordinates[1]
	r_major = 6378137.000
	x = r_major * math.radians(lon)
	scale = x/lon
	y = 180.0/math.pi * math.log(math.tan(math.pi/4.0 + lat * (math.pi/180.0)/2.0)) * scale
	return (x, y)

#supporting function
def make_tuple_str(x, y):
	t = (x, y)
	return str(t)

#read with pandas
#df = pd.read_csv('housing.csv')

#converting latitude and longitudes of corners of california into mercator range
range0 = merc('(32.080577, -114.052642)')
range1 = merc('(42.356802, -124.753326)')
x_range = (range0[0],range1[0])
y_range = (range0[1], range1[1])

#now convert DataFrame longitude and latitude column into mercator coordinates
df['coords'] = df.apply(lambda x: make_tuple_str(x['latitude'], x['longitude']), axis = 1)
df['coords_latitude'] = df['coords'].apply(lambda x: merc(x)[0])
df['coords_longitude'] = df['coords'].apply(lambda x: merc(x)[1])

#prepare data
source = ColumnDataSource(
	data = dict(
		lat = df['coords_latitude'].tolist(),
		lon = df['coords_longitude'].tolist(),
		size = df.median_income.tolist(),
		color = df.median_house_value.tolist()
		)
	)

#initiate figure
p = figure(x_range = x_range, y_range = y_range, x_axis_type = "mercator", y_axis_type = "mercator")
p.add_tile(CARTODBPOSITRON)

#color palette
color_mapper = LinearColorMapper(palette = Viridis5)

#add a glyph
p.circle(x = 'lat', y = 'lon',
		size = 'size',
		color = {'field':'color',
				 'transform':color_mapper},
		source = source
		)
#put a colorbar to support
color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                     label_standoff=12, border_line_color=None, location=(0,0))

#layout
p.add_layout(color_bar, 'right')

#show it in web browser
output_file('example.html')

show(p)


