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
        return self.sendPayload(payload)

    def sendPayload(self, payload):
        s = JSONWebSignatureSerializer(self.key)
        data = s.dumps(payload)
        return requests.post(self.url + self.endpoint, data={'data': data})
