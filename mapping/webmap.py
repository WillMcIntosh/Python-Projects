import folium, pandas

_data = pandas.read_csv("/home/will/projects/Python-Projects/mapping/Volcanoes.txt")
lat = list(_data["LAT"])
lon = list(_data["LON"])
volcano = list(_data["NAME"])
elev = list(_data["ELEV"])

#colour of volcano marker for elevation
def colour_producer(elevation):
    if elevation < 2000:
        return 'green'
    elif 2000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[39.349,-11.86], zoom_start=2, tiles = "Mapbox Bright")

fg_p = folium.FeatureGroup(name="Population")
fg_v = folium.FeatureGroup(name="Volcanoes")

#adds json data and using lambda function colours each country based on population data
fg_p.add_child(folium.GeoJson(data=open("/home/will/projects/Python-Projects/mapping/world.json", 'r', encoding='utf-8-sig'), style_function=lambda x: {'fillOpacity':0.7, 'fillColor': 'red' if x['properties'] ['POP2005'] >= 1000000000 else 'orange' if 200000000 <= x['properties'] ['POP2005'] < 10000000000 else 'yellow' if 100000000 <= x['properties'] ['POP2005'] < 200000000 else 'green' if 50000000 <= x['properties'] ['POP2005'] < 100000000 else 'blue' if 25000000 <= x['properties'] ['POP2005'] < 50000000 else 'gray'}))

#feature group used so each volcano belongs to the same volcano layer
for lt, ln, nm, el in zip(lat, lon, volcano, elev):
    fg_v.add_child(folium.CircleMarker(location=[lt,ln], radius = 5, color = colour_producer(el), fill_color = colour_producer(el), fill_opacity=0.8, popup=nm +" , "+ str(el) + " m"))

map.add_child(fg_p)
map.add_child(fg_v)
map.add_child(folium.LayerControl())

map.save("Map2.html")
