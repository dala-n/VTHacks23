from flask import Flask, render_template, request
from search import search_demographics  # Import the search function
import csv
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        zipcode = request.form["zipcode"]
        # Call the search_demographics function to retrieve percentage data based on the ZIP code.
        # Store the data in a variable.
        data = search_demographics(zipcode)

        # Create a pie chart using Matplotlib
        labels = ['White', 'Black', 'Hispanic', 'Foreign']
        sizes = [data["White"], data["Black"], data["Hispanic"], data["Foreign"]]
        colors = ['red', 'blue', 'green', 'yellow']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        
        # Save the pie chart as an image file
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img_buf.seek(0)
        img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')

        return render_template("index.html", data=data, img_base64=img_base64)
    
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