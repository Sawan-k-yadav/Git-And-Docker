from flask import Flask
import numpy as np
import pandas as pd


app  = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    return "<h1>This is home Page</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)