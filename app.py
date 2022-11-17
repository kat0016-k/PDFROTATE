import requests

url ='http://127.0.0.1:5000/pdf'
files = {'file': open('kartik.pdf', 'rb')}
r = requests.post(url, files=files)