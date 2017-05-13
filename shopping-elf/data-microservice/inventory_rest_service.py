import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,Response

from flask import json
from flask import jsonify
from werkzeug import secure_filename
import processed_data_service as pdservice;
import MailHelper as mailHelper

app = Flask(__name__)



@app.route("/inventory/list/<username>", methods=['GET'])
def getShoppingList(username):
    #return  pdservice.getShoppingList(username))


    j = jsonify(pdservice.getShoppingList(username));


    return j

@app.route("/inventory/notification", methods=['GET'])
def getNotifications():


    j = jsonify(pdservice.getNotificationData());


    return j


@app.route("/inventory/mail/<user>", methods=['GET'])
def mail(user):
    sList = pdservice.getShoppingListProducts(user)

    txt = ""
    for p in sList:
        txt=txt+""+p+"\n";

    mailHelper.sendemail(from_addr='shoppingelf.3clicks@gmail.com',
              to_addr_list=[user],
              cc_addr_list=[],
              subject='Shopping List',
              message='Here is your Shopping List:\n \n\n'+txt,
              )

    return "sent"



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=3008)
