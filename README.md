# Icelandic Met Office (IMO) Deformation Portal

This application streams workflows from the Icelandic Meteorological office concerning surface measurements of volcano deformation and its modelling through deformation models in Iceland, currently more focused in the Reykjanes peninsula activity.
You can browse this from the Dash Examples in the Geospatial section https://plotly.com/examples/geospatial/ 

## Instructions for Local Development Installation

To get started, first clone this repo:
```
git clone git@github.com:mariafgg/deformation-portal.git
```
Go to the current development version directory
```
cd deformation-portal/site
```
Create Virtual Environment:

```bash
python3 -m venv env
```
Activate Virtual Environment:

```bash
source env/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```
Run the app:

```bash
python3 app.py
```
Open a browser at http://localhost:8050
 
