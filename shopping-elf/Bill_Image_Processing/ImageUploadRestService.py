import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from flask import json
from ImageProcessor import ImageProcessor
from flask import jsonify
from werkzeug import secure_filename
import UserService as userService
from Models import UserPojo


app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route("/bill/upload/<username>", methods=['POST'])
def userImageUpload(username):

    file = request.files['file'];
    #jsonObject = request.get_json()
    billDate = request.form['billDate'];
    print billDate    
    #print filename

    if (file and allowed_file(file.filename)):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        imageOutput = ImageProcessor(username, filename, billDate)
        print imageOutput

    return jsonify(imageOutput.getImageContents())

@app.route("/user/signup", methods=['POST'])
def signup():
    request_json=request.get_json()
    email=request_json['email']
    password=request_json['password']
    family_members=request_json['family_members']

    return userService.addUser(UserPojo(email,password,family_members))


@app.route("/user/authenticate", methods=['POST'])
def login():
    request_json=request.get_json()
    email=request_json['email']
    password=request_json['password']


    return userService.findUser(email,password)


@app.route("/user/password-update", methods=['POST'])
def passwordUpdate():
    request_json=request.get_json()
    email=request_json['email']
    password=request_json['password']
    return userService.updateUserPassword(UserPojo(email,password,0))



@app.route("/user/update-api-key", methods=['POST'])
def apiKeyUpdate():
    request_json=request.get_json()
    email=request_json['email']
    api_key=request_json['api-key']
    return userService.updateApiKey(email,api_key)






if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port =3009)
