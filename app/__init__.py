from flask import Flask
from app.config import Config
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES, configure_uploads
import logging
from logging.handlers import SMTPHandler,RotatingFileHandler
import os
from flask_moment import Moment

project = Flask(__name__)
project.config.from_object(Config)

# Configure the image uploading via Flask-Uploads
images = UploadSet('images', IMAGES)
moment = Moment(project)
configure_uploads(project, images)

Bootstrap(project)

if not project.debug:

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/aptos.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    project.logger.addHandler(file_handler)

    project.logger.setLevel(logging.INFO)
    project.logger.info('APTOS startup')

from app import routes