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

map = folium.Map(location=[39.349,-11.86], zoom_start=2, tiles = "Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, nm, el in zip(lat, lon, volcano, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 5, color = colour_producer(el), fill_color = colour_producer(el), fill_opacity=0.8, popup=nm +" , "+ str(el) + " m"))

fg.add_child(folium.GeoJson(data=open("/home/will/projects/Python-Projects/mapping/world.json", 'r', encoding='utf-8-sig'), style_function=lambda x: {'fillColor':'yellow'}))


map.add_child(fg)

map.save("Map2.html")
