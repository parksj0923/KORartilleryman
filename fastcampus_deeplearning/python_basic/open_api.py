#open API 이용하여 원하는 데이터 가져오기
#openAPI(Application Programming Interface)

#Mashup서비스 : 하나 이상의 외부의 서비스를 갖고와서 application을 만드는것  

#공공데이터포털에서 이용
#여기서는 고속도로 공공데이터 포털에서 함
#먼저 openAPI 인증키를 발급받아야함->2457386156
#여기서는 고속도로 공공데이터포털->교통->통행시간->실시간 영업소간 통행시간

#1.Open API
#실시간 영업소간 통행시간
# url : http://data.ex.co.kr/openapi/trtm/realUnitTrtm

import requests

key = '2457386156'
type ='json'
StartUnitcode = '101'
EndUnitCode = '103'

URL = 'http://data.ex.co.kr/openapi/trtm/realUnitTrtm'

url = URL + '?key=' + key + '&type=json&iStartUnitCode=' + StartUnitcode + '&iEndUnitCode=' + EndUnitCode 

response = requests.get(url)

#print(response)
#그냥 print해버리면 <response [200]>이렇게 온다
#json형식으로 온것을 봐야함

json = response.json()
#print(json)

#필요한 부분만 뽑아서 가져오기-차들이 있는것
cars = json['realUnitTrtmVO']

#여기서도 또 뽑아오기
records = []
for car in cars:
    dic = {}
    dic['date'] = car['stdDate']
    dic['time'] = car['stdTime']
    dic['type'] = car['tcsCarTypeDivName']
    records.append(dic)
print(records)