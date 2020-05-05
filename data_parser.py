import csv
import json
import datetime
from dateutil.parser import parse
import os
from json_validator import validate_schema
import logging


FILEPATH = os.path.join(os.getcwd(), "input", "data.csv")
OUTPUTPATH = os.path.join(os.getcwd(), "output")

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

def get_static_values(json_obj):
    json_obj["title"] = "Floor Access Event"
    json_obj["type"] = "object"
    # json_obj = get_properties(json_obj, row)
    json_obj["required"] = ["person_id", "datetime", "floor_level", "building"]
    return json_obj

def get_properties(row):
    try:
        row_obj = {}
        row_obj["person_id"] = row['Person Id']
        row_obj["datetime"] = get_date_from_string(row['Floor Access DateTime'])
        row_obj["floor_level"] = int(row['Floor Level'])
        row_obj["building"] = row['Building']
        if validate_schema(row_obj):
            return row_obj
    except Exception as e:
        logger.info(str(e))

def get_date_from_string(date):
    try:
        date_parsed = parse(date)
        date_converted = date_parsed.strftime("%Y-%M-%d %H:%M:%S")
        return date_converted
    except Exception as e:
        logger.info(str(e))


def save_as_json(csvfile, fieldnames):
    try:
        reader = csv.DictReader(csvfile, fieldnames)
        # json_obj = {}
        # json_obj = get_static_values(json_obj)
        output = []
        for row in reader:
            if reader.line_num != 1:
                output.append(get_properties(row))
        filename = "output.json"
        with open(os.path.join(OUTPUTPATH, filename), 'w') as f:
            json.dump(output, f, ensure_ascii=False, indent=4)
    except Exception as e:
        logger.info(str(e))

def main():
    try:
        csvfile = open(FILEPATH)
        fieldnames = ("Person Id","Floor Access DateTime","Floor Level","Building")
        save_as_json(csvfile, fieldnames)
    except Exception as e:
        logger.info(str(e))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.info(str(e))
