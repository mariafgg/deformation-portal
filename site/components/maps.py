from dash import html, dcc
import dash_bootstrap_components as dbc
import requests
import dash_leaflet as dl
import json

# All compiled fractures to February 2023
with open('assets/Allt_WGS84.geojson', 'r') as f:
    All_data = json.load(f)

# Simplified frac network
with open('assets/Simplified_WGS84.geojson', 'r') as f:
    Simplified = json.load(f)

# fracture zones
with open('assets/saemundssonfissureswarms.geojson', 'r') as f:
    geojson_data = json.load(f)

# fractures South Iceland Seismic Zone
with open('assets/fracturessisz.geojson', 'r') as f:
    geojson_data1 = json.load(f)

# fractures Insar Nov 12, 2023
with open('assets/insarfaults20240228.geojson', 'r') as f:
    geojson_data2 = json.load(f)

# fractures ISOR
with open('assets/Faults_and_fissures_by_ISOR.geojson', 'r') as f:
    geojson_data3 = json.load(f)

# Geldingadalir
with open('assets/Lavafield_Geldingadalir_2021.geojson', 'r') as f:
    geojson_data4 = json.load(f)

# Meradalir
with open('assets/Lavafield_Meradalir_2022.geojson', 'r') as f:
    geojson_data5 = json.load(f)

# Litli Hrutur
with open('assets/Lavafield_Litli_Hrutur_2023.geojson', 'r') as f:
    geojson_data6 = json.load(f)

# Gossprungur á Íslandi
with open('assets/gossprungar.geojson', 'r') as f:
    gossprungar = json.load(f)

# Gígar
with open('assets/gigar.geojson', 'r') as f:
    gigar = json.load(f)

# Brotalinar
with open('assets/brotalina.geojson', 'r') as f:
    brotalina = json.load(f)

# Load GPS STations GeoJSON data
with open('assets/gpsstations.geojson', 'r') as f:
    gpsstations = json.load(f)

# New IMO Basemap Tile Layer
imo_basemap_tile_layer = dl.TileLayer(
    url='https://geo.vedur.is/geoserver/www/imo_basemap_epsg3857/{z}/{x}/{y}.png',
    attribution='&copy; Icelandic Meteorological Office basemap'
)

# Örnefni WMS layer from LMÍ
ornefni = dl.WMSTileLayer(
    url="https://gis.lmi.is/geoserver/wms",
    layers="Ornefni",
    format="image/png",
    transparent=True,
    opacity=0.5,
    attribution="&copy; Landmælingar Íslands"
)
# WMS layer from LMÍ
lava_dec = dl.WMSTileLayer(
    url="https://gis.lmi.is/geoserver/wms",
    layers="LMI_vektor:gos_Reykjanes_hraun_ni_lmi_20231221",
    format="image/png",
    transparent=True,
    opacity=0.5,
    attribution="&copy; Landmælingar Íslands"
)

lava_jan = dl.WMSTileLayer(
    url="https://gis.lmi.is/geoserver/wms",
    layers="LMI_vektor:gos_Reykjanes_hraun_hagaf_20240114_1615",
    format="image/png",
    transparent=True,
    opacity=0.5,
    attribution="&copy; Landmælingar Íslands"
)
lava_feb = dl.WMSTileLayer(
    url="https://gis.lmi.is/geoserver/wms",
    layers="LMI_vektor:gos_Reykjanes_hraun_20240213",
    format="image/png",
    transparent=True,
    opacity=0.5,
    attribution="&copy; Landmælingar Íslands"
)

lava_mars = dl.WMSTileLayer(
    url="https://gis.lmi.is/geoserver/wms",
    layers="LMI_vektor:gos_Reykjanes_hraun_vi_ICEYE_20240317",
    format="image/png",
    transparent=True,
    opacity=0.5,
    attribution="&copy; Landmælingar Íslands"
)

jardhitaborholur = dl.WMSTileLayer(
    url="https://gis.lmi.is/geoserver/wms",
    layers="orkustofnun:gisborhola",
    styles="borholur_jardhiti",
    format="image/png",
    transparent=True,
    opacity=1,  # Adjust opacity as needed
    attribution="&copy; Orkustofnun",
    #cql_filter="tilgangurborunar = 'Niðurdælingarhola' OR tilgangurborunar = 'Gufuöflun'"
)

# Creating a GeoJSON layer for the GPS stations
gpsstations_layer = dl.GeoJSON(data=gpsstations, id='gpsstations-layer')

# Extracting station names, latitudes, and longitudes
station_names = gpsstations['gpsstations']['station']
latitudes = gpsstations['gpsstations']['latitude']
longitudes = gpsstations['gpsstations']['longitude']

# Define styles for gossprungar and brotalina
style_gossprungar = {'color': 'orange', 'weight': 3}
style_brotalina = {'color': 'darkblue', 'weight': 2}
style_allt = {'color': 'black', 'weight': 3}


# Create GeoJSON layers for gossprungar and brotalina with specific styles
gossprungar_layer = dl.GeoJSON(data=gossprungar, style=style_gossprungar, id='gossprungar-layer')
brotalina_layer = dl.GeoJSON(data=brotalina, style=style_brotalina, id='brotalina-layer')


# Create circle markers for "gígar"
gigar_markers = [dl.CircleMarker(center=[feature['geometry']['coordinates'][1], feature['geometry']['coordinates'][0]], 
                                 radius=2, color='red', fill=True, fillOpacity=0.8) for feature in gigar['features']]


# Combining them into a list of dictionaries
stations = []
for idx, name in station_names.items():
    station_info = {
        'name': name,
        'latitude': latitudes[idx],
        'longitude': longitudes[idx]
    }
    stations.append(station_info)

# Create station markers
def create_station_markers(stations):
    markers = []
    for station in stations:
        # URLs for the images
        image_url_90d = f"https://cdn.vedur.is/gps/timeseries/graphs/standard_24h/{station['name']}-plate-90d.png"
        image_url_year = f"https://cdn.vedur.is/gps/timeseries/graphs/standard_24h/{station['name']}-plate-year.png"
        image_url_full = f"https://cdn.vedur.is/gps/timeseries/graphs/standard_24h/{station['name']}-plate-full.png"
        data_file_dt_url = f"https://cdn.vedur.is/gps/timeseries/data/post-processing/timeseries/{station['name']}-plate.NEU"
        data_file_fr_url = f"https://cdn.vedur.is/gps/timeseries/data/post-processing/timeseries-fractional/{station['name']}-plate.NEU"

        # Construct the popup content with DBC tabs
        popup_content = dbc.Tabs([
            dbc.Tab(label='90-Daga mynd', children=[
                html.Div([  
                    html.Img(src=image_url_90d, style={'maxWidth': '100%', 'height': 'auto'}),
                    html.A("Opna myndina", href=image_url_90d, target="_blank")
                ], style={'paddingTop': '10px'}),  
            ]),
            dbc.Tab(label='Eitt ár mynd', children=[
                html.Div([
                    html.Img(src=image_url_year, style={'maxWidth': '100%', 'height': 'auto'}),
                    html.A("Opna myndina", href=image_url_year, target="_blank")
                ], style={'paddingTop': '10px'}),
            ]),
            dbc.Tab(label='Allt Tímaröð mynd', children=[
                html.Div([
                    html.Img(src=image_url_full, style={'maxWidth': '100%', 'height': 'auto'}),
                    html.A("Opna myndina", href=image_url_full, target="_blank")
                ], style={'paddingTop': '10px'}),
            ]),
            dbc.Tab(label='Gagna skrár', children=[
                html.Div([
                    html.A("Hlaða niður tímaraðargögnum | datetime format", href=data_file_dt_url, target="_blank", style={'display': 'block', 'marginBottom': '10px'}),
                    html.A("Hlaða niður tímaraðargögnum | fractional format", href=data_file_fr_url, target="_blank")
                ], style={'paddingTop': '10px'}),
            ])
        ], style={'maxWidth': '500px'})

        # Create the marker with the popup
        marker = dl.Marker(
            position=[station['latitude'], station['longitude']],
            children=[
                dl.Tooltip(station['name']),
                dl.Popup(children=popup_content, maxWidth="auto")
            ]
        )
        markers.append(marker)
    return markers


# From 'stations' as already defined
station_markers = create_station_markers(stations)

# Base layers configuration
# Openstreet
open_street_map_tile_layer = dl.TileLayer(
    url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', 
    attribution='© OpenStreetMap contributors'
)


# Esri World Imagery Tile Layer
esri_world_imagery = dl.TileLayer(
    url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attribution='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
)

# Define colors for each GeoJSON layer
colors = ['#FFCCFF', '#CC0000', '#000000', '#541bf3', '#1bf331', '#000000', '#f3f31b']

# function to apply color based on layer
def get_style(color):
    return {'color': color, 'weight': 1, 'opacity': 0.5}

# Adding the MeasureControl to your map
measure_control = dl.MeasureControl(
    position="topleft",
    primaryLengthUnit="kilometers",
    secondaryLengthUnit="miles",
    primaryAreaUnit="sqmeters",
    secondaryAreaUnit="sqmiles",
    activeColor="#214097",
    completedColor="#9721f5"
)

# Map component with toggleable GeoJSON layers and base layers
leafletmap = dl.Map(children=[
    dl.LayersControl([
#        dl.BaseLayer(ornefni, name= "Örnefni", checked=True),
        dl.BaseLayer(imo_basemap_tile_layer, name="VÍ grunnkort/IMO Basemap", checked=True),
        dl.BaseLayer(open_street_map_tile_layer, name="OpenStreetMap", checked=False),
        dl.BaseLayer(esri_world_imagery, name="Gervihnattamynd/Satellite", checked=False),

        ## Lava Flows
        dl.Overlay(lava_dec, name="Hraun/Lavafield við Sundhnúksgíga (19-21 des. 2023), LMÍ, NÍ, JHÍ", checked=True),
        dl.Overlay(lava_jan, name="Hraun/Lavafield við Hagafell 14. jan. 2024 kl. 16:15, LMÍ, NÍ, JHÍ", checked=True),
        dl.Overlay(lava_feb,name="Hraun/Lavafield við Sundhnúksgíga (8. feb 2024), LMÍ, NÍ, JHÍ", checked=True),
        dl.Overlay(lava_mars,name="Hraun/Lavafield við Sundhnúksgíga (17. mars 2024), LMÍ, NÍ, JHÍ", checked=True),
        dl.Overlay(dl.GeoJSON(data=geojson_data4, style=get_style(colors[5])), name="Hraun/Lavafield við Geldingadalir, LMÍ, NÍ, JHÍ, 2021", checked=True),
        dl.Overlay(dl.GeoJSON(data=geojson_data5, style=get_style(colors[5])), name="Hraun/Lavafield við Meradalir, LMÍ, NÍ, JHÍ, 2022", checked=True),
        dl.Overlay(dl.GeoJSON(data=geojson_data6, style=get_style(colors[5])), name="Hraun/Lavafield við Litli Hrútur, LMÍ, NÍ, JHÍ, 2023", checked=True),

        ## Geothermal wells
        dl.Overlay(jardhitaborholur, name="Jarðhítaborholur/Geothermal Wells, Orkustofnun", checked=False),
        # Örnefni
        dl.Overlay(ornefni, name= "Örnefni", checked=True),

        # Fractures
        dl.Overlay(dl.GeoJSON(data=geojson_data, style=get_style(colors[0])), name="Sprungusvæði/Fracture zones, Sæmundsson 2012-2022", checked=False),
        dl.Overlay(dl.GeoJSON(data=brotalina, style=style_brotalina), name="Misgengi/Faults, Náttúrufræðistofnun Íslands (NÍ) 2019", checked=False),
        dl.Overlay(dl.GeoJSON(data=gossprungar, style=style_gossprungar), name="Gossprungur á Íslandi, NÍ 2019", checked=True),
        dl.Overlay(dl.LayerGroup(children=gigar_markers), name="Gígar/Craters, NÍ 2019 ", checked=True),
        dl.Overlay(dl.GeoJSON(data=geojson_data1, style=get_style(colors[1])), name="Virkar jarðskjálftasprungur á Suðurlandi, NÍ 2019", checked=False),
        dl.Overlay(dl.GeoJSON(data=geojson_data2, style=get_style(colors[2])), name="INSAR Misgengi/Faults (Veðurstofa Íslands, 2024)", checked=False),
        dl.Overlay(dl.GeoJSON(data=geojson_data3, style=get_style(colors[3])), name="ISOR Sprungur/Fractures (Jarðfræðikort af Suðvesturlandi, 1, 100., 2012-2022)", checked=False),

    ]),
    dl.ScaleControl(position="bottomleft"),
    *station_markers,
    measure_control
], style={'width': '100%', 'height': '100vh'}, center=[64.73, -18.6], zoom=7, id='leaflet-map')


