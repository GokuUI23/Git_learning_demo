# program to authenticate github account ( modified to token based)

import requests
# from requests.auth import HTTPBasicAuth

# responce = requests.get('https://api.github.com/user',auth=HTTPBasicAuth('user','pass'))
# print(responce)
# print(responce.json())

# instead using token based authentication

url = 'https://api.github.com/user'
header = {
    'Authorization' : 'token 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'
}

responce = requests.get(url,headers=header)

print(responce)
print(responce.json())