#!/usr/bin/python3
import dash
dash.register_page(__name__, path='/svinafellsheidi')

import dash
from dash import html
import dash_leaflet as dl
from components.focused_maps import create_focused_map
from components.regions import regions  # Ensure to import the regions dictionary correctly
from components.navbar import navbar

# Assuming the 'regions' dictionary is structured as {'RegionName': [min_lat, max_lat, min_lon, max_lon]}
region_name = 'Svinafellsheidi'  # Use the appropriate region name
region_data = regions[region_name]
center_lat = (region_data[2] + region_data[3]) / 2
center_lon = (region_data[0] + region_data[1]) / 2
zoom_level = 11  # Determine an appropriate zoom level based on the region
area = 'svinafellsheidi'

# Generate the map focused on the region
region_map = create_focused_map(center_lat, center_lon, zoom_level, area)

layout = html.Div([
    navbar,
    region_map
    ])

