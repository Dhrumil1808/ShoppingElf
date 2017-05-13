from pyfcm import FCMNotification
from uregression import estimate_days

push_service = FCMNotification(api_key="AIzaSyB1byDiSollNF32f7auagCdzRXWqcs8aAs")

# OR initialize with proxies

#proxy_dict = {
        #  "http"  : "http://127.0.0.1",
         # "https" : "http://127.0.0.1",
        #}
#push_service = FCMNotification(api_key="<api-key>", proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = ["ci9Vh3AIJv4:APA91bF7D2REk3cAUo_eB_2efGfmYNtXY-KYswPKrA0YwRZboIbVpBse4hEc1CKhQWDDMsBlIqYFMc7Rx24i0GoWSDYIytdVTmGZU7YV2e8BfuhAfjO7vvlKEdIYFvQNtwANUcMAb4Kg"]
#message_title = "Uber update"
#message_body = "Hi john, your customized news for today is ready"
#result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
#print result
# Send to multiple devices by passing a list of ids.
#registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
productData=[['A','2','01-25-2017'],['A','12','01-28-2017'],['A','12','01-28-2017'],['A','5','02-15-2017'],['A','10','02-28-2017'],['A','1','03-05-2017'],['A','6','03-06-2017'],['A','10','03-16-2017'],['A','3','04-01-2017'],['A','8','04-03-2017'],['A','5','04-08-2017']]

message_title = "Shopping notification"
#message_body = int (estimate_days(productData,['A']))
#message_body=str(message_body)
message_body="6"
print message_body
result = push_service.notify_multiple_devices(registration_ids=registration_id, message_title=message_title, message_body=message_body)

print result

# With FCM, you can send two types of messages to clients:
# 1. Notification messages, sometimes thought of as "display messages."
# 2. Data messages, which are handled by the client app.

# Client app is responsible for processing data messages. Data messages have only custom key-value pairs. (Python dict)
# Data messages let developers send up to 4KB of custom key-value pairs.

# Sending a notification with data message payload
data_message = {
    "Nick" : "Mario",
    "body" : "great match!",
    "Room" : "PortugalVSDenmark"
}
# To multiple devices
#result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_body=message_body, data_message=data_message)
# To a single device

#result = push_service.notify_single_device(registration_id=registration_id, message_body=message_body, data_message=data_message)

# Sending a data message only payload, do NOT include message_body
# To multiple devices
#result = push_service.notify_multiple_devices(registration_ids=registration_ids, data_message=data_message)
# To a single device
result = push_service.notify_single_device(registration_id=registration_id, data_message=data_message)

# To send extra kwargs (keyword arguments not provided in any of the methods),
# pass it as a key value in a dictionary to the method being used
extra_kwargs = {
    'content_available': True
}
result = push_service.notify_single_device(registration_id=registration_id, data_message=data_message, extra_kwargs=extra_kwargs)
print result
# To support rich notifications on iOS 10, set
#extra_kwargs = {
 #   'mutable_content': True
#}
# and then write a NotificationService Extension in your app

# Use notification messages when you want FCM to handle displaying a notification on your app's behalf.
# Use data messages when you just want to process the messages only in your app.
# PyFCM can send a message including both notification and data payloads.
# In such cases, FCM handles displaying the notification payload, and the client app handles the data payload.'''