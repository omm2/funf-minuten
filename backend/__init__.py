from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from backend.config import Config

import strawberry
from strawberry.flask.views import GraphQLView

db = SQLAlchemy()


def create_app(config_obj=Config):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    db.init_app(app)
    migrate = Migrate(db=db, app=app)

    CORS(app, supports_credentials=True)

    from backend.api.query import Query

    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view(
            "graphql_view", schema=strawberry.Schema(query=Query)
        ),
    )

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return "test hello world"

    # from backend.models import Rotation, Status, Card

    # @app.route("/addcard")
    # def addcard():
    #     card = Card(
    #         name="Arschtritt",
    #         hint="directional movement with the foot towards an ass of sb else",
    #         status=Status.NEW,
    #         counter=0,
    #         rotation=Rotation.DAILY,
    #     )
    #     db.session.add(card)
    #     db.session.commit()

    #     return "card added"

    return app


# # from app import app
# from backend import create_app


# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=False)
