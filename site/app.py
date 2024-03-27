import dash
from dash import Output, html
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, '/assets/dark.css'], use_pages=True,
                suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}],
                title='GNSS VÍ',  # Custom title
                update_title='Síða hleður'  # Custom loading message here
                )


from pages import GNSS, notkunarskilmalar

# expose the flask variable in the file
server = app.server

# Layout
app.layout = html.Div(
        [
            #main app framework
            html.Div( style = {'fontSize':50,
                                                'textAlign':'center'}),

            #content of each page
            dash.page_container
            ], 
)

if __name__ == "__main__":
    app.run(debug=True, host ='0.0.0.0')



