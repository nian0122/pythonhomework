import requests
url="https://www.python.org"
r=requests.get(url)
r.encoding = 'utf-8'
print(r.text)

