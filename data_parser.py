import csv
import json
import datetime
from dateutil.parser import parse
import os

FILEPATH = os.path.join(os.getcwd(), "data.csv")
OUTPUTPATH = os.path.join(os.getcwd(), "output")

def get_static_values(json_obj):
    json_obj["title"] = "Floor Access Event"
    json_obj["type"] = "object"
    # json_obj = get_properties(json_obj, row)
    json_obj["required"] = ["person_id", "datetime", "floor_level", "building"]
    return json_obj

def get_properties(row):
    row_obj = {}
    row_obj["person_id"] = row['Person Id']
    row_obj["datetime"] = get_date_from_string(row['Floor Access DateTime'])
    row_obj["floor_level"] = int(row['Floor Level'])
    row_obj["building"] = row['Building']
    return row_obj

def get_date_from_string(date):
    date_parsed = parse(date)
    date_converted = date_parsed.strftime("%Y-%M-%d %H:%M:%S")
    return date_converted


def save_as_json(csvfile, fieldnames):
    reader = csv.DictReader(csvfile, fieldnames)
    json_obj = {}
    json_obj = get_static_values(json_obj)
    json_obj["properties"] = []
    for row in reader:
        if reader.line_num != 1:
            json_obj["properties"].append(get_properties(row))
    fillename = "output.json"
    with open(os.path.join(OUTPUTPATH, fillename), 'w') as f:
        json.dump(json_obj, f, ensure_ascii=False, indent=4)

def main():
    csvfile = open(FILEPATH)
    fieldnames = ("Person Id","Floor Access DateTime","Floor Level","Building")
    save_as_json(csvfile, fieldnames)

if __name__ == "__main__":
    main()
