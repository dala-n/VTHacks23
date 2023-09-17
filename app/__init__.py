import matplotlib
matplotlib.use('agg')  # Use the "agg" backend for non-interactive mode

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
        data_type = request.form["data-type"]  # Get the selected data type
        data = search_demographics(zipcode, data_type)  # Filter data based on data type

        if data:
            # Create a new figure and axis for the pie chart using Matplotlib
            fig, ax = plt.subplots()
            labels = list(data.keys()) 
            sizes = list(data.values())
            colors = ['red', 'blue', 'green', 'yellow']

            # Function to split long labels into multiple lines
            def split_labels(labels, max_line_length=20):
                split_labels = []
                for label in labels:
                    if len(label) > max_line_length:
                        words = label.split()  # Split the label into words
                        lines = []
                        current_line = ""
                        for word in words:
                            if len(current_line) + len(word) + 1 <= max_line_length:
                                current_line += " " + word if current_line else word
                            else:
                                lines.append(current_line)
                                current_line = word
                        if current_line:
                            lines.append(current_line)
                        split_labels.append('\n'.join(lines))
                    else:
                        split_labels.append(label)
                return split_labels

            # Split the labels
            split_labels = split_labels(labels)
            
            ax.pie(sizes, labels=split_labels, colors=colors, autopct='%1.1f%%', startangle=140)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

            # Adjust the left margin to shift the pie chart to the right
            # plt.subplots_adjust(left=0.2) 

            # Save the pie chart as an image file
            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png')
            img_buf.seek(0)
            img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')

            # Close the Matplotlib figure to free up resources
            plt.close(fig)

            # Close the image buffer
            img_buf.close()

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