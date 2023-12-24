import os


class Config:
    # SECRET_KEY = os.environ["SECRET_KEY"]

    SECRET_KEY = '+?sSoPOLu?8vRCzoq`K|KKOYv4[br"V6[8?Jc|{xj?`l$}X&^KPC#W@82=2zi`9'
    basedir = os.path.abspath(os.path.dirname(__file__))
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "bluefriday.db")
    # SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://funfminuten:funfminuten@db4free.net:3306/funfminuten"
    )
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://baslsb:bfbaslsb2023@baslsb.mysql.pythonanywhere-services.com/baslsb$default"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = "None"
    # SESSION_COOKIE_HTTPONLY = True,
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # REMEMBER_COOKIE_HTTPONLY = True
