import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State
from components.focused_maps import stations, url_to_area_mapping
from components.regions import regions
import requests


def generate_tab_content(time_period, area):
    images = []
    
    # Extract Reykjanesskagi region boundaries from the 'regions' dictionary
    reykjanesskagi_boundaries = regions['Reykjanesskagi']
    min_lon, max_lon, min_lat, max_lat = reykjanesskagi_boundaries[:4]
    
    # Filter stations based on the Reykjanesskagi region boundaries
    filtered_stations = [station for station in stations if min_lon <= station['longitude'] <= max_lon and min_lat <= station['latitude'] <= max_lat]
    
    for station in filtered_stations:
        image_url = None

        # Construct the image URL based on the time period
        if time_period == "90d":
            image_url = f"https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/24h/{station['name']}-plate-90d.png"
        elif time_period == "year":
            image_url = f"https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/24h/{station['name']}-plate-year.png"
        elif time_period == "síðan January 1st, 2020":
            image_url = f"https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/24h/{station['name']}-plate_since-20200101.png"
        elif time_period == "síðan November 12th, 2023":
            image_url = f"https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/24h/{station['name']}-plate_since-20231112.png"

        if image_url:
            try:
                response = requests.head(image_url)
                if response.ok:
                    image_element = html.Img(src=image_url, style={'maxWidth': '100%', 'height': 'auto'})
                    images.append(dbc.Col(image_element, width=6, md=6))
            except requests.exceptions.RequestException as e:
                print(f"Failed to load image {image_url}: {e}")

    return dbc.Row(images, className="g-4")


tabs = dbc.Tabs([
    dbc.Tab(label="90 dagar", tab_id="90d"),
    dbc.Tab(label="1 ár", tab_id="year"),
    dbc.Tab(label="Síðan Jan 1, 2020", tab_id="since_1"),
    dbc.Tab(label="Síðan Nóv 12, 2023", tab_id="since_2"),
], id="time-period-tabs")

offcanvas = dbc.Offcanvas(
    [
        tabs, 
        dcc.Loading(
            id="loading-content", 
            type="default", 
            children=html.Div(id="tab-content", style={'marginTop': '20px'}), 
            className="dash-loading-container"
            )
        ],
    id="offcanvas",
    title="GNSS Tímaraðir",
    is_open=False,
    className="custom-offcanvas-width",
)

@callback(
    Output("tab-content", "children"),
    [Input("time-period-tabs", "active_tab"),
     Input("url", "pathname")]
)
def update_tab_content(active_tab, pathname):
    area = pathname.strip('/').split('/')[-1]
    mapped_area = url_to_area_mapping.get(area, 'default')

    if active_tab == "90d":
        return generate_tab_content("90d", mapped_area)
    elif active_tab == "year":
        return generate_tab_content("year", mapped_area)
    elif active_tab == "since_1":
        return generate_tab_content("síðan January 1st, 2020", mapped_area)
    elif active_tab == "since_2":
        return generate_tab_content("síðan November 12th, 2023", mapped_area)

