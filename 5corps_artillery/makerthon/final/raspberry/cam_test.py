from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

#얼굴을 인식하는 facenet 객체 생성, 마스크 착용 유무를 알려줄 model 생성. (모델은 이미 만들어진 상태)
facenet = cv2.dnn.readNet('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')
model = load_model('mask_detector.model')

#비디오를 읽어서 cap에 저장. cap.read()로 비디오의 한 프레임씩을 읽는다. 
#프레임을 잘 읽었냐에 따라 ret이 True or False가 나옴.
# img는 읽은 프레임이 나온다. 이때 읽은 프레임은 사진이므로 가로,세로 사이즈가 나온다
# img.shape[0]은 세로, img.shape[1]은 가로이다.

cap = cv2.VideoCapture(0)
ret, img = cap.read()



# fourcc는 동영상 파일의 코덱, 압축방식, 색상, 픽셀 포멧 등을 정의하는 정수 값임. 그냥 검색해서 사용 ㄱㄱ
# cv2.VideoWriter(파일 이름, fourcc, fps, 프레임 사이즈) 이렇게 기본 파라미터임.
# cap.get(cv2.CAP_PROP_FPS) -> 요것은 초당 프레임 수를 넣을 수 있음.
fps = cap.get(cv2.CAP_PROP_FPS)
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#delay = round(1000/fps)
out = cv2.VideoWriter('output2.mp4', fourcc, fps, (img.shape[1],img.shape[0]))  
# frame_count = 0
while cap.isOpened(): # 영상이 열리는지 유무 확인
    ret, frame = cap.read() # 프레임 확인하고 사이즈 확인.
    if not ret: #만약 프레임이 False가 뜬다면 break.
        break

    h, w = frame.shape[:2] #h는 세로 w는 가로를 의미하므로 프레임 사이즈를 각 변수에 대입시키는 것이다.

    blob = cv2.dnn.blobFromImage(frame, scalefactor=1., size=(300, 300), mean=(104., 177., 123.)) #영상을 blob객체로 만들어서 추론을 진행해야 한다고 합니다. blobFromImage(입력영상, 입력 픽셀에 곱할 값, 출력영상의 크기, 입력 영상 픽셀에서 뺄 평균값(104,177,123은 경험적 최적값임.) )
    facenet.setInput(blob) #blob객체로 설정한 내용을 readNet으로 만든 facenet객체에 적용시킴.
    dets = facenet.forward() #facenet객체로 추론을 시작함. 결론적으로 facenet 객체는 face_detection 모델이기 때문에 얼굴 감지 모델 결과가 dets에 저장됨.

    result_img = frame.copy()
      
    for i in range(dets.shape[2]): # for를 통해 dets.shape[2]까지 반복하는 이유는 얼굴 감지를 1건만 한것이 아니라 여러 건 했을 수도 있기 때문이다.
        confidence = dets[0, 0, i, 2] #dets의 결과가 0.5, 즉 확신도가 50% 미만이면 continue하고 
        if confidence < 0.5:
            continue

        x1 = int(dets[0, 0, i, 3] * w)
        y1 = int(dets[0, 0, i, 4] * h)
        x2 = int(dets[0, 0, i, 5] * w)
        y2 = int(dets[0, 0, i, 6] * h)
        
        face = frame[y1:y2, x1:x2]

        try:
          face_input = cv2.resize(face, dsize=(224, 224))
          face_input = cv2.cvtColor(face_input, cv2.COLOR_BGR2RGB)
          face_input = preprocess_input(face_input)
          face_input = np.expand_dims(face_input, axis=0)
        except Exception as e:
          print(str(e))
        
        mask, nomask = model.predict(face_input).squeeze()

        if mask > nomask:
            color = (0, 255, 0)
            label = 'Mask %d%%' % (mask * 100)
        else:
            color = (0, 0, 255)
            label = 'No Mask %d%%' % (nomask * 100)


        cv2.rectangle(result_img, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=color, lineType=cv2.LINE_AA)
        cv2.putText(result_img, text=label, org=(x1, y1 - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=color, thickness=2, lineType=cv2.LINE_AA)

    out.write(result_img)
    #plt.imshow('result', result_img)
    if cv2.waitKey(1) == ord('q'):
       break

cap.release()
out.release()