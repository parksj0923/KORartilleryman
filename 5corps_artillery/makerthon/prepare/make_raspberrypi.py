
import cv2
import numpy as np
import os
import io
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model
#mport imutils #나중에 imutils쓸때 주석 해제

import json
import base64
import requests
import re #한글 뽑아낼때 정규식 사용
import os, requests, json, wave #오디오 파일 만들 때 사용

import pygame #wave 파일 출력시 사용
#먼저 라즈베리파이에서 sudo apt-get install python-pygame 설치

#init
pygame.mixer.init()

#얼굴과 마스크 검출 후 확률 보여주는 함수
#입력으로 프레임, facenet, masknet , 출력으로 얼굴위치, 마스크확률
def detect_predict_mask(frame, faceNet, maskNet):
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1., size=(300, 300), mean=(104., 177., 123.))
    # Preprocessing. OpenCV의 FaceNet에서 학습시킨대로 Param값을 넣어줌. DNN이 사용하는 형태로 이미지 변환
    # cv2.dnn.blobFromImage함수가 하는 일은 1. Mean subtraction (평균 빼기) / 2.Scaling (이미지 사이즈 바꾸기) / 3.And optionally channel swapping (옵션, 이미지 채널 바꾸기)
    # (104.0,177.0, 123.0)는 mean subtraction의 경험적 최적값. 그럼 mean subtraction이란 RGB값의 일부를 제외해서 dnn이 분석하기 쉽게 단순화해주는 것.
    # mean substraction 데이터의 모든 feature에 대해 각각에 대해 평균만큼 차감=>모든 차원에 대해 원점이동 느낌
    # (300,300) : dnn모듈이 CNN으로 처리하기 좋은 이미지 사이즈, 모델이 300,300으로 고정
    #출력값은 numpy.ndarray. shape=(N,C,H,W). dtype=numpy.float32.
    
    
    faceNet.setInput(blob) # faceNet에 blob이미지 input
    detections = faceNet.forward() # face detections에 저장
    #result_img = frame.copy()
    
    # initialize our list of faces, their corresponding locations,
	# and the list of predictions from our face mask network
	faces = []
	locs = []
	preds = []
    
    for i in range(detections.shape[2]):
        
        # extract the confidence (i.e., probability) associated with the detection
        confidence = detections[0,0,i,2]
        # detections[0, 0]은 우리가 그릴 박스"들"의 속성
        # 따라서 i는 현재 i번째 박스. 2는 세번째 속성이 의미하는데 이게 얼굴일 확률을 나타냄.
        
        if confidence > 0.5:
            
            # bounding 박스 구하기
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# ensure the bounding boxes fall within the dimensions of
			# the frame
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# extract the face ROI(region of interest), convert it from BGR to RGB channel
			# ordering, resize it to 224x224, and preprocess it
			face = frame[startY:endY, startX:endX]
            #얼굴이 있어야 확률을 유추
            if face.any():
				face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB) #이미지의 컬러시스템 변경
				face = cv2.resize(face, (224, 224))  # 이미지 크기 변경
				face = img_to_array(face)  #이부분이 다른데 안되면 없얘기
				face = preprocess_input(face) # mobileNetV2에서 하는 preprocessing과 똑같은 처리
                #face = np.expand_dims(face, axis=0) # 이렇게 하면 shape이 (224,224,3) 으로 나오는데 넣을때는 (1,224,224,3)이 되어야 하므로 차원하나 추가
                # add the face and bounding boxes to their respective
				# lists
				faces.append(face)
				locs.append((startX, startY, endX, endY))
    # only make a predictions if at least one face was detected
	if len(faces) > 0:
		# for faster inference we'll make batch predictions on *all*
		# faces at the same time rather than one-by-one predictions
		# in the above `for` loop
		faces = np.array(faces, dtype="float32")
		preds = maskNet.predict(faces, batch_size=32)
        #preds shape 확인해보기
    
    # return a 2-tuple of the face locations and their corresponding
	# locations
	return locs, preds
    
# Naver Clova OCR API
#입력으로 파일이름, 출력으로 이름
def naver_OCR_api(frame):
    with open(frame, "rb") as f:
    img = base64.b64encode(f.read())

    # 본인의 APIGW Invoke URL로 치환
    URL = "https://2ecb2f2b9c79470cb77f7337f747a291.apigw.ntruss.com/custom/v1/11062/29b707430fc943cd49355417e654eb3515a843d362b418100ec3a70729453661/general"
    
    # 본인의 Secret Key로 치환
    KEY = "WmxoWHpja2xFSmVYcWVRblBGU3FBT0xmd2hIalVwUFQ="
    
    headers = {
        "Content-Type": "application/json",
        "X-OCR-SECRET": KEY
    }
    
    data = {
        "version": "V1",
        "requestId": "test", # 요청을 구분하기 위한 ID, 사용자가 정의
        "timestamp": 0, # 현재 시간값
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
    for dic in res['images'][0]['fields'] :
      #print(dic['inferText'])
      name = name + dic['inferText']
    temp = re.compile('[가-힣]+').findall(name)
    name = ''.join(temp)
    return name
    
# KaKao Speech Synthesis API
# 입력으로 사람이름, 출력으로 같은 디렉토리에 'warning.wav'파일 생성
def kakao_Speech_Synthesis_api(name):
    file_name = 'warning.wav'
    url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
    key = '3cc9239a60f93d908dabe029c94c2213'
    headers = {
	    "Content-Type": "application/xml",
        "Authorization": "KakaoAK " + key,
    }

    talk = "{}님, 올바른 마스크 착용 부탁드려요".format(name).encode('utf-8').decode('latin-1')
    data = '<speak><prosody rate="1.5" volume="loud">{}</prosody></speak>'.format(talk)

    res = requests.post(url, headers=headers, data=data)
    f= open(file_name, 'wb')
    f.write(res.content)
    f.close()
    return file_name
    

#face_detection prototxtPath & weightsPath
fd_prototxtPath = '../training custom dataset/face_detector/deploy.prototxt'
fd_weightsPath =  '../training custom dataset/face_detector/res10_300x300_ssd_iter_140000.caffemodel'

mask_modelPath = '../training custom dataset/mask_detector.model'

#사진 저장할 디렉토리 
save_imgPath = 'without_Mask/'

# FaceDetector 모델 > OpenCv의 DNN
faceNet = cv2.dnn.readNet(prototxtPath,weightsPath)

# MaskDetector 모델 > Keras 모델
maskNet = load_model(mask_modelPath)

#count는 keywait(1)덕분에 1ms씩 센다. 따라서 1000count에 1초
#기본 가정이 위에껀데 저게 아니면 시간 세는거 엎어야함@@@@@
count = 3000
#1.5초 세는 변수
sec = 1
#사진저장 혹은 tts,ocr시 너무 빨리 사진을 보내거나 읽으면 안되기때문에 초단위로 비교할려고함
check = 0


os.system('sudo modprobe bcm2835-v412')
# 라즈베리 파이에서 OpenCV의 VideoCapure()을 이용하려면 써야하는 명령어
cap = cv2.VideoCapture(0)
#VideoCapture() 파라미터 안에 filename을 넣으면 저장된 비디오를 불러오고, 0,1 등을 넣으면 입력 디바이스 순서(한개인 경우0)에 따라 실시간 영상 촬영 frame을 받아 올 수 있다.
#ret에는 성공이면 true, 실패면 false
#img에는 현재 프레임(numpy형)을 가져온다


#파일이 정상적으로 열였는지 를 확인 True면 정상
while cap.isOpended():
    count +=1
    #2초에 한번씩 사진을 저장할려고 만들었음 안되면 없애기
    sec = count//2000
    ret, frame = cap.read() #가시광선 카메라 현재화면을 이미지로 read
    if not ret:
        break 
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) #이거 화면 돌아가서 인식을 못하는 걸 수 도 있으니까 안되면 꼭 확인하기@@@@@@@@@@@@@@@@@@@@@@
    # OCR을 위해서 frame 복사
    img = frame.copy()
    
    
    # detect faces in the frame and determine if they are wearing a
	# face mask or not
	locs, preds = detect_predict_mask(frame, faceNet, maskNet)
    
    #여기 for문에서 마스크 썻는지 안썻는지 얼굴에 바운딩한 한 프레임(사진)이 나옴
    for (box, pred) in zip(locs, preds):
        #unpack the bounding box and predictions
        (startX, startY, endX, endY) = box
		(mask, withoutMask) = pred
        
        # determine the class label and color we'll use to draw
		# the bounding box and text
        state = "Mask" if mask > withoutMask else "No_Mask" 
        color = (0, 255, 0) if state == "Mask" else (0, 0, 255)
        
        # include the probability in the label
		label = "{}: {:.2f}%".format(state, max(mask, withoutMask) * 100)
        
        # display the label and bounding box rectangle on the output
		# frame
		cv2.putText(frame, label, (startX, startY - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
		cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
        
            
    #마스크를 안썻으면 사진으로 저장하고, OCR하고(TTS도 같이), web으로 사진 보내기(폰으로도)
    #저장은 1초에 한번씩 하는걸로 
    if withoutMask > 0.75:
        #너무 많은 사진과 음성출력이 있으면 안되기 때문에 시간을 두고 함
        if check != sec:
            #naver_ocr_api 사용해서 이름 얻기
            name = naver_OCR_api(img)
        
            #사진 저장하기, 원본이미지인 img가 아닌 바운딩된 frame사용
            cv2.imwrite(save_imgPath + str(count) + name + '.jpg',frame)
        
            #카카오 TTS실행
            sound_file = kakao_Speech_Synthesis_api(name)
            
            #출력파일을 통해 출력하기 짜기
            #여기서 아마 문제가 있을꺼 같은데 만약 여기서 2초를 기다리는동안 다른 프로세스가 돌아가지 않는다면
            #FORK를 써야할듯, 아니면
            #애초에 모니터링을 안하면 여기서 2초씩 기다리는것도 나쁘지 않은듯
            pygame.mixer.music.load("./{}".format(sound_file))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            
            #if name이 빈 문자열이 아니면 web으로 보내기도 짜야함
            
            #시간 조정
            check = sec
        
        
    #화면 쓰면서 영상을 보여줄꺼면 이 구절 쓰면됨
    cv2.imshow("Frame",frame)
    #64bit os면 & 0xFF를 같이 쓰면됨, 아니면 빼면됨
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, 동영상 종료
	if key == ord("q"):
		break

cap.release()

#화면쓸꺼면 이껄로 다 꺼줘야함 
#cv2.destroyAllWindows()