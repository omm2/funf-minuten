from app import db
from enum import Enum


class Status(Enum):
    NEW = 1
    LEARNED = 2
    INPROGRESS = 3


class Rotation(Enum):
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    hint = db.Column(db.String(length=200), nullable=True)
    status = db.Column(db.String(length=30), nullable=True)
    rotation = db.Column(db.String(length=30), nullable=False)
    image = db.Column(db.Text, nullable=True)
    counter = db.Column(db.Integer, nullable=False)
