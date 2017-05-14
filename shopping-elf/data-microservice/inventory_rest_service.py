import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,Response
from pyfcm import FCMNotification
from flask import json
from flask import jsonify
from werkzeug import secure_filename
import processed_data_service as pdservice;
import MailHelper as mailHelper

app = Flask(__name__)

print "Hello"
print "Happy Monday"

@app.route("/inventory/list/<username>", methods=['GET'])
def getShoppingList(username):
    #return  pdservice.getShoppingList(username))


    j = jsonify(pdservice.getShoppingList(username));
    return j

@app.route("/inventory/notification", methods=['GET'])
def getNotifications():

	push_service = FCMNotification(api_key="AIzaSyB1byDiSollNF32f7auagCdzRXWqcs8aAs")
	j = jsonify(pdservice.getNotificationData())
	message_title ="Shopping notification"
	message_body="You should buy these products by tomorrow : " + "\n"
	products_name=""
	device_registration_ids=[]
	message=""
   
 	for registration_id in j:
 		device_registration_ids.append(registration_id)
 		print device_registration_ids
 		print "registration_id ", registration_id
 		print "length= ", len(j[registration_id])
 		for i in range(0,len(j[registration_id])):
 			products_name = products_name + j[registration_id][i] + ", "

 		print products_name	
 		message = message_body + products_name  + "\n" + "Thank You"
 		result = push_service.notify_multiple_devices(registration_ids=device_registration_ids, message_title=message_title, message_body=message)
 		print result
 		products_name=""
 		message=""
 		device_registration_ids=[]
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
    app.run(port=3008,debug=True, host='0.0.0.0')
