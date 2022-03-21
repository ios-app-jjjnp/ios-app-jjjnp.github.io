# helper to generate json files from csv data

# for reference, calls should ultimately look like these:
# https://api.weather.gov/points/{latitude},{longitude}
# https://api.weather.gov/points/39.7456,-97.0892

# forecast data from above:
# https://api.weather.gov/gridpoints/{office}/{grid X},{grid Y}/forecast

import csv
import json

CSV_FILENAME = "US.txt"

with open(CSV_FILENAME) as csv_file:
    zip_reader = csv.reader(csv_file, delimiter="\t")

    entry = {}
    
    for line in zip_reader:
        entry["place_name"] = line[2]
        entry["state_name"] = line[3]
        entry["state_abbrv"] = line[4]
        entry["lat"] = line[9]
        entry["long"] = line[10]
    
        with open("data/" + line[1] + ".json", "w") as json_out:
            json_out.write(json.dumps(entry))