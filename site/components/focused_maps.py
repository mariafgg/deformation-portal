from dash import html, dcc
import dash_bootstrap_components as dbc
import requests
import dash_leaflet as dl
import json
from dash import html, dcc
import dash_leaflet as dl
import json
from components.models import mogi_source_geojson, sill_rectangle_geojson


# Loading GIS layers
# Load GeoJSON data
def load_geojson(filename):
    with open(filename, 'r') as f:
        return json.load(f)

All_data = load_geojson('assets/Allt_WGS84.geojson')
Simplified = load_geojson('assets/Simplified_WGS84.geojson')
geojson_data = load_geojson('assets/saemundssonfissureswarms.geojson')
geojson_data1 = load_geojson('assets/fracturessisz.geojson')
geojson_data2 = load_geojson('assets/insarfaults20240228.geojson')
geojson_data3 = load_geojson('assets/Faults_and_fissures_by_ISOR.geojson')
geojson_data4 = load_geojson('assets/Lavafield_Geldingadalir_2021.geojson')
geojson_data5 = load_geojson('assets/Lavafield_Meradalir_2022.geojson')
geojson_data6 = load_geojson('assets/Lavafield_Litli_Hrutur_2023.geojson')
gossprungar = load_geojson('assets/gossprungar.geojson')
gigar = load_geojson('assets/gigar.geojson')
brotalina = load_geojson('assets/brotalina.geojson')
gpsstations = load_geojson('assets/gpsstations.geojson')



# Load GeoJSON data
with open('assets/baselines.geojson', 'r') as f:
    baselines_geojson = json.load(f)


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

# Define styles for line geojsons
style_gossprungar = {'color': 'orange', 'weight': 3}
style_brotalina = {'color': 'darkblue', 'weight': 2}
style_allt = {'color': 'black', 'weight':3}


# Create GeoJSON layers for gossprungar and brotalina with specific styles
gossprungar_layer = dl.GeoJSON(data=gossprungar, style=style_gossprungar, id='gossprungar-layer')
brotalina_layer = dl.GeoJSON(data=brotalina, style=style_brotalina, id='brotalina-layer')
#
## Create circle markers for "gígar"
gigar_markers = [dl.CircleMarker(center=[feature['geometry']['coordinates'][1], feature['geometry']['coordinates'][0]], 
                                 radius=2, color='red', fill=True, fillOpacity=0.8) for feature in gigar['features']]

## Combining them into a list of dictionaries
stations = []
for idx, name in station_names.items():
    station_info = {
        'name': name,
        'latitude': latitudes[idx],
        'longitude': longitudes[idx]
    }
    stations.append(station_info)


# URL or Page to Area Mapping
url_to_area_mapping = {
    'reykjanes': 'reykjanes',
    'askja': 'askja',
    'eyjafjallajokull': 'eyjafjallajokull',
    'hekla': 'hekla',
    'katla': 'katla',
    'bardarbunga': 'bardarbunga',
    'oraefajokull': 'oraefajokull',
    'kverkfjoll': 'kverkfjoll',
    'thorbjorn': 'thorbjorn',
    'grimsvotn': 'grimsvotn',
    # Add other mappings as needed
}

# Function to create station markers and its popups 
def create_station_markers(stations, area_identifier):
    markers = []
    #print('area identifier\n', area_identifier)
    area = url_to_area_mapping.get(area_identifier, 'default')
    #print('mapped area \n', area)
    for station in stations:

        # URLs for the images
        image_url_90d = f"https://cdn.vedur.is/gps/locations/volcanos/{area}/graphs/24h/{station['name']}-plate-90d.png"
        image_url_year = f"https://cdn.vedur.is/gps/locations/volcanos/{area}/graphs/24h/{station['name']}-plate-year.png"
        image_url_since_20200101 = f"https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/24h/{station['name']}-plate_since-20200101.png"
        image_url_since_20231112 = f"https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/24h/{station['name']}-plate_since-20231112.png"
        data_file_dt_url = f"https://cdn.vedur.is/gps/timeseries/data/post-processing/timeseries/{station['name']}-plate.NEU"
        data_file_fr_url = f"https://cdn.vedur.is/gps/timeseries/data/post-processing/timeseries-fractional/{station['name']}-plate.NEU"

        # Constructing the popup content with dbc.Tabs
        popup_content = dbc.Tabs([
            dbc.Tab(label='90-Daga mynd', children=[
                html.Div([
                    html.Img(src=image_url_90d, style={'maxWidth': '100%', 'height': 'auto'}),
                    html.Br(),
                    html.Div([
                        html.Div("Eldgos", style={'color': 'red', 'fontSize': 14, 'paddingRight': '5px'}),
                        html.Div("Innskot", style={'color': 'blue', 'fontSize': 14, 'paddingLeft': '5px'}),
                    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'marginBottom': '20px'}),
                    html.A("Opna myndina", href=image_url_90d, target="_blank")
                ], style={'paddingTop': '10px'}),
            ]),
            dbc.Tab(label='Eitt ár mynd', children=[
                html.Div([
                    html.Img(src=image_url_year, style={'maxWidth': '100%', 'height': 'auto'}),
                    html.Div([
                        html.Div("Eldgos", style={'color': 'red', 'fontSize': 14, 'paddingRight': '5px'}),
                        html.Div("Innskot", style={'color': 'blue', 'fontSize': 14, 'paddingLeft': '5px'}),
                    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'marginBottom': '20px'}),
                    html.A("Opna myndina", href=image_url_year, target="_blank")
                ], style={'paddingTop': '10px'}),
            ]),
            dbc.Tab(label='Síðan 2020-01-01', children=[
                html.Div([
                    html.Img(src=image_url_since_20200101, style={'maxWidth': '100%', 'height': 'auto'}),
                    html.Div([
                        html.Div("Eldgos", style={'color': 'red', 'fontSize': 14, 'paddingRight': '5px'}),
                        html.Div("Innskot", style={'color': 'blue', 'fontSize': 14, 'paddingLeft': '5px'}),
                    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'marginBottom': '20px'}),
                    html.A("Opna myndina", href=image_url_since_20200101, target="_blank")
                ], style={'paddingTop': '10px'}),
            ]),
            dbc.Tab(label='Síðan 2023-11-12', children=[
                html.Div([
                    html.Img(src=image_url_since_20231112, style={'maxWidth': '100%', 'height': 'auto'}),
                    html.Div([
                        html.Div("Eldgos", style={'color': 'red', 'fontSize': 14, 'paddingRight': '5px'}),
                        html.Div("Innskot", style={'color': 'blue', 'fontSize': 14, 'paddingLeft': '5px'}),
                    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'marginBottom': '20px'}),
                    html.A("Opna myndina", href=image_url_since_20231112, target="_blank")
                ], style={'paddingTop': '10px'}),
            ]),
            dbc.Tab(label='Gagnaskrár', children=[
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


# Base layers loading
imo_basemap_tile_layer = dl.TileLayer(url='https://geo.vedur.is/geoserver/www/imo_basemap_epsg3857/{z}/{x}/{y}.png', attribution='&copy; Icelandic Meteorological Office basemap')
ornefni = dl.WMSTileLayer(url="https://gis.lmi.is/geoserver/wms", layers="Ornefni", format="image/png", transparent=True, opacity=0.5, attribution="&copy; Landmælingar Íslands")
open_street_map_tile_layer = dl.TileLayer(url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', attribution='© OpenStreetMap contributors')
esri_world_imagery = dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', attribution='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community')

# Defining styles
colors = ['#FFCCFF', '#CC0000', '#000000', '#541bf3', '#1bf331', '#000000', '#f3f31b']

def get_style(color):
    return {'color': color, 'weight': 1, 'opacity': 0.5}

# Measure control - Not currently active
measure_control = dl.MeasureControl(position="topleft", primaryLengthUnit="kilometers", secondaryLengthUnit="miles", primaryAreaUnit="sqmeters", secondaryAreaUnit="sqmiles", activeColor="#214097", completedColor="#9721f5")

# Function to create tooltips
def create_tooltip(text):
    return dl.Tooltip(text)

# Once all layers have been created and loaded, the map is created based on its feature and the area of interest - This is for Reykjanes only
def create_focused_map(center_lat, center_lon, zoom_level, area_identifier):
    # Function to generate popup from GeoJSON properties
    from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
    def create_popup(feature):
        return dl.Popup([DangerouslySetInnerHTML(feature['properties']['popupContent'])], maxWidth="auto")

    station_markers = create_station_markers(stations, area_identifier)
    
    # Define custom names for each baseline based on its ID
    baseline_names = {
        "3": "ELDC Set 2 RTK Baseline",
        "4": "NAMC RTK Baseline",
        "2": "ELDC Set 1 RTK Baseline",
        "1": "SUDV RTK Baseline"
    }

        # Define image URLs for each rtk (real-time kinematix) solution baseline and tab
    image_urls = {
        "3": {
            "6 tímar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_SENG-ELDC_6h.png",
            "12 tímar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_SENG-ELDC_12h.png",
            "2 dagar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_SENG-ELDC_twodays.png"
        },
        "1": {
            "6 tímar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_SENG-SUDV_6h.png",
            "12 tímar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_SENG-SUDV_12h.png",
            "2 dagar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_SENG-SUDV_twodays.png"
        },
        "2": {
            "6 tímar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_ORFC-ELDC_6h.png",
            "12 tímar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_ORFC-ELDC_12h.png",
            "2 dagar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_ORFC-ELDC_twodays.png"
        },
        "4": {
            "6 tímar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_SENG-NAMC_6h.png",
            "12 tímar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_SENG-NAMC_12h.png",
            "2 dagar": "https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/rtk_SENG-NAMC_twodays.png"
        }
    }
    

    # Initialize the list of children for the map, starting with base layers
    map_children = [
        dl.BaseLayer(imo_basemap_tile_layer, name="VÍ grunnkort/IMO Basemap", checked=True),
        dl.BaseLayer(open_street_map_tile_layer, name="OpenStreetMap", checked=False),
        dl.BaseLayer(esri_world_imagery, name="Gervihnattamynd/Satellite", checked=False),
        # Add other base layers and overlays here
    ]
   
    for feature in baselines_geojson['features']:
        feature_id = feature['properties']['id']
        feature_name = baseline_names.get(feature_id, f"Baseline {feature_id}")  # Fallback to a default name if ID not in baseline_names
        
        # Create popup content with tabs if images are defined for the baseline
        if feature_id in image_urls:
            tabs = []
            for tab_name, img_url in image_urls[feature_id].items():
                tab_content = html.Div([
                    html.Img(src=img_url, style={'width': '100%', 'height': 'auto'}),
                    html.Br(),
                    html.A("Opna myndina", href=img_url, target="_blank", style={'display': 'block', 'textAlign': 'center'})
                ])
                tabs.append(dbc.Tab(tab_content, label=tab_name))
            popup_content = dbc.Tabs(tabs, style={'maxWidth': '500px'})
        else:
            popup_content = "No data available"

        
        feature_layer = dl.GeoJSON(data={
            "type": "FeatureCollection",
            "features": [feature]
        }, id=f'baseline-{feature_id}', children=dl.Popup(children=popup_content, maxWidth="500px"))
   
        
        feature_layer = dl.GeoJSON(data={
            "type": "FeatureCollection",
            "features": [feature]
        }, id=f'baseline-{feature_id}', children=dl.Popup(children=popup_content))
        
        overlay = dl.Overlay(feature_layer, name=feature_name, checked=False)
        map_children.append(overlay)
   

        # Create a CircleMarker for the Mogi source with custom color and tooltip
        mogi_source_marker = dl.CircleMarker(
            center=[mogi_source_geojson['features'][0]['geometry']['coordinates'][1], mogi_source_geojson['features'][0]['geometry']['coordinates'][0]],
            radius=8, color='black', fill=True, fillOpacity=0.8,
            children=[create_popup(mogi_source_geojson['features'][0]), create_tooltip("Mogi Deformation Source ")]
        )

        sill_rectangle_style = {'color': 'green', 'weight': 5, 'opacity': 0.75}

        # Create GeoJSON layer for the Sill rectangle with custom style and tooltip
        sill_rectangle_layer = dl.GeoJSON(
            data=sill_rectangle_geojson, 
            style=sill_rectangle_style, 
            children=[create_popup(sill_rectangle_geojson['features'][0]), create_tooltip("Sill Deformation Source ")], 
            id='sill-rectangle'
        )
        mogi_source_overlay = dl.Overlay(mogi_source_marker, name="Mogi Source", checked=True)
        sill_rectangle_overlay = dl.Overlay(sill_rectangle_layer, name="Sill Rectangle", checked=True)

    # Add other layers and controls
    map_children.extend([
        # Models overlayes
        mogi_source_overlay,
        sill_rectangle_overlay,

        # Lava fields
        dl.Overlay(lava_dec, name="Hraun/Lavafield við Sundhnúksgíga (19-21 des. 2023), LMÍ, NÍ, JHÍ", checked=True),
        dl.Overlay(lava_jan, name="Hraun/Lavafield við Hagafell 14. jan. 2024 kl. 16:15, LMÍ, NÍ, JHÍ", checked=True),
        dl.Overlay(lava_feb,name="Hraun/Lavafield við Sundhnúksgíga (8. feb 2024), LMÍ, NÍ, JHÍ", checked=True),
        dl.Overlay(lava_mars,name="Hraun/Lavafield við Sundhnúksgíga (17. mars 2024), LMÍ, NÍ, JHÍ", checked=True),

        dl.Overlay(dl.GeoJSON(data=geojson_data4, style=get_style(colors[5])), name="Hraun/Lavafield við Geldingadalir, LMÍ, NÍ, JHÍ, 2021", checked=True),
        dl.Overlay(dl.GeoJSON(data=geojson_data5, style=get_style(colors[5])), name="Hraun/Lavafield við Meradalir, LMÍ, NÍ, JHÍ, 2022", checked=True),
        dl.Overlay(dl.GeoJSON(data=geojson_data6, style=get_style(colors[5])), name="Hraun/Lavafield við Litli Hrútur, LMÍ, NÍ, JHÍ, 2023", checked=True),

        # Geothermal wells
        dl.Overlay(jardhitaborholur, name="Jarðhítaborholur/Geothermal Wells, Orkustofnun", checked=False),

        # Örnefni
        dl.Overlay(ornefni, name= "Örnefni", checked=True),

        # Fractures and craters
        dl.Overlay(dl.GeoJSON(data=geojson_data, style=get_style(colors[0])), name="Sprungusvæði/Fracture zones, Sæmundsson 2012-2022", checked=False),
        dl.Overlay(dl.GeoJSON(data=brotalina, style=style_brotalina), name="Misgengi/Faults, Náttúrufræðistofnun Íslands (NÍ) 2019", checked=False),
        dl.Overlay(dl.GeoJSON(data=gossprungar, style=style_gossprungar), name="Gossprungur á Íslandi, NÍ 2019", checked=True),
        dl.Overlay(dl.LayerGroup(children=gigar_markers), name="Gígar/Craters, NÍ 2019 ", checked=True),
        dl.Overlay(dl.GeoJSON(data=geojson_data1, style=get_style(colors[1])), name="Virkar jarðskjálftasprungur á Suðurlandi, NÍ 2019", checked=False),
        dl.Overlay(dl.GeoJSON(data=geojson_data2, style=get_style(colors[2])), name="INSAR Misgengi/Faults (Veðurstofa Íslands, 2024)", checked=False),
        dl.Overlay(dl.GeoJSON(data=geojson_data3, style=get_style(colors[3])), name="ISOR Sprungur/Fractures (Jarðfræðikort af Suðvesturlandi, 1, 100., 2012-2022)", checked=False),
        dl.ScaleControl(position="bottomleft"),
        *station_markers,  # Unpacking the list of station markers
    ])
    
    # Create the map component with LayersControl wrapping the layers
    map_component = dl.Map(children=[
        dl.LayersControl(children=map_children, position='topright')
    ], style={'width': '100%', 'height': '100vh'}, center=[center_lat, center_lon], zoom=zoom_level, id='leaflet-map')

    return map_component


