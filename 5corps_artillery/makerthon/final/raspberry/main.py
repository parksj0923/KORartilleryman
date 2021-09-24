import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
import subprocess
import kakao_MES_api

facenet = cv2.dnn.readNet('face_detector/deploy.prototxt', 'face_detector/res10_300x300_ssd_iter_140000.caffemodel')
model = load_model('model.h5')

cap = cv2.VideoCapture(0)

#video save
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_video = cv2.VideoWriter('video.avi',fourcc,5,(640,480))



flag = 0 #with mask state = 0, without mask state = 1 

if not cap.isOpened():

        print("Could not open cam")

        exit()
# loop through frames

while cap.isOpened():
	faces = []
	locs = []
	ret, frame = cap.read()
	frame = cv2.flip(frame,-1)
	if not ret:
		print("Could not read frame")
		exit()

	h, w = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, scalefactor=1., size=(300, 300), mean=(104., 177., 123.))
	facenet.setInput(blob)
	detections = facenet.forward()
	confidence = detections[0, 0, 0, 2]

	if confidence > 0.5:
		box = detections[0, 0, 0, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")
		(startX, startY) = (max(0, startX), max(0, startY))
		(endX, endY) = (min(w - 1, endX), min(h - 1, endY))
		face = frame[startY:endY, startX:endX]
		if face.any():
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)
			faces.append(face)
			locs.append((startX, startY, endX, endY))
			faces = np.array(faces, dtype="float32")
			preds = model.predict(faces, batch_size=32)
		for (box, no_mask) in zip(locs, preds):
			(startX, startY, endX, endY) = box
			if no_mask > 0.6:
				if flag == 0:
					cv2.imwrite('find.jpg',frame)
					name = subprocess.check_output("python3 naver_OCR_api.py -i find.jpg", shell = True)
					p = subprocess.Popen(['python3','kakao_TTS_api.py','-n',name])
					p2 = subprocess.Popen(['python3','send_message.py','-n',name, '-l','cam01','-i','find.jpg'])
					p3 = subprocess.Popen(['python3','kakao_MES_api.py'])
				flag = 1
				color = (0,0,255)
				label = "No Mask ({:.2f}%)".format(no_mask[0]*100)
				cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color,2)
				cv2.rectangle(frame, (startX, startY), (endX, endY), color,2)

			else:
				flag = 0
				color = (0,255,0)
				label = "Mask ({:.2f}%)".format( (1-no_mask[0]) * 100)
				cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
				cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

	cv2.imshow('mask',frame)
	out_video.write(frame)
	if cv2.waitKey(1) & 0xFF == 27:
		break

cap.release()
out_video.release()
cv2.destroyAllWindows()
