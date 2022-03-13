import folium
import pandas

# create a dataframe of the file
data = pandas.read_csv("Volcanoes.txt")
# list that will contain latitudes
lat = list(data["LAT"])
# list that will contain longitudes
lon = list(data["LON"])
# list that will contain volcano names
volNames = list(data["NAME"])
# list that contains the location of Volcanoes
location = list(data["LOCATION"])
# list that contains status of volcano
status = list(data["STATUS"])
# list that contains elevations of Volcanoes
elevations = list(data["ELEV"])

# function to determine the color of the marker based upon elevation
def determine_color(elev):
    if elev < 1000:
        return 'green'
    elif elev >= 1000 and elev < 2000:
        return 'blue'
    elif elev >= 2000 and elev < 3000:
        return 'purple'
    else:
        return 'red'
# create a map
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My map")

# create a marker in each coordinate
for lt, ln, names, loc, stat, el in zip(lat, lon, volNames, location, status, elevations):
    tempString = "Volcano Name: {} \nLongitude: {} \nLatitude: {} \nLocation: {} \nStatus: {}" .format(names, ln, lt, loc, stat, el)
    #pp = folium.Html(tempString)
    popup = folium.Popup(tempString, max_width=180)
    fg.add_child(folium.Marker(location=[lt, ln], popup = popup, icon=folium.Icon(color=determine_color(el))))


map.add_child(fg)

map.save("Map1.html")
