from pandas import DataFrame
import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from flask import Flask, jsonify, render_template
from sklearn.linear_model import LinearRegression
from pathlib import Path

# Flask Setup
app = Flask(__name__)

##################################################################################################
# Flask Routes 
##################################################################################################
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/all_stocks.html")
def about():
    return render_template("/all_stocks.html")

@app.route("/top10stocks.html")
def map():
    return render_template("/top10stocks.html")

@app.route("/winning.html")
def teams():
    return render_template("/winning.html")

# @app.route("/batting_avg.html")
# def batting_avg():
#     return render_template("/batting_avg.html")

# @app.route("/earn_run_avg.html")
# def earn_run_avg():
#     return render_template("/earn_run_avg.html")c

# @app.route("/pie_charts.html")
# def pie_charts():
#     return render_template("/pie_charts.html")

#Debug
if __name__ == '__main__':
    app.run(debug=True)