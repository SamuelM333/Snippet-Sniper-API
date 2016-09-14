from eve import Eve
from settings import DOMAIN

port = 5000
# host = '127.0.0.1'
host = '0.0.0.0'

SETTINGS = {'DOMAIN': DOMAIN}

app = Eve(settings=SETTINGS)

if __name__ == '__main__':
    app.run(host=host, port=port)
