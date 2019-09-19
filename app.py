import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Rock Creek Park'
myheading1 = "An Oasis in the City"
myheading2 = "America's 3rd Designated National Park"
image1 = 'Rock_Creek_Park_NPS_sign.jpg'
image2 = 'rcp_map.jpg'
textbody = "Teddy Roosevelt explored the park - you should too!"
sourceurl = 'https://www.nps.gov/rocr/index.htm'
githublink = 'https://github.com/aidanjdm/dash-dc-layout'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.H2(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '50%', 'height': 'auto'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '80%', 'height': 'auto'}),
        ],className='three columns'),
        html.Div([
            html.Div(textbody, style={
                'padding': '4px',
                'font-size': '16px',
                'height': '100px',
                'border': 'thin green solid',
                'color': 'rgb(255, 255, 255)',
                'backgroundColor': 'rgb(57, 83, 107)',
                'textAlign': 'center',
                }),
        ],className='six columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
