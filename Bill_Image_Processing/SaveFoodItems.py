from flask import Flask
from flask import request
from flask import json
app = Flask(__name__)

language='eng'
isOverlayRequired='true'
url='/home/neil/Desktop/Selection_001.png'
hit_url='https://api.ocr.space/parse/image'

import urllib

post_params = {
              'param1' : language,
              'param2' : isOverlayRequired,
              'param3' : url
              }
post_args = urllib.urlencode(post_params)

@app.route("/v1/imageSave", methods=['POST'])
def userInput():
	if request.methods == 'POST':
		response = urllib.urlopen(hit_url, post_args)
		res_json = json.load(response)
		print res_json
		
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
