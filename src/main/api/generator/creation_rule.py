from pydantic.dataclasses import dataclass


@dataclass
class CreationRule:
    regex: str