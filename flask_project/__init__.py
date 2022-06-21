from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_project.config import Config
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():

    app = Flask(__name__)
    db.init_app(app)

    from flask_project.main.routes import main
    app.register_blueprint(main)

    app.config.from_object(Config)
    login_manager.init_app(app)
    bcrypt = Bcrypt()

    from flask_project.users.routes import users
    app.register_blueprint(users)

    return app
