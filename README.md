# Parsdantic

Parsdantic is a powerful Python package that automatically generates Pydantic models from JSON schemas. It simplifies the process of data validation and serialization by bridging the gap between JSON Schema and Pydantic.
Features

## Features

- Convert JSON schemas to Pydantic models with a single function call
- Support for nested objects and complex data structures
- Automatic type inference and validation

## Installation

You can install Parsdantic using pip:

```bash
pip install parsdantic
```

## Quick Start
Here's a simple example of how to use Parsdantic:

```python
from parsdantic.parser import parse

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

Person = parse(schema)

person = Person(
    name="John",
    age=30,
    hair={"color": {"r": 255, "g": 0, "b": 0}},
)

print(person) # Person(name='John', age=30, hair=Hair(color=Color(r=255, g=0, b=0)))
```
_Note : Collections (e.g. List, Dict) and Enum are still not available._

## Support
You can open an issue on the [GitHub issue tracker](https://github.com/SergiFuster/parsdantic/issues).


## LICENSE
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.