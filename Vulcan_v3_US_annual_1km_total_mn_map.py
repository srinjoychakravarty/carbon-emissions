"""
Created on Wed Nov 25 17:28:43 2020
@author: Eeshan
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

filename = 'Vulcan_v3_US_annual_1km_total_mn.nc4'
data =  Dataset(filename) 
# print(data)

x_data = data.variables['x'][:]
print(f"\nx_data: {x_data}")
print(f"\nx datatype: {type(x_data)}")
print(f"\nx total items: {x_data.size}")
print(f"\nx non-masked elements: {x_data.count()}")


y_data = data.variables['y'][:]
print(f"\ny_data: {y_data}")
print(f"\ny datatype: {type(y_data)}")
print(f"\ny total items: {y_data.size}")
print(f"\ny non-masked elements: {y_data.count()}")

lats = data.variables['lat'][:]
print(f"\nlats: {lats}")
print(f"\nlats datatype: {type(lats)}")
print(f"\nlats total items: {lats.size}")
print(f"\nlats non-masked elements: {lats.count()}")

lons = data.variables['lon'][:]
print(f"\nlons: {lons}")
print(f"\nlons datatype: {type(lons)}")
print(f"\nlons total items: {lons.size}")
print(f"\nlons non-masked elements: {lons.count()}")

time = data.variables['time'][:]
print(f"\ntime: {time}")
print(f"\ntime datatype: {type(time)}")
print(f"\ntime total items: {time.size}")
print(f"\ntime non-masked elements: {time.count()}")

emissions = data.variables['carbon_emissions'][:]
print(f"\nemissions: {emissions}")
print(f"\nemissions datatype: {type(emissions)}")
print(f"\nemissions total items: {emissions.size}")
print(f"\nemissions non-masked elements: {emissions.count()}")
print(f"\nemissions masked elements: {(emissions.size) - (emissions.count())}")

mp = Basemap(projection = 'lcc',
             llcrnrlon = -121.239177,
             llcrnrlat = 28.505245,
             urcrnrlon = 45.124307,
             urcrnrlat = -54.966528,
             lat_1= 33.0,
             lon_0= -97.0,
             resolution = 'i')

print(f"\nBasemap Projection Object: {mp}")

lon, lat = np.meshgrid(x_data, y_data)
print(f"\nlongitudes: {lon}")
print(f"\nlongitudes datatype: {type(lon)}")
print(f"\nlongitudes total items: {lon.size}")
print(f"\nlongitudes non-masked elements: {lon.count()}")
print(f"\nlongitudes first element: {lon[0]}")
print(f"\nlongitudes datatype of first element: {type(lon[0])}")
print(f"\nlongitudes first element within first element: {lon[0][0]}")
print(f"\nlongitudes datatype of first element within first element: {type(lon[0][0])}")

print(f"\nlatitudes: {lat}")
print(f"\nlatitudes datatype: {type(lat)}")
print(f"\nlatitudes total items: {lat.size}")
print(f"\nlatitudes non-masked elements: {lat.count()}")
print(f"\nlatitudes first element: {lat[0]}")
print(f"\nlatitudes datatype of first element: {type(lat[0])}")
print(f"\nlatitudes first element within first element: {lat[0][0]}")
print(f"\nlatitudes datatype of first element within first element: {type(lat[0][0])}")

a, b = mp(lon, lat)

print(f"\na: {a}")
print(f"\nType a: {type(a)}")

print(f"\nb: {b}")
print(f"\nType b: {type(b)}")

np_squeezed = np.squeeze(emissions[1, :, :])
print(f"\nNP Squeezed: {np_squeezed}")
print(f"\nNP Squeezed Type: {type(np_squeezed)}")

c_scheme = mp.pcolormesh(a, b, np_squeezed, cmap = 'jet')
print(f"\nC Scheme Object Memory Address: {c_scheme}")
print(f"\nC Scheme Datatype: {type(np_squeezed)}")

# c_scheme = mp.pcolor(a, b, np.squeeze(emissions[1,:,:]), cmap = 'jet')

mp.drawcoastlines()
mp.drawstates()
mp.drawcountries()

plt.title('Average Carbon Emissions for 2010')
plt.show()