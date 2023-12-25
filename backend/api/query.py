import strawberry
from backend.api.schema import Status, Rotation, Card_schema
from backend.models import Card
from typing import List as TypingList


@strawberry.type
class Query:
    def cards(self) -> Card_schema:
        return Card.query.all()

    cards: TypingList[Card_schema] = strawberry.field(resolver=cards)
