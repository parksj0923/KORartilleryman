import argparse
import json
import base64
import requests
import re

# Naver Clova OCR API
#input filename, output korean text
def naver_OCR_api(frame):
	with open(frame, "rb") as f:
		img= base64.b64encode(f.read())

		URL = "https://2ecb2f2b9c79470cb77f7337f747a291.apigw.ntruss.com/custom/v1/11062/29b707430fc943cd49355417e654eb3515a843d362b418100ec3a70729453661/general"

		KEY = "WmxoWHpja2xFSmVYcWVRblBGU3FBT0xmd2hIalVwUFQ="

		headers = {
			"Content-Type": "application/json",
			"X-OCR-SECRET": KEY
		}

		data = {
			"version": "V1",
			"requestId": "test",
			"timestamp": 0,
			"images": [
				{
				"name": "127777",
				"format": "jpg",
				"data": img.decode('utf-8')
				}
			]
		}
		data = json.dumps(data)
		response = requests.post(URL, data=data, headers=headers)
		res = json.loads(response.text)
		name = ''
		temp = []
		for dic in res['images' ][0]['fields'] :
			name = name + dic['inferText']
			temp = re.compile('[가-힣]+').findall(name)
			if temp =='대' or temp =='한' or temp =='민' or temp =='국' or temp =='육' or temp =='군':
				continue
			name = ''.join(temp)
	return name


if __name__ ==  "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True, help="image file")
	args = vars(ap.parse_args())

	img = args["image"]
	name = naver_OCR_api(img)
	print(name)
