import time

from collectr import Collectr

URL = 'http://127.0.0.1:8000/push/'
ENDPOINT = 'tr'
KEY = 'super-secret-key'

c = Collectr(URL, ENDPOINT, KEY)
r = c.send('asdf ' + str(int(time.time())), 'me', 'Es ist schon wieder was passiert.')

print(r.status_code)
print(r.text)
