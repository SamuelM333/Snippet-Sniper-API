# -*- coding: utf-8 -*-

from eve import Eve
from src.settings import SETTINGS, pre_get_users


port = 5000
host = '127.0.0.1'
# host = '0.0.0.0'

app = Eve(settings=SETTINGS)
app.on_pre_GET_user += pre_get_users

if __name__ == '__main__':
    app.run(host=host, port=port)
