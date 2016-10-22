import requests
from itsdangerous import JSONWebSignatureSerializer


class Collectr:
    def __init__(self, url, endpoint, key):
        self.url = url
        self.endpoint = endpoint
        self.key = key

    def send(self, identifier, source, text):
        payload = {'identifier': identifier,
                   'source': source,
                   'text': text}

        s = JSONWebSignatureSerializer(self.key)
        data = s.dumps(payload)
        r = requests.post(self.url + self.endpoint, data={'data': data})
