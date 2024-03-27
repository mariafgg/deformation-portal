
from dash import html, dcc
import dash_bootstrap_components as dbc
from components.navbar import navbar
from components.maps import leafletmap

# Page layout
layout = dbc.Container(
    [
        dbc.Row(navbar),
        dbc.Row([
            dbc.Col([
                #html.Br(),
                leafletmap,
            ], width=12),  
        ]),
    ],
    fluid=True,
    className='fluid'
)


