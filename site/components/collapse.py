import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_leaflet as dl


# Define the button to show/hide images
collapse_button = dbc.Button(
    "Show Stations Images",
    id="collapse-button",
    className="mb-3",
    color="primary",
    n_clicks=0,
)

# Placeholder for the collapse content; content will be generated dynamically
collapse_content = dbc.Collapse(
    dbc.Row(
        id='images-grid',
    ),
    id="collapse",
    is_open=False,
)

