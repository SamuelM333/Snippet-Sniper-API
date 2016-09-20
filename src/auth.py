from bcrypt import hashpw
from eve.auth import BasicAuth
from flask import current_app as app
from flask import request


class BCryptAuth(BasicAuth):
    def check_auth(self, email, password, allowed_roles, resource, method):
        users = app.data.driver.db['user']
        lookup = {'email': email}
        auth_user = users.find_one(lookup)

        if auth_user is not None:
            if hashpw(password, auth_user['password']) == auth_user['password']:
                if resource == 'user':
                    if method == 'GET':
                        if auth_user['role'] in ['admin', 'superuser']:
                            return True
                        elif request.path == "/user/{}".format(auth_user['_id']):
                            return True
                    else:
                        if request.json['role'] == 'admin':
                            return auth_user['role'] == "superuser"

                        return True

        return False
