# Library Imports
import json
from plotly import graph_objects as go
from plotly import utils
import plotly.express as px

# Create graphJSON

def create_graph(data):
    px_line = px.line(data, x='datetime', y='status')
    px_line_js = json.dumps(px_line, cls=utils.PlotlyJSONEncoder)

    return px_line_js


def create_table(data):
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(data.columns),
                fill_color='gray',
                align='center'),
    cells=dict(values=[data.datetime, data.device_code, data.status],
            fill_color='lightgray',
            align='left'))
    ])

    return fig