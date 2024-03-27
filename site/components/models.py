mogi_source_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "popupContent": """
                <div>
                    <h4>Inflation</h4>
                    <img src='https://cdn.vedur.is/gps/locations/volcanos/reykjanes/models/svartsengi/graph_inflation_mogi_is.png' style='width:100%;'>
                    <h4>Flowrate</h4>
                    <img src='https://cdn.vedur.is/gps/locations/volcanos/reykjanes/models/svartsengi/graph_flowrate_mogi_is.png' style='width:100%;'>
                </div>
                """
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-22.46093, 63.86163]
            }
        }
    ]
}

sill_rectangle_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "popupContent": """
                <div class='tabs'>
                    <input type='radio' id='tab3' name='tab-control' checked>
                    <input type='radio' id='tab4' name='tab-control'>
                    <ul>
                        <li title='Inflation'><label for='tab3' role='button'><span>Inflation</span></label></li>
                        <li title='Flowrate'><label for='tab4' role='button'><span>Flowrate</span></label></li>
                    </ul>
                    <div class='content'>
                        <section>
                            <img src='https://cdn.vedur.is/gps/locations/volcanos/reykjanes/models/svartsengi/graph_inflation_sill_is.png' style='width:100%;'>
                        </section>
                        <section>
                            <img src='https://cdn.vedur.is/gps/locations/volcanos/reykjanes/models/svartsengi/graph_flowrate_sill_is.png' style='width:100%;'>
                        </section>
                    </div>
                </div>
                """
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-22.49633, 63.85848],
                    [-22.41633, 63.88618],
                    [-22.40378, 63.87912],
                    [-22.48377, 63.85143],
                    [-22.49633, 63.85848]
                ]]
            }
        }
    ]
}

sill_rectangle_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "popupContent": """
                <div>
                    <h4>Inflation</h4>
                    <img src='https://cdn.vedur.is/gps/locations/volcanos/reykjanes/models/svartsengi/graph_inflation_sill_is.png' style='width:100%;'>
                    <h4>Flowrate</h4>
                    <img src='https://cdn.vedur.is/gps/locations/volcanos/reykjanes/models/svartsengi/graph_flowrate_sill_is.png' style='width:100%;'>
                </div>
                """
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-22.49633, 63.85848],
                    [-22.41633, 63.88618],
                    [-22.40378, 63.87912],
                    [-22.48377, 63.85143],
                    [-22.49633, 63.85848]
                ]]
            }
        }
    ]
}

