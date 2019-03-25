from flask import Flask

from .settings import Settings


def create_app(config_class=Settings):

    app = Flask(__name__)
    app.config.from_object(config_class)

    return app


def register_extensions(app):
    pass


def register_blueprints(app):
    pass


def register_shellcontext(app):
    pass
