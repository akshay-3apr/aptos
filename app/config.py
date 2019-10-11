import os
from pathlib import Path,PurePath

basedir = os.path.abspath(os.path.dirname(__file__))
pathlibBaseDir = Path.cwd()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'out_of_ur_range'
    UPLOADS_DEFAULT_DEST = 'app/static/img/'
    UPLOADS_DEFAULT_URL = 'static/img/'
    UPLOADED_IMAGES_DEST = 'app/static/img/'
    UPLOADED_IMAGES_URL = 'static/img/'
    TEMPUSERIMG = pathlibBaseDir / Path('app/static/img')
    IMAGE_STORE = pathlibBaseDir / Path('app/static/img')
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]