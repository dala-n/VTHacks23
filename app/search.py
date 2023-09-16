import csv

def search_demographics(zipcode):
    data = None
    with open("app/data/demographic_data.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["zcta10"] == zipcode:
                data = {
                    "ZIP Code": row["zcta10"],
                    "Total Population (13-17)": row["totpop13_17"],
                    "White": float(row["pnhwhite13_17"]),
                    "Black": float(row["pnhblack13_17"]),
                    "Hispanic": float(row["phispanic13_17"]),
                    "Foreign": float(row["pfborn13_17"]),
                    
                    # Add other demographic data here
                }
                break  # Stop searching after finding a matching ZIP code
    return data
