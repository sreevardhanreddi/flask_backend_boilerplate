from flask import Flask, request
from config import config


app = Flask(__name__)


def create_app(config_name):
    app.config.from_object(config[config_name])

    from auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from chapters_verses import gita as gita_blueprint

    app.register_blueprint(gita_blueprint, url_prefix="/gita")

    app.run(debug=True)


if __name__ == "__main__":
    create_app("development")

