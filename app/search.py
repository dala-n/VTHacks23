import csv

def search_demographics(zipcode):
    data = None
    with open("data/demographic_data.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["zcta10"] == zipcode:
                data = {
                    "ZIP Code": row["zcta10"],
                    "Total Population (08-12)": row["totpop08_12"],
                    "Total Population (13-17)": row["totpop13_17"],
                    "Population Density (08-12)": row["popden08_12"],
                    "Population Density (13-17)": row["popden13_17"],
                    # Add other demographic data here
                }
                break  # Stop searching after finding a matching ZIP code
    return data