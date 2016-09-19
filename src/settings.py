# -*- coding: utf-8 -*-

from bcrypt import hashpw
from eve.auth import BasicAuth
from flask import current_app as app


class BCryptAuth(BasicAuth):
    def check_auth(self, email, password, allowed_roles, resource, method):
        users = app.data.driver.db['user']
        logging_user = users.find_one({'email': email})
        if logging_user and '_id' in logging_user:
            self.set_request_auth_value(logging_user['_id'])
        return user and hashpw(password, logging_user['password']) == logging_user['password']


def pre_get_users(request, lookup):
    email = app.auth.get_request_auth_value()
    print(email)
    # only return user with current username
    lookup["email"] = email


MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'
MONGO_DBNAME = 'snippet_sniper'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

user = {
    'item_title': 'user',
    'cache_control': '',
    'cache_expires': 0,
    'item_methods': ['GET', 'PATCH', 'PUT'],
    'resource_methods': ['GET', 'POST'],
    'authentication': BCryptAuth,
    'auth_field': 'user_id',
    'additional_lookup': {
        'url': 'regex("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")',
        'field': 'email'
    },
    'schema': {
        'first_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 120,
            'required': True,
        },
        'last_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 120,
        },
        'email': {
            'type': 'string',
            'minlength': 8,
            'maxlength': 120,
            'required': True,
            'unique': True,
            'regex': "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        },
        'password': {
            'type': 'string',
            'minlength': 8,
            'maxlength': 120,
            'required': True,
        },
        'role': {
            'type': 'string',
            'allowed': ["user", "admin", "superuser"],
            'required': True,
        }
    }
}

snippet = {
    'item_title': 'snippet',
    'cache_control': '',
    'cache_expires': 0,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH', 'PUT'],
    'schema': {
        'title': {
            'type': 'string',
            'minlength': 5,
            'maxlength': 60,
            'required': True
        },
        'body': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'language': {'type': 'string'},  # Choices
                    'body': {'type': 'string'}
                }
            },
            'minlength': 1,
            'maxlength': 128,
            'required': True
        },
        'owner': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'user',
                # make the owner embeddable with ?embedded={"owner":1}
                'embeddable': True
            },
        },
        'created': {'type': 'datetime'}
    }
}

SETTINGS = {
    'DOMAIN': {
        'user': user,
        'snippet': snippet,
    },
    'X_DOMAINS': '*',
    'X_HEADERS': '*',
    'XML': False
}
