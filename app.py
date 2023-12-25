import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(db=db, app=app)

with app.app_context():
    db.create_all()

CORS(app, supports_credentials=True)


@app.route("/")
def home():
    return "test hello world"


from models import Rotation, Status, Card


@app.route("/addcard")
def addcard():
    card = Card(
        name="Arschtritt",
        hint="directional movement with the foot towards an ass of sb else",
        status=Status.NEW,
        counter=0,
        rotation=Rotation.DAILY,
    )
    db.session.add(card)
    db.session.commit()

    return "card added"


# # from app import app
# from backend import create_app


# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=False)
