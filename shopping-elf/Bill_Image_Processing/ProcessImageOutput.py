from flask import Flask
from flask import request
from flask import json
from ImageOutput import ImageOutput
from flask import jsonify

app = Flask(__name__)

@app.route("/v1/<username>",methods=['POST'])
def userImageUpload(username):
	jsonObject=request.get_json()
	filename = jsonObject['filename']
	imageOutput = ImageOutput(username, filename)
	return jsonify(imageOutput.getImageContents(), username)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')