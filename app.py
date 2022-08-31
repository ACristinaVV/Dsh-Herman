from dash import Dash, html, dcc

from visualizations import chart

app = Dash(__name__)



fig = chart

app.layout = html.Div(children=[
    html.H1(children='Herman'),
    html.Div(children='''Dashboard'''),
    dcc.Graph(id='Daily Sales', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
