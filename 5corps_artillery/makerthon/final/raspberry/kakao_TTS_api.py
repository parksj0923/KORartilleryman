import time
import argparse
import requests
import pygame

# KaKao Speech Synthesis API
# input = name, output = make "warning.wav" in same directory
def kakao_Speech_Synthesis_api(name):
	file_name = 'warning.mpeg'
	url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
	key = '3cc9239a60f93d908dabe029c94c2213'
	headers = {
		"Content-Type": "application/xml",
		"Authorization": "KakaoAK " + key,
	}

	talk = "{}님, 올바른 마스크 착용 부탁드려요".format(name).encode('utf-8').decode('latin-1')
	data = '<speak><prosody rate="1.2" volume="loud">{}</prosody></speak>'.format(talk)

	res = requests.post(url, headers=headers, data=data)
	f= open(file_name, 'wb')
	f.write(res.content)
	f.close()
	return file_name

if __name__ == "__main__":
	pygame.mixer.init()

	ap = argparse.ArgumentParser()
	ap.add_argument("-n", "--name", required=True, help="input name")
	args = vars(ap.parse_args())

	name = args["name"]
	file_name = kakao_Speech_Synthesis_api(name)
	time.sleep(1.5)
	pygame.mixer.music.load(file_name)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
	#sound = pygame.mixer.Sound(file_name)
	#sound.play()
