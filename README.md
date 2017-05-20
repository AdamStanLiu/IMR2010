# IMR2010
Visualize Infant mortality rate (IMR) 2010

The infant mortality rate (IMR) data can be downlaoded from Devinfo, a database developed by UNICEF in cooperation with the UN System to assist the UN and Member States in tracking progress toward the Millennium Development Goals (MDGs). 'IMR.csv' in this repository contains the Infant mortality rate (IMR) -- Deaths per 1000 live births of the countrys in 2010.

## 1. Visualizing in Tableau

Tableau (https://www.tableau.com/) is a powerful tool for visualizing data. It has a mapping functionality which is very ease to use. To plot IMR on a map in Tableau, we also need the geographic data that connect the IMR data with the map and there are two ways for Tableau to read the spatial information.

### 1.1 Use the Spatial file

The Spatial file can be a shapefile, a MapInfo table or a GeoJSON. More information about the acceptable file types and connecting to Spacial files in Tableu can be found in http://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_shapefiles.html. 

Use the geojson file from http://data.okfn.org/data/datasets/geo-boundaries-world-110m, and build the map for Asian IMR in two dimensions (IMR and economy): 

https://public.tableau.com/views/IMR2010_Asia/IMR_Asia_2010?:embed=y&:display_count=yes



