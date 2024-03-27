import dash_bootstrap_components as dbc
from dash import html
from components.regions import regions
# Import the regions dictionary
from components.regions import regions  

## Generate region page paths and labels
#def generate_region_paths_and_labels():
#    return [(region.replace(' ', '_').lower(), regions[region]['name_is']) for region in regions.keys()]
# Assuming the Icelandic name ('name_is') is the first element in each list
def generate_region_paths_and_labels():
#    return [(region.replace(' ', '_').lower(), regions[region][4]) for region in regions.keys()]
    return [('reykjanesskagi', regions['Reykjanesskagi'][4])]
    

# Main site navbar with Icelandic labels
navbar = html.Div([
    dbc.Navbar(
        dbc.Container([
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src='../assets/Logo.png', height="30px")),
                        dbc.Col(dbc.NavbarBrand("GNSS gátt", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",  # Adjusted from "mx-auto" for Bootstrap 5 spacing utilities
                ),
               # href="/",
            ),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem(label, href=f"/{path}") for path, label in generate_region_paths_and_labels()
                ],
                nav=True,
                in_navbar=True,
                label="Eldstöð",
            ),
            #dbc.NavItem(dbc.NavLink("Pane", href="#", id='open-offcanvas-btn')),
            dbc.NavItem(dbc.NavLink("Notkunarskilmálar", href="/notkunarskilmalar")),
        ]),
        dark=True,
        #color="primary",
        #expand="lg",
        #style={'background-color': '#004c80'},
        className="custom-navbar",
    ),
])

hidden_trigger = dbc.Button("Open Offcanvas", id="open-offcanvas-link", n_clicks=0, style={"display": "none"})
hidden_trigger_rtk = dbc.Button("Open RTK Offcanvas", id="open-offcanvas-link-rtk", n_clicks=0, style={"display": "none"})

#nav bar pages
navbar_pages = html.Div([
    dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(html.Img(src='../assets/Logo.png', height="30px"), width='auto'),
                        dbc.Col(dbc.NavbarBrand("GNSS gátt", className="ms-2"), width="auto"),                      ],
                    align="center",
                    className="g-0",
                ),
                # Group "Heimasíða" and "Svæði" inside a div with Bootstrap spacing classes for additional space
                html.Div(
                    [
                        dbc.NavLink("Heimasíða", href="/", className="nav-link me-4"),  # Add margin to the right of "Heimasíða"
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem(label, href=f"/{path}") for path, label in generate_region_paths_and_labels()
                            ],
                            nav=True,
                            in_navbar=True,
                            label="Eldstöð",
                            className="nav-link me-4"
                        ),
                    dbc.NavItem(dbc.NavLink("Gröf", id='open-offcanvas-btn', className="nav-link me-4")),
                    hidden_trigger,
                    dbc.NavItem(dbc.NavLink("RTK GNSS", id='open-rtk-offcanvas-btn', className="nav-link")),
                    hidden_trigger_rtk,

                    ],
                    className="d-flex justify-content-center flex-grow-1",  # Center the div containing the links
                ),
#                dbc.NavItem(dbc.NavLink("Pane", href="#", id='open-offcanvas-btn')),
                dbc.NavItem(dbc.NavLink("Notkunarskilmálar", href="/notkunarskilmalar")),
                           ],
            fluid=True,
        ),
        dark=True,
#        color="primary",
        className="custom-navbar",
#        expand="lg",
    ),
])


# Navigation bar with Terms of Use link
navbar2 = html.Div([
    dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src='../assets/Logo.png', height="30px")),
                            dbc.Col(dbc.NavbarBrand("GNSS gátt", className="ms-2")),
                        ],
                        align="center",
                        className="mx-auto",
                    ),
                    style={"textAlign": "end"},
                ),
                dbc.NavItem(dbc.NavLink("Heimasíða", href="/")),  # Terms of Use link
            ]
        ),
        className="custom-navbar",
        dark=True,
    ),
])
