import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'b1ded699321ad82f9b2681bab2ed115d'
redirect_uri = 'https://makerthon.com/oauth'
authorize_code = 'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code&scope=talk_message,friends'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
with open("/workspace/Artillery/5corps_artillery/makerthon/kakao_code.json","w") as fp:
    json.dump(tokens, fp)