from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,DataRequired,ValidationError,EqualTo,Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask import app
from app import images

class IndexForm(FlaskForm):
    image = FileField('Upload Image Here',validators=[FileRequired(),FileAllowed(['jpg', 'png','jpeg'], 'Images only!')])