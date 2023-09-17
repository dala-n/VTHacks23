import csv

def search_demographics(zipcode, data_type):
    data = None
    with open("app/data/demographic_data.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["zcta10"] == zipcode:
                data = {}

                if data_type == "ethnicity":
                    data.update({
                        "White": float(row["pnhwhite13_17"]),
                        "Black": float(row["pnhblack13_17"]),
                        "Hispanic": float(row["phispanic13_17"]),
                        "Foreign": float(row["pfborn13_17"])
                    })
                elif data_type == "income":
                    data.update({
                        "<15K": float(row["pin1b_13_17"]),
                        "15-30K": float(row["pin2b_13_17"]),
                        "30-50K": float(row["pin3b_13_17"]),
                        "50-100K": float(row["pin4b_13_17"]),
                        "100K+": float(row["pin5b_13_17"])
                    })
                elif data_type == "education":
                    data.update({
                        "Less than High School Diploma": float(row["ped1_13_17"]),
                        "High School Diploma and/or Some College": float(row["ped2_13_17"]),
                        "Bachelor's Degree or Higher": float(row["ped3_13_17"])
                    })
                elif data_type == "age":
                    data.update({
                        "<18": float(row["p18yr_13_17"]),
                        "18-29": float(row["p18_2913_17"]),
                        "30-39": float(row["p30_3913_17"]),
                        "40-49": float(row["p40_4913_17"]),
                        "50-69": float(row["p50_6913_17"]),
                        "70+": float(row["pge7013_17"]),
                    })

                break  # Stop searching after finding a matching ZIP code
    return data
