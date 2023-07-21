from flask import Flask, render_template, request, url_for, redirect, session
from dotenv import load_dotenv
import pymongo
import os
import pandas as pd

# initialize Flask app
app = Flask(__name__)

# env variables
mongo_conn_str = (
    "mongodb+srv://kennethr:jldWyszwZi8bRtsN@data-main.ubaxa5i.mongodb.net/data_main"
)

# initialize mongo client
mongo_client = pymongo.MongoClient(mongo_conn_str).get_database("mqtt").RawSignals
data = mongo_client.find()
signals = list(data)


# routes
@app.get("/")
def get_table():
    return render_template("table.html", signals=signals)


@app.get("/dashboard")
def get_dash():
    return render_template("dashboard.html", signals=signals)


# start
if __name__ == "__main__":
    app.run(port=8080, debug=True)
