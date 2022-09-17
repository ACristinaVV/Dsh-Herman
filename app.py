from dash import dash, html, dcc
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components

from visualizations import chart

# App initialization
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Layout parameters
app.layout =  html.Div([
    html.Br(),

    # Heading
    dbc.Container(children=[
        dbc.Row([
            dbc.Col(html.H1(children=["Parametrización macroeconómica"], style={'font-family': 'Arial', 'color': '#D6D4C9'}), width=8, align='left'),
            dbc.Col(html.Img(src='https://ilab.net/wp-content/uploads/2020/07/citibanamex.png', width='244.8', height='82'))
        ], justify='left')
        ]),

    # First row level. Param button
    dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Dropdown(id='crisis-choose',
                             options=['Crisis financiera de 1994',
                              'Crisis financiera de 2008',
                              'Crisis financiera por COVID-19'])
                ])
            ]),
        ], width=3),
        ],className='mb-2'),

    # Second row level
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='inflation-chart', figure={}),
                ])
            ]),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='unemploy-chart', figure={}),
                ])
            ]),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=2)
    ],className='mb-2 mt-4'),

    # Third row level
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='usdmxn-chart', figure={}),
                ])
            ]),
        ], width=8),
    ],className='mb-2'),

    # Fourth level
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='short-chart', figure={}),
                    ])
                ]),
            ], width=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='long-chart', figure={}),
                    ])
                ]),
            ], width=4),
        ], className='mb-2'),

    # Fifth row level
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='pib-chart', figure={}),
                ])
            ]),
        ], width=10),
    ], className='mb-2'),

], fluid=True)

    ])

if __name__=='__main__':
    app.run_server(debug=False, port=8001)