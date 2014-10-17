import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
m = Basemap(
        projection='merc',
        llcrnrlon=-130,
        llcrnrlat=25,
        urcrnrlon=-60,
        urcrnrlat=50,
        lat_ts=0,
        resolution='i',
        suppress_ticks=True)


# Cali, NYC, Vegas NV, Austin TX
locations = {}

locations['cali'] = {'lat':37.96, 'lon':-121.29}
locations['nyc'] = {'lat':42.82, 'lon':-73.95}
locations['vegas'] = {'lat':36.17, 'lon':-115.17}
locations['austin'] = {'lat':30.26, 'lon':-97.74}

lats = []
lons = []

for place, data in locations.items():
	# position in decimal lat/lon
	lats.append(data['lat'])
	lons.append(data['lon'])

# convert lat and lon to map projection
mx,my = m(lons,lats)

# The NetworkX part
pos = {}
# loop through locations and assign positions as well
for idx, loc in enumerate(locations):
	pos[loc]= (mx[idx],my[idx])


# put map projection coordinates in pos dictionary
G = nx.Graph()
# need to order these points via TSP
G.add_edge('cali','nyc')
G.add_edge('nyc','vegas')
G.add_edge('vegas','austin')

# draw
nx.draw_networkx(G,pos,node_size=200,node_color='blue')

# Now draw the map
m.drawcountries()
m.drawstates()
m.bluemarble()
plt.title('My maps')
plt.savefig('foo.png')