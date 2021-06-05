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
def all():
    return render_template("/all_stocks.html")

@app.route("/top10stocks.html")
def top():
    return render_template("/top10stocks.html")

@app.route("/winning.html")
def winning():
    return render_template("/winning.html")

@app.route("/losing.html")
def losing():
    return render_template("/losing.html")


#Debug
if __name__ == '__main__':
    app.run(debug=True)