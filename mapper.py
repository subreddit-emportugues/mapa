import linecache
import folium
import time
from folium.features import CustomIcon
from geopy import Nominatim 
from geopy.exc import GeocoderTimedOut
from geopy.exc import GeocoderServiceError



geonames_account=''
g = Nominatim(user_agent=geonames_account)
marker_group = folium.FeatureGroup("Places")
with open('places.txt', 'r') as f:
    line_counter = 0
    for place in f:
        line_counter += 1
        place_location = g.geocode(place, addressdetails=True, timeout=1000)
        subreddit_line = linecache.getline('subreddits.txt', line_counter)
        marker_group.add_child(folium.Marker(
            location = [place_location.latitude, place_location.longitude],
            icon = folium.Icon(color="orange"),
            popup = folium.Popup('<a href="https://www.reddit.com/' + subreddit_line + '" target="_blank" style="font-weight:bold;">' + subreddit_line + '</a>')
        ))
        time.sleep(1)
m = folium.Map(location=[0, 0])
m.add_child(marker_group)
m.save('map.html')
m
map_id = m.get_name()
js_sub =f'''            var {map_id} = L.map(
                "{map_id}",
                {{
                    center: [0.0, 0.0],
                    crs: L.CRS.EPSG3857,
                    zoom: 10,
                    zoomControl: true,
                    preferCanvas: false,
                }}
            );
'''
js_block =f'''            var {map_id} = L.map("{map_id}");

            {map_id}.setView([0, 0], 3);

            var southWest = L.latLng(-90, -180),
            northEast = L.latLng(90, 180);
            var bounds = L.latLngBounds(southWest, northEast);

            {map_id}.setMinZoom(2);
            {map_id}.setMaxBounds(bounds);
            {map_id}.on('drag', function() {{
                {map_id}.panInsideBounds(bounds, {{ animate: false }});
            }});
'''
css_sub ='''            </style>
        
</head>
'''
css_block ="""            </style>
            <style>.leaflet-container a.leaflet-popup-close-button{display: none;important!}</style>
</head>
"""
with open('map.html','r+') as f:
    filedata = f.read()
    new_text = filedata.replace(js_sub, js_block).replace(css_sub, css_block)
    f.seek(0)
    f.write(new_text)
    f.truncate()
