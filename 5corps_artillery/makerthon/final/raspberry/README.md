(folders)

-dataset
    
    마스크 착용, 미착용 이미지 데이터가 들어있는 폴더
    -with_mask
    -witout_mask
    로 이루어짐
    정확히 세보지는 않았지만 각각 거의 500장식은 넘게 들어있음 
    kaggle datasets와 RMFD dataset에서 가져옴

-face_detector

    학습된 얼굴 검출 DNN파일이 들어있는 폴더
    -res10_300x300_ssd_iter_140000.caffemodel
    로 이루어짐

(files)

-main.py:

    라즈베리파이를 동작시키기 위해 실행시키는 main파일
    1.얼굴을 검출하는 학습된 dnn모델을 face_detector에 담겨있는 파일들을 통해 upload
    2.마스크 착용 유무를 식별하는 학습된 mobileNetV2를 불러옴
    3.라즈베리파이 카메라 모듈을 실시간으로 실행시켜 매 프레임별로 사진에서 마스크 착용유무 판단
    4.입력된 프레임별로 이미지 전처리 (기존 프레임 ->blob 객체로 만듬->기존 라이브러리를 활용한 전처리)
    5.전처리 이미지에서 얼굴 부분을 확률적으로 검출후 그 구획을 나누어 입력으로 학습된 마스크 모델에 넣고 마스크 착용유무 판단
    
    6. 마스크 미 착용 검출시 매 프레임마다 영상을 불러올 때 지연되는 것을 방지하기 위해 여러 기능들을 멀티 프로세싱
        6.1 naver_OCR_api.py를 통해 사진의 이름표에서 이름을 텍스트로 받아옴
        6.2 kakao_TTS_api.py를 통해 받은 이름을 input으로 음성을 출력함
        6.3 send_message.py를 통해 서버로 사진을 보냄
        6.4 kakao_MES_api.py를 통해 관리자에게 카카오톡을 보냄
    7. 화면에서 직접 모니터링 할 수 있도록 마스크 착용했든 안했든 각 프레임별로 사람 얼굴부분에 얼굴부분 구획과 마스크 착용유뮤(확률)을 표시 
    
    
-train_mask_detector.py:

    마스크 사진 dataset을 통하여 모델을 학습시키기 위한 파일
    MobileNetV2를 basemodel로 하여 transfer learning을 하였음
    learing rate: 1e-4
    epoch: 20
    batch size: 32 로 하여 
    dataset안의 with_mask, without_mask 이미지 데이터들을 이용하여 학습시킴
    모델 성능 확인을 위하여 전체 dataset의 20%는 test데이터로 사용
    
    성능을 끌어올리기 위하여 data agumentation도 진행
        1. 무작위로 ± 20도 회전
        2.[0.85, 1.15] 범위에서 균일하게 샘플링하여 확대 
        3. 0.1의 비율로 수평 및 수직 이동
        4. 0.2만큼 전단
        5. 무작위로 수평으로 플리핑 정확한 데이터 세트에 따라 이러한 데이터 증가 값을 조정
    
    학습된 모델은 detector.model로 저장
    
-naver_OCR_api.py:

    네이버 클로바 OCR api를 활용하여 사진에서 이름부분을 텍스트로 전환하여 받음
    Input : 사진, Output : 텍스트 data
-kakao_TTS_api.py:

    카카오 음성합성 api를 활용하여 텍스트 데이터를 자연스러운 음성 데이터로 전환하여 받음
    Input : 텍스트 data(string), Output : 디렉토리에 음성파일 저장후 출력
-kako_MES_api.py:

    카카오톡 메세지 보내기 api를 활용하여 지인(친구)에게 카카오톡 보내기 기능
    1.나의 친구 리스트를 불러와서
    2.그중 원하는 사람에게 카카오톡 메세지를 보냄
    Input : x, Output : 지인(친구)에게 원하는 내용의 카카오톡을 보냄
-send_message.py:

    Rest API를 활용하여 서버로 사진데이터와 이름, 위치를 보냄
    Input : 이름, 위치, 이미지, Output : response status code
