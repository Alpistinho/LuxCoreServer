import json
from collections import OrderedDict
from pathlib import Path

from jsonschema import Draft7Validator, RefResolver
from flask_restplus import fields


from ...server.instance import server

api = server.api

basepath = Path(__file__).parent

filepath = str((basepath / "schemas/config_model_schema.json").resolve())
with open(filepath,'r') as f:
    schema = f.read()
    
config_post_schema = json.loads(schema, object_pairs_hook=OrderedDict)

config_schema_resolver = RefResolver(base_uri='file://{}'.format(filepath), referrer=config_post_schema)

print('Resolver: ', config_schema_resolver.base_uri)

Draft7Validator.check_schema(config_post_schema)
config_schema_validator = Draft7Validator(config_post_schema, resolver=config_schema_resolver)
