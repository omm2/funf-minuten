import strawberry
from enum import Enum
from typing import Optional


@strawberry.enum
class Status(Enum):
    NEW = 1
    LEARNED = 2
    INPROGRESS = 3


@strawberry.enum
class Rotation(Enum):
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3


@strawberry.type
class Card_schema:
    id: int
    name: str
    hint: Optional[str]
    status: Optional[Status]
    rotation: Rotation
    image: Optional[str]
    counter: int
