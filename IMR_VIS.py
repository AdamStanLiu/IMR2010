
# coding: utf-8

# ### Import googlemaps package and login with the key

# In[1]:

import googlemaps


# In[2]:

gomaps = googlemaps.Client(key='AI...')


# ### Check the result and data type

# In[3]:

geocode_result = gomaps.geocode('China')


# In[4]:

geocode_result


# ### Import IMR data

# In[2]:

import pandas as pd
import numpy as np 


# In[3]:

IMR = pd.read_csv('IMR.csv',encoding = "ISO-8859-1")


# In[7]:

IMR[:5]


# In[8]:

len(IMR['Area'])


# ### Extract the latitude and longitude from googlemaps

# In[9]:

lat = []
lng = []


# In[10]:

for i in range(len(IMR['Area'])):
    gm_re = gomaps.geocode(IMR['Area'][i])
    lat.append(gm_re[0]['geometry']['location']['lat'])
    lng.append(gm_re[0]['geometry']['location']['lng'])    


# In[11]:

len(lng)


# ### Write geoinfomation data for Tableau drawing the maps

# In[12]:

country = list(IMR['Area'])


# In[13]:

col=['Country','Latitude','Longitude']


# In[14]:

geoinf = pd.DataFrame([country,lat,lng], col)
geoinf = geoinf.transpose()


# In[15]:

geoinf


# In[16]:

geoinf.to_csv('geoinf.csv')


# ### Or use gmaps package to plot in jupyter

# In[4]:

from matplotlib.cm import viridis
from matplotlib.colors import to_hex

import gmaps
import gmaps.geojson_geometries


# In[5]:

gmaps.configure(api_key="AI...")


# In[6]:

# load geojson
countries_geojson = gmaps.geojson_geometries.load_geometry('countries')


# In[7]:

imr_max = max(IMR['Data Value'])
imr_min = min(IMR['Data Value'])
imr_range = imr_max - imr_min


# In[8]:

def calc_color(imr):
    norm_imr = (imr - imr_min) / imr_range
    inv_imr = 1.0 - norm_imr
    mpl_color = viridis(inv_imr)
    gmaps_color = to_hex(mpl_color, keep_alpha=False)
    return gmaps_color


# In[9]:

colors = []
for feature in countries_geojson['features']:
    country_name = feature['properties']['name']
    try:
        if(len(IMR.loc[IMR['Area'] == country_name]['Data Value'])):
            imr = int(IMR.loc[IMR['Area'] == country_name]['Data Value'])
            color = calc_color(imr)
    except KeyError:
        # no IMR for that country: return default color
        color = (0, 0, 0, 0.3)
    colors.append(color)


# In[10]:

fig = gmaps.figure()
imr_layer = gmaps.geojson_layer(countries_geojson, 
                                fill_color=colors, 
                                stroke_color=colors,
                                fill_opacity=0.8)
fig.add_layer(imr_layer)


# In[11]:

fig


# In[ ]:



