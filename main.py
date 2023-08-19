# library imports
from flask import Flask, render_template, request, send_file, make_response, Response
from dotenv import load_dotenv
import os
import io
import base64
import pandas as pd
import datetime

# initialize Flask app
app = Flask(__name__)

# user imports
from db_mongo import signals
import plotly_service as ps

# Routes
@app.get("/")
def get_table():
	return render_template("table.html", signals=signals)

@app.route("/dashboard", methods=["GET", "POST"])
def get_dashboard():
	dfsignals_display = dfsignals
	dfsignals_display['datetime'] = pd.to_datetime(dfsignals['datetime'], format='%Y-%m-%d %H:%M:%S.%f')
	if request.method == 'POST':
		start = request.form["dtpickerstart"]
		end = request.form["dtpickerend"]
		print(f"start: {start}, end: {end}")
		# dfsignals_display = dfsignals
		dfsignals_display = dfsignals_display[(dfsignals_display['datetime'] > start) & (dfsignals_display['datetime']< end)]
	
	graph = ps.create_graph(dfsignals_display)
	return render_template("dashboard.html", graph=graph)

@app.get("/dashboard/download")
def dl_dashboard():
	return Response(
       dfsignals.to_csv(),
       mimetype="text/csv",
       headers={"Content-disposition":
       "attachment; filename=filename.csv"})

# App Start
if __name__ == "__main__":
	dfsignals = pd.DataFrame(signals)
	table = ps.create_table(dfsignals)
	app.run(port=8080, debug=True)
