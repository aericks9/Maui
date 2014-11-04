import cPickle
import requests 
import json 
import csv

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import Graphics as artist

from mpl_toolkits.basemap import Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
from geopy import geocoders
from pprint import pprint
from random import random


from matplotlib import rcParams

rcParams['text.usetex'] = True
# Lambert Conformal map of lower 48 states.
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
# draw state boundaries.
shp_info = m.readshapefile('st99_d00','states',drawbounds=True)
#counts = cPickle.load(open('classified-tweets.pkl','rb'))
#density = {}

with open('state.csv','rb') as f:
	reader = csv.reader(f)
	convert_names = {line[1]:line[0] for line in reader}

#density = {convert_names[key]:value 
#		for key,value in json.load(open('location-quotient.json','rb')).iteritems()}
# choose a color for each state based on population density.



density = {convert_names[key]:value 
            for key,value in json.load(open('lq-count-tracker','rb')).iteritems()}


#density = json.load(open('actual-usage.json','rb'))

with open('/Volumes/My Book/Dropbox/Utah/table_8_nsduh_with_population_scaled','rU') as f:
    input_file = csv.DictReader(f)
    nsduh = {row['State']:float(row['NSDUH']) for row in input_file}

with open('/Volumes/My Book/Dropbox/Utah/table_8_nsduh_with_population_scaled','rU') as f:
    input_file = csv.DictReader(f)
    toxtweet = {row['State']:float(row['ToxTweet']) for row in input_file}

pprint(toxtweet)

denom = sum(density.values())
colors={}
statenames=[]
cmap = plt.cm.seismic # use 'hot' colormap
vmin = 0; vmax = 1 # set range.
for shapedict in m.states_info:
    statename = shapedict['NAME']
    pop = nsduh[statename] if statename in nsduh else 0
#    colors[statename] = cmap((pop-mn)/float(mx-mn))[:3]
    colors[statename] = cmap(pop)[:3]#cmap((pop/float(denom)))[:3]
    statenames.append(statename)

ax = plt.gca() # get current axes instance
ax.patch.set_alpha(0)
for nshape,seg in enumerate(m.states):
    # skip DC and Puerto Rico.
    if statenames[nshape] not in ['District of Columbia','Puerto Rico']:
        color = rgb2hex(colors[statenames[nshape]]) 
        poly = Polygon(seg,facecolor=color,edgecolor=color)
        ax.add_patch(poly)
        ax.annotate(r'\Large \textbf{\textsc{NSDUH}}', xy=(.5, .8),  xycoords='figure fraction',
             ha="left", va="bottom")
cbar = plt.gcf().add_axes([0.92, 0.2, 0.03,0.6])
norm = mpl.colors.Normalize(vmin=-2.5,vmax=2.5)
cb1 = mpl.colorbar.ColorbarBase(cbar,cmap=cmap,norm=norm,orientation='vertical')
artist.adjust_spines(ax,[])
plt.show()