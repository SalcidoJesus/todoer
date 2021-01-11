import os

from flask import Flask

def create_app():
    app = Flask(__name__)
    #cuando vayas a poner esto en consola quitale los putos acentos
    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    #from todo import db

    #db.init_app(app)

    #from todo import auth

    #app.register_blueprint(auth.bp)

    @app.route('/hola')
    def hola():
        return 'jesus hola'

    return app
