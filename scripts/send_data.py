from itsdangerous import JSONWebSignatureSerializer
import requests


URL = 'http://127.0.0.1:8000/push/'

ENDPOINT = 'tr'

PAYLOAD = {'identifier': 'asdf2',
           'source': 'me',
           'text': 'Something happened, again!'}

KEY = 'super-secret-key'


s = JSONWebSignatureSerializer(KEY)
data = s.dumps(PAYLOAD)
r = requests.post(URL + ENDPOINT, data={'data': data})

print(r.status_code)
print(r.text)
