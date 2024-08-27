from flask import Flask, render_template
import numpy as np
import pandas as pd


app  = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)