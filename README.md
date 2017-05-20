# IMR2010
Visualize Infant mortality rate (IMR) 2010

The infant mortality rate (IMR) data can be downlaoded from Devinfo, a database developed by UNICEF in cooperation with the UN System to assist the UN and Member States in tracking progress toward the Millennium Development Goals (MDGs). 'IMR.csv' in this repository contains the Infant mortality rate (IMR) -- Deaths per 1000 live births of the countrys in 2010.

## 1. Visualizing in Tableau

Tableau (https://www.tableau.com/) is a powerful tool for visualizing data. It has a mapping functionality which is very ease to use. To plot IMR on a map in Tableau, we also need the geographic data that connect the IMR data with the map and there are two ways for Tableau to read the spatial information.

### 1.1 Use the Spatial file

The Spatial file can be a shapefile, a MapInfo table or a GeoJSON. More information about the acceptable file types and connecting to Spacial files in Tableu can be found in http://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_shapefiles.html. 
Use the geojson file from http://data.okfn.org/data/datasets/geo-boundaries-world-110m, and build the map for Asian IMR in two dimensions (IMR and economy):

<div class='tableauPlaceholder' id='viz1495268449957' style='position: relative'><noscript><a href='#'><img alt='IMR_Asia_2010 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IM&#47;IMR2010_Asia&#47;IMR_Asia_2010&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='site_root' value='' /><param name='name' value='IMR2010_Asia&#47;IMR_Asia_2010' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IM&#47;IMR2010_Asia&#47;IMR_Asia_2010&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1495268449957');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1004px';vizElement.style.height='869px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>



<div class='tableauPlaceholder' id='viz1495268449957' style='position: relative'><noscript><a href='#'><img alt='IMR_Asia_2010 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IM&#47;IMR2010_Asia&#47;IMR_Asia_2010&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='site_root' value='' /><param name='name' value='IMR2010_Asia&#47;IMR_Asia_2010' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IM&#47;IMR2010_Asia&#47;IMR_Asia_2010&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object></div>           
