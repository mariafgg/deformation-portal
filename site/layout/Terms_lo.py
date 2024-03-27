
from dash import html, dcc
import dash_bootstrap_components as dbc
from components.navbar import navbar2
#from components.maps import leafletmap
from components.terms import text

# Page layout
layout = dbc.Container(
    [
        dbc.Row(navbar2),
        dbc.Row([
            dbc.Col([
                text
            ], width=12),  
        ]),
    ],
    fluid=True,
    className='fluid'
)


