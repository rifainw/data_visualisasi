import dash
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

import connection

from pages.visualisasi_data import pendidikan, kesehatan, pupr, perumahan, sosial, naker, lingkungan, capil

# HEADER
def Header(name, app):
    title = html.H2(name, style={"margin-top": 7,"color":"navy","font-weight":"bold"})
    logo = html.Img(src=app.get_asset_url("logo_satudatabantul.png"), style={"float": "right", "height": 90})
    logo2 = html.Img(src=app.get_asset_url("logo_sdi.png"), style={"float": "right", "height": 70})
    return dbc.Row([dbc.Col(title, md=10), dbc.Col(logo, md=1), dbc.Col(logo2, md=1)])

# Start the app
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.MORPH],
                suppress_callback_exceptions=True,
                routes_pathname_prefix='/visualisasi_data/',
                requests_pathname_prefix='/visualisasi_data/')
app.title = 'Satu Data Bantul'
app._favicon = 'favicon.ico'
server = app.server

card_content1 = [
    dbc.CardBody([html.P(DashIconify(icon="la:user-graduate",width=55,color="navy"),style={"textAlign": "center"}),dbc.Button("Pendidikan",color="primary",className="mt-auto",href='/visualisasi_data/pendidikan',style={'color':'navy'})],style={"textAlign": "center"})
]
card_content2 = [
    dbc.CardBody([html.P(DashIconify(icon="la:briefcase-medical",width=55,color="navy"),style={"textAlign": "center"}),dbc.Button("Kesehatan",color="primary",className="mt-auto",href='/visualisasi_data/kesehatan',style={'color':'navy'})],style={"textAlign": "center"})
]
card_content3 = [
    dbc.CardBody([html.P(DashIconify(icon="fluent:people-team-28-regular",width=55,color="navy"),style={"textAlign": "center"}),dbc.Button("Sosial",color="primary",className="mt-auto",href='/visualisasi_data/sosial',style={'color':'navy'})],style={"textAlign": "center"})
]
card_content4 = [
    dbc.CardBody([html.P(DashIconify(icon="healthicons:young-people-outline",width=55,color="navy"),style={"textAlign": "center"}),dbc.Button("Kependudukan",color="primary",className="mt-auto",href='/visualisasi_data/capil',style={'color':'navy'})],style={"textAlign": "center"})
]
card_content5 = [
    dbc.CardBody([html.P(DashIconify(icon="entypo:tree",width=55,color="navy"),style={"textAlign": "center"}),dbc.Button("Lingkungan Hidup",color="primary",className="mt-auto",href='/visualisasi_data/lingkungan',style={'color':'navy'})],style={"textAlign": "center"})
]
card_content6 = [
    dbc.CardBody([html.P(DashIconify(icon="healthicons:city-worker-outline",width=55,color="navy"),style={"textAlign": "center"}),dbc.Button("Tenaga Kerja",color="primary",className="mt-auto",href='/visualisasi_data/naker',style={'color':'navy'})],style={"textAlign": "center"})
]
card_content7 = [
    dbc.CardBody([html.P(DashIconify(icon="bi:house-door",width=55,color="navy"),style={"textAlign": "center"}),dbc.Button("Perumahan",color="primary",className="mt-auto",href='/visualisasi_data/perumahan',style={'color':'navy'})],style={"textAlign": "center"})
]
card_content8 = [
    dbc.CardBody([html.P(DashIconify(icon="bx:building-house",width=55,color="navy"),style={"textAlign": "center"}),dbc.Button("Tata Ruang",color="primary",className="mt-auto",href='/visualisasi_data/pupr',style={'color':'navy'})],style={"textAlign": "center"})
]

cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content1, color="#A7D7C5", inverse=True)),
                dbc.Col(dbc.Card(card_content2, color="#74B49B", inverse=True)),
                dbc.Col(dbc.Card(card_content3, color="#A7D7C5", inverse=True)),
                dbc.Col(dbc.Card(card_content4, color="#74B49B", inverse=True))
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content5, color="#74B49B", inverse=True)),
                dbc.Col(dbc.Card(card_content6, color="#A7D7C5", inverse=True)),
                dbc.Col(dbc.Card(card_content7, color="#74B49B", inverse=True)),
                dbc.Col(dbc.Card(card_content8, color="#A7D7C5", inverse=True))
            ],
            className="mb-4",
        )
    ]
)

app.layout = dbc.Container([
    Header("DATA VISUALISATION", app),
    html.Hr(),
    html.Div([dcc.Location(id="url", refresh=False),html.Div(id="page-content")])
],fluid=False)

@callback(Output('page-content','children'),
         [Input('url','pathname')])
def display_page(pathname):
    if pathname == '/visualisasi_data/pendidikan':
        return pendidikan.layout
    elif pathname == '/visualisasi_data/kesehatan':
        return kesehatan.layout
    elif pathname == '/visualisasi_data/pupr':
        return pupr.layout
    elif pathname == '/visualisasi_data/perumahan':
        return perumahan.layout
    elif pathname == '/visualisasi_data/sosial':
        return sosial.layout
    elif pathname == '/visualisasi_data/lingkungan':
        return lingkungan.layout
    elif pathname == '/visualisasi_data/naker':
        return naker.layout
    elif pathname == '/visualisasi_data/capil':
        return capil.layout    
    else:
        return cards

if __name__ == "__main__":
    app.run_server(host='0.0.0.0',debug=True)