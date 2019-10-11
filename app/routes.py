from app import project
from app.forms import IndexForm
from app.config import Config
from flask import jsonify, render_template, request,flash, redirect, url_for,send_from_directory
from werkzeug.urls import url_parse
from PIL import Image
import base64,json,os,traceback,sys
from pathlib import Path
from app import images
from datetime import datetime
from app.predict import APTOS

@project.route('/index',methods=['GET'])
def register():
    form = IndexForm()
    return render_template('index.html', title='Register', form=form)


    
@project.route('/displayImage',methods=['GET','POST'])
@project.route('/',methods=['GET','POST'])
def displayImage():
    url=''
    if request.method == 'POST':
        if 'file' in request.files:
            image = request.files['file']
            label = APTOS().predict(image=image.read())
            print('label: ',label)
            
            with open('image.txt', 'w') as f:
                f.write("Read")
                f.write(str(image.read()))
                f.write("Stream")
                f.write(str(image.stream))
            if image.filename == "":
                print("No filename")
                return redirect(request.url)
            
            if allowed_image(image.filename):
                # filename=Image.open(image)
                # secure_name = image.filename
                # filename.save(Config.TEMPUSERIMG / secure_name)
                # url = images.url(image.filename)
                return jsonify(uploaded_image='',label = label)
            else:
                flash("That file extension is not allowed")
                return redirect(request.url)

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in project.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

def unique_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            return path