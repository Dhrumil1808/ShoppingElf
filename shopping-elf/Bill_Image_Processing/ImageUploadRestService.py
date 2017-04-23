from flask import Flask
from flask import request
from flask import json
from ImageProcessor import ImageProcessor
from flask import jsonify

app = Flask(__name__)

@app.route("/bill/upload/<username>",methods=['POST'])
def userImageUpload(username):
	jsonObject=request.get_json()
	filename = jsonObject['filename']
	billDate = jsonObject['billDate']
	print filename
	imageOutput = ImageProcessor(username, filename,billDate)
	print imageOutput

	return jsonify(imageOutput.getImageContents(), username)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
