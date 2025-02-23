from typing import Any

import jsonref
from pydantic import BaseModel, create_model

from .types.types import Types


def pydantize(obj: dict[str, Any]) -> type[BaseModel]:
    """Convert JSON Schema to Pydantic model

    Args:
        obj (dict[str, Any]): Model JSON Schema

    Returns:
        type[BaseModel]: Resulting Pydantic model
    """
    def _pydantize(title: str, obj: dict[str, dict[str, dict]], res={}) -> type[BaseModel]:
        """Convert JSON Schema to Pydantic model

        Args:
            title (str): Pydantic class name
            obj (dict[str, dict[str, dict]]): Properties JSON Schema
            res (dict, optional): _description_. Defaults to {}.

        Returns:
            type[BaseModel]: _description_
        """
        for k, v in obj.items():
            if v.get("properties"):
                res = res | {title: (_pydantize(v["title"], v["properties"]), None)}
            else:
                res = res | {k: (Types[v["type"]], None)}

        return create_model(title, **res)
    
    obj = jsonref.replace_refs(obj)
    return _pydantize(obj["title"], obj["properties"])
