from flask import Flask, render_template, request
from search import search_demographics  # Import the search function
import csv

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        zipcode = request.form["zipcode"]
        # Call the search_demographics function to retrieve data based on the ZIP code.
        # Store the data in a variable.
        data = search_demographics(zipcode)
        return render_template("index.html", data=data)
    return render_template("index.html", data=None)

@app.route("/map", methods=["GET", "POST"])
def map():
    return render_template("map.html")

@app.route("/tests")
def tests():
    return render_template("tests.html")

@app.route("/about-us")
def aboutus():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)