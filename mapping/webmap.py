import folium, pandas

_data = pandas.read_csv("/home/will/projects/Python-Projects/mapping/Volcanoes.txt")
lat = list(_data["LAT"])
lon = list(_data["LON"])
volcano = list(_data["NAME"])
elev = list(_data["ELEV"])

def colour_producer(elevation):
    if elevation < 2000:
        return 'green'
    elif 2000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[39.03,-97.60], zoom_start=4, tiles = "Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, nm, el in zip(lat, lon, volcano, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 10, color = colour_producer(el), fill_color = colour_producer(el), fill_opacity=0.8, popup=nm +" , "+ str(el) + " m"))


map.add_child(fg)

map.save("Map2.html")
