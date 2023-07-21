from flask import Flask, render_template, request, url_for, redirect, session
from dotenv import load_dotenv
import pymongo
import os

# initialize Flask app
app = Flask(__name__)

# env variables
mongo_conn_str = (
    "mongodb+srv://kennethr:jldWyszwZi8bRtsN@data-main.ubaxa5i.mongodb.net/data_main"
)

# initialize mongo client
mongo_client = pymongo.MongoClient(mongo_conn_str).get_database("mqtt").RawSignals


# routes
@app.get("/")
def index():
    return render_template("dashboard.html")


# start
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
