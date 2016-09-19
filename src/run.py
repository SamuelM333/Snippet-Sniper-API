from eve import Eve
from eve.auth import BasicAuth
from bcrypt import hashpw
from flask import current_app as app
from settings import SETTINGS


class BCryptAuth(BasicAuth):
    def check_auth(self, email, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        users = app.data.driver.db['user']
        user = users.find_one({'email': email})
        # return user and hashpw(password, user['password']) == user['password']
        return user and password == user['password']

port = 5000
host = '127.0.0.1'
# host = '0.0.0.0'

app = Eve(settings=SETTINGS) #, auth=BCryptAuth)

if __name__ == '__main__':
    app.run(host=host, port=port)
