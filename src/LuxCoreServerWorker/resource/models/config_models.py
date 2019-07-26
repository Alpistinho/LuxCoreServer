from pathlib import Path
import csv
import json
from collections import OrderedDict

from flask_restplus import fields

from ...server.instance import server

api = server.api
api.models
config_post_model = api.model('Render configuration model',
 {'renderengine.type': fields.String,
 'int': fields.Integer,
 'listInts': fields.List(fields.Integer)})

address = api.schema_model('Address', {
    'properties': {
        'road': {
            'type': 'string'
        },
    },
    'type': 'object'
})

basepath = Path(__file__).parent
filepath = (basepath / "config_models_schema.json").resolve()

with open(str(filepath),'r') as f:
    schema = f.read()
schema_json = json.loads(schema, object_pairs_hook=OrderedDict)
config_post_model = address = api.schema_model('Config files', schema_json)

