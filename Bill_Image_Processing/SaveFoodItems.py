from flask import Flask
from flask import request
from flask import json
app = Flask(__name__)

hit_url='https://api.ocr.space/parse/image'

import urllib

@app.route("/v1/imageSave", methods=['POST'])
def userInput():
	if request.methods == 'POST':
		request_json=request.get_json()
		language=request_json['language']
		isOverlayRequired=request_json['isOverlayRequired']
		url=request_json['url']  #/home/neil/Desktop/Selection_001.png
		post_params = {
		              'param1' : language,
		              'param2' : isOverlayRequired,
		              'param3' : url
		              }
		post_args = urllib.urlencode(post_params)

		response = urllib.urlopen(hit_url, post_args)
		res_json = json.load(response)
		print res_json

		dicti = res_json['WordText']
		print dicti
		
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
