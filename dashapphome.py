import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {"background": "#AAAAAA", "text": "#000000"}


app.layout = html.Div(
    [
        html.H1(
            id="heading",
            children="Interactive Sine wave",
            style={"textAlign": "center"},
        ),
        dcc.Graph(id="graph-sine"),
        html.H3(id="label-amp", children="Amplitude"),
        dcc.Slider(
            id="amp-slider", min=0, max=10, value=5, step=0.5, updatemode="drag"
        ),
        html.H3(id="label-freq", children="Frequency"),
        dcc.Slider(
            id="freq-slider", min=1, max=10, value=5, step=0.5, updatemode="drag"
        ),
        html.H3(id="label-phase", children="Phase"),
        dcc.Slider(
            id="phase-slider",
            min=0,
            max=2 * np.pi,
            value=0,
            step=0.5,
            updatemode="drag",
        ),
        html.H3(id="label-offset", children="Offset"),
        dcc.Slider(
            id="offset-slider", min=-5, max=5, value=0, step=0.5, updatemode="drag"
        ),
    ],
)


@app.callback(
    Output("graph-sine", "figure"),
    [
        Input("amp-slider", "value"),
        Input("freq-slider", "value"),
        Input("phase-slider", "value"),
        Input("offset-slider", "value"),
    ],
)
def update_graph(amp, freq, phi, off):
    x = np.linspace(0, 5, 100)
    y = off + amp * np.sin(freq * x + phi)
    fig = px.line(x=x, y=y)
    fig.layout.yaxis.range = [-10, 10]
    fig.layout.xaxis.range = [0, 5]
    return fig


dashapp = app.server
if __name__ == "__main__":
    app.run_server(debug=True)
