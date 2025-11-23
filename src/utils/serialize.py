from dataclasses import is_dataclass, asdict
from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel


def serialize(obj):
    if obj is None:
        return None

    if is_dataclass(obj):
        return {k: serialize(v) for k, v in asdict(obj).items()}

    if isinstance(obj, BaseModel):
        return obj.model_dump()

    if isinstance(obj, Enum):
        return obj.value

    return obj
