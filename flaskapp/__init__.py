"""
Пакет для работы с Flask, APScheduler и запросами к hh.ru
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
import dash
from hhconfig import Config as cnf


def create_server():
    flask_server = Flask(__name__, instance_relative_config=True)
    flask_server.config.from_object(cnf)
    flask_server.config.from_pyfile('config.py')

    return flask_server


def create_app():
    db.init_app(server)
    app = dash.Dash(__name__, server=server)

    return app


db = SQLAlchemy()
scheduler = APScheduler()
server = create_server()
footer = server.config['FOOTER']
