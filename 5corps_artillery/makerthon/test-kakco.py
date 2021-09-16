import json
import requests

KAKAO_TOKEN1 = 'ckLLW8bqkYWB_uTLeitG7nqXH5VW_lqddeFZxwo9dRoAAAF77Q_pIQ'
KAKAO_TOKEN2 = 'suxIY38_tr9eWPP6cA2wwhGXzIKFWIUUJrDUHgopb7gAAAF77Whasg'

def getFriendsList():
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN2}
    url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 정보 요청

    result = json.loads(requests.get(url, headers=header).text)

    friends_list = result.get("elements")
    friends_id = []

    print(requests.get(url, headers=header).text)

    for friend in friends_list:
        friends_id.append(str(friend.get("uuid")))

    return friends_id

url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + KAKAO_TOKEN1
}


data = {
    "receiver_uuids": json.dumps(["{}".format(getFriendsList()[0])]),
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "마스크 미착용자 검출!",
                                     "link" : {
                                                 "web_url" : "https://maskre.run.goorm.io",
                                                "mobile_web_url" : "https://maskre.run.goorm.io"
                                                 
                                              }
                                     
    })
}


response = requests.post(url, headers=headers, data=data)
'''print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))'''

