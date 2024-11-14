import requests as r

status = r.post('https://httpbin.org/post',data={'key':'value'})
print(status)
print(status.json())

