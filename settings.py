MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'apitest'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

user = {
    'item_title': 'user',
    'cache_control': '',
    'cache_expires': 0,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH'],
    'schema': {
        # Schema definition, based on Cerberus grammar. Check the Cerberus project
        # (https://github.com/nicolaiarocci/cerberus) for details.
        'first_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required': True,
        },
        'last_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required': True,
        },
        'email': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required': True,
            'unique': True,
        },
        'password': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 60,
            'required': True,
        },
        'role': {
            'type': 'string',
            'allowed': ["user", "admin", "superuser"],
            'required': True,
        },
        'coupon': {
            'type': 'dict',
            'schema': {
                'percentage': {'type': 'number'},
                'date_assigned': {'type': 'datetime'},
                'date_used': {'type': 'datetime'},
                'used': {'type': 'boolean'}
            }
        },
        'buy_list': {'type': 'list', 'schema': {'type': 'objectid'}},
        'pantry': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'pantry_name': {'type': 'string'},
                    'articles': {
                        'type': 'list',
                        'schema': {
                            'type': 'dict',
                            'schema': {
                                'article_name': {'type': 'string'},
                                'quantity': {'type': 'number'}
                            }
                        }
                    }
                }
            }
        },
        'location': {
            'type': 'dict',
            'schema': {
                'address': {'type': 'string'},
                'city': {'type': 'string'}
            },
        },
    }
}

DOMAIN = {
    'user': user,
}
