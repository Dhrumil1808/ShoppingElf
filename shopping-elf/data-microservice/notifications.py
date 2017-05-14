from pyfcm import FCMNotification
#from uregression import estimate_days


push_service = FCMNotification(api_key="AIzaSyB1byDiSollNF32f7auagCdzRXWqcs8aAs")

registration_id = ["ci9Vh3AIJv4:APA91bF7D2REk3cAUo_eB_2efGfmYNtXY-KYswPKrA0YwRZboIbVpBse4hEc1CKhQWDDMsBlIqYFMc7Rx24i0GoWSDYIytdVTmGZU7YV2e8BfuhAfjO7vvlKEdIYFvQNtwANUcMAb4Kg"]
#print len(registration_id[0])
#productData=[['A','2','01-25-2017'],['A','12','01-28-2017'],['A','12','01-28-2017'],['A','5','02-15-2017'],['A','10','02-28-2017'],['A','1','03-05-2017'],['A','6','03-06-2017'],['A','10','03-16-2017'],['A','3','04-01-2017'],['A','8','04-03-2017'],['A','5','04-08-2017']]

message_title ="Shopping notification"
message_body="6"
print message_body
result = push_service.notify_multiple_devices(registration_ids=registration_id, message_title=message_title, message_body=message_body)

#print result
