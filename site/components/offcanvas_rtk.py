# rtk baseline offcanvas

import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State
import requests
from bs4 import BeautifulSoup
import re

# Assuming these components are defined elsewhere in your project
from components.focused_maps import stations, url_to_area_mapping
from components.regions import regions

# Existing baseline_ids for other tabs
baseline_ids = ["SENG-SUDV", "ORFC-ELDC", "SENG-NAMC", "SENG-SUDV"]

from itertools import groupby

def fetch_file_baseline_ids(directory_url):
    file_baseline_ids = []
    try:
        response = requests.get(directory_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            file_links = soup.find_all('a')
            for link in file_links:
                href = link.get('href')
                match = re.match(r'([A-Z]+-[A-Z]+)-distance\.neu', href)
                if match:
                    file_baseline_ids.append(match.group(1))
    except requests.ConnectionError:
        print("Failed to fetch file baseline IDs")
    return file_baseline_ids

#def generate_rtk_data_content():
#    content = []
#    data_base_url = "https://cdn.vedur.is/gps/timeseries/data/rtk/rt_short/"
#    file_baseline_ids = fetch_file_baseline_ids(data_base_url)
#    for baseline_id in file_baseline_ids:
#        file_url = f"{data_base_url}{baseline_id}-distance.neu"
#        link_text = f"Download {baseline_id} Data"
#        link_element = html.A(link_text, href=file_url, target="_blank", style={'display': 'block', 'marginBottom': '5px'})
#        content.append(dbc.Col(link_element, width=12))
#    return content

def generate_rtk_data_content():
    content = []
    data_base_url = "https://cdn.vedur.is/gps/timeseries/data/rtk/rt_short/"
    file_baseline_ids = fetch_file_baseline_ids(data_base_url)
    
    # Sort the file_baseline_ids based on the last station name
    sorted_baseline_ids = sorted(file_baseline_ids, key=lambda x: x.split('-')[-1])
    
    # Group the sorted_baseline_ids by the last station name
    for key, group in groupby(sorted_baseline_ids, key=lambda x: x.split('-')[-1]):
        station_group_title = html.H4(f"{key} Baselines", style={'marginTop': '20px', 'marginBottom': '10px'})
        content.append(dbc.Col(station_group_title, width=12))
        
        for baseline_id in group:
            file_url = f"{data_base_url}{baseline_id}-distance.neu"
            link_text = f"Hlaða niður {baseline_id} gögnum"
            link_element = html.A(link_text, href=file_url, target="_blank", style={'display': 'block', 'marginBottom': '5px'})
            content.append(dbc.Col(link_element, width=12))
    
    return content

# Function that generates 
def generate_rtk_tab_content(time_period, area):
    content = []  # Use a list to hold both titles and images
    base_url = f"https://cdn.vedur.is/gps/locations/volcanos/reykjanes/graphs/rtk/baseline_plots/"
    
    time_period_suffix = {
        "6h": "_6h.png",
        "12h": "_12h.png",
        "2d": "_twodays.png",
    }
    
    if time_period == "rtk_data":
        # Special handling for "Gagnaskrár" tab
        content = generate_rtk_data_content()
    else:
        suffix = time_period_suffix.get(time_period, "")
        if not suffix:
            return "Invalid time period selected"
        
        for baseline_id in baseline_ids:
            image_url = f"{base_url}rtk_{baseline_id}{suffix}"
            try:
                response = requests.head(image_url)
                if response.status_code == 200:
                    title_element = html.H3(baseline_id, style={'textAlign': 'center', 'marginBottom': '0px'})
                    image_element = html.Img(src=image_url, style={'maxWidth': '100%', 'height': 'auto', 'marginTop': '0px'})
                    content.append(dbc.Col([title_element, image_element], width=6, md=6))
            except requests.ConnectionError:
                print(f"Failed to load image {image_url}")

    return dbc.Row(content, className="g-4") if content else "No images available"

rtk_tabs = dbc.Tabs([
    dbc.Tab(label="6 tímar", tab_id="6h"),
    dbc.Tab(label="12 tímar", tab_id="12h"),
    dbc.Tab(label="2 dagar", tab_id="2d"),
    dbc.Tab(label="Gagnaskrár", tab_id="rtk_data"),
], id="rtk-time-period-tabs")

rtk_offcanvas = dbc.Offcanvas(
    [
        rtk_tabs, 
        dcc.Loading(
            id="rtk_loading-content", 
            type="default", 
            children=html.Div(id="rtk-tab-content", style={'marginTop': '20px'}), 
            className="dash-loading-container"
        ),
    ],
    id="rtk_offcanvas",
    title="RTK Tímaraðir",
    is_open=False,
    className="custom-offcanvas-width",
)

@callback(
    Output("rtk-tab-content", "children"),
    [Input("rtk-time-period-tabs", "active_tab"),
     Input("url", "pathname")]
)
def update_rtk_tab_content(active_tab, pathname):
    area = pathname.strip('/').split('/')[-1]
    mapped_area = url_to_area_mapping.get(area, 'default')

    if active_tab == "rtk_data":
        return generate_rtk_data_content()
    else:
        return generate_rtk_tab_content(active_tab, mapped_area)

