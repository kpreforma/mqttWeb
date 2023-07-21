from flask import Flask, render_template
from dotenv import load_dotenv
import pymongo
import os
import pandas as pd
import json
import plotly
import plotly.express as px

# initialize Flask app
app = Flask(__name__)

# env variables
mongo_conn_str = (
    "mongodb+srv://kennethr:jldWyszwZi8bRtsN@data-main.ubaxa5i.mongodb.net/data_main"
)

# initialize mongo client
mongo_client = pymongo.MongoClient(mongo_conn_str).get_database("mqtt").RawSignals
mongo_cursor = mongo_client.find()
signals = list(mongo_cursor)
pd_signals = pd.DataFrame(signals)


# Create graphJSON
fig = px.line(pd_signals, x='datetime', y='status')
graph_js = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


# routes
@app.get("/")
def get_table():
    return render_template("table.html", signals=signals)


@app.get("/dashboard")
def get_dash():
    return render_template("dashboard.html", graph=graph_js)


# start
if __name__ == "__main__":
    app.run(port=8080, debug=True)
