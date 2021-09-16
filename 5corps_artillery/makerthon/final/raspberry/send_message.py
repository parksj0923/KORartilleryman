import argparse
import json
import requests
import base64

def send_message(name,location,image):
	with open(image,"rb") as f:
		img = base64.b64encode(f.read())

		URL ='https://maskre.run.goorm.io/upload'

		headers = {
			"Content-Type": "application/json"
		}

		data = {
			"name": name,
			"location": location,
			"image": [
				{
				"name": "find",
				"format": "jpg",
				"data": img.decode('utf-8')
				}
			]

		}

		data = json.dumps(data)
		response = requests.post(URL, data=data, headers=headers)
	return response.status_code

if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("-n", "--name", required=True, help="input name")
	ap.add_argument("-l", "--location", required=True, help="input location")
	ap.add_argument("-i", "--image", required=True, help="input image")
	args = vars(ap.parse_args())

	name = args["name"]
	location = args["location"]
	image = args["image"]
	status = send_message(name,location,image)
	print(status)
