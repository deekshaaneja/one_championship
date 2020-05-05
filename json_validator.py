import jsonschema
import json
import os
import logging

input_schema_file = os.path.join(os.getcwd(), "input", "schema.json")

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

with open(input_schema_file) as f:
    schema = json.load(f)

def validate_schema(input_json):
    try:
        jsonschema.validate(input_json, schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        logger.info("well-formed but invalid JSON:" + str(e))
    except json.decoder.JSONDecodeError as e:
        logger.info("poorly-formed text, not JSON:" +  str(e))