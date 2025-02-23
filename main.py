import json
from pprint import pp

from pydantic import BaseModel

from src.parsdantic.parser import parse

schema = {
    "$defs": {
        "Color": {
            "properties": {
                "r": {"title": "R", "type": "integer"},
                "g": {"title": "G", "type": "integer"},
                "b": {"title": "B", "type": "integer"},
            },
            "required": ["r", "g", "b"],
            "title": "Color",
            "type": "object",
        },
        "Hair": {
            "properties": {"color": {"$ref": "#/$defs/Color"}},
            "required": ["color"],
            "title": "Hair",
            "type": "object",
        },
    },
    "properties": {
        "name": {"title": "Name", "type": "string"},
        "age": {"title": "Age", "type": "integer"},
        "hair": {"$ref": "#/$defs/Hair"},
    },
    "required": ["name", "age", "hair"],
    "title": "Person",
    "type": "object",
}

pydantic_model = parse(schema)

data = {
    "name": "John",
    "age": 30,
    "hair": {"color": {"r": 255, "g": 0, "b": 0}},
}

person = pydantic_model.model_validate(data)

pp(person.model_json_schema())
pp(person.model_json_schema())
