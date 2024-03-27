#!/usr/bin/python3
import dash
dash.register_page(__name__, path='/reykjanesskagi')

from dash import html, callback, Input, Output, State, dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl
from components.focused_maps import create_focused_map
from components.regions import regions
from components.navbar import navbar_pages
from components.offcanvas import offcanvas
from components.offcanvas_rtk import rtk_offcanvas

# Assuming the 'regions' dictionary is structured appropriately
region_name = 'Reykjanesskagi'
region_data = regions[region_name]
center_lat = 63.93
center_lon = -22.08
zoom_level = 11
area = 'reykjanes'

# Generate the map focused on the region
region_map = create_focused_map(center_lat, center_lon, zoom_level, area)

# Define Offcanvas Component directly in this file for simplicity
offcanvas_content = html.P("Your content here")
rtk_offcanvas_content = html.P("Your content here")

# Define a static trigger for the Offcanvas within the layout
trigger = dbc.Button("Open Offcanvas", id="open-offcanvas-link", n_clicks=0)
rtk_trigger = dbc.Button("Open RTK Offcanvas", id="open-rtk-offcanvas-link", n_clicks=0)

layout = html.Div([
    navbar_pages,
    region_map,
    dcc.Location(id='url', refresh=False),
    trigger,  # Include the trigger in the layout
    offcanvas,  # Include the offcanvas component
    rtk_trigger,  # Include the trigger in the layout
    rtk_offcanvas
])


# Adjust the callback to listen for clicks on the 'open-offcanvas-btn' and toggle 'offcanvas'
@callback(
    Output("offcanvas", "is_open"),  # Ensure this ID matches your offcanvas component's ID
    [Input("open-offcanvas-btn", "n_clicks")],  # Listen for clicks on the "Pane" link
    [State("offcanvas", "is_open")],  # Use the correct ID here as well
    prevent_initial_call=True
)
def toggle_offcanvas(n, is_open):
    if n:
        return not is_open
    return is_open

# Corrected callback for toggling the RTK offcanvas
@callback(
    Output("rtk_offcanvas", "is_open"),  # Match the ID of your RTK offcanvas component
    [Input("open-rtk-offcanvas-btn", "n_clicks")],  # Corrected to listen to the unique ID of the RTK trigger button
    [State("rtk_offcanvas", "is_open")],  # Ensure this matches the ID of the RTK offcanvas component
    prevent_initial_call=True
)
def toggle_rtk_offcanvas(n, is_open):
    if n:
        return not is_open
    return is_open

