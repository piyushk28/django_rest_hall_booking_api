import datetime

DEV_STATIC_VARS = {
    'db_settings': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'booking_mgmt',
        'USER': 'premier_agent_network',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'rest_framework': {

        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
        'EXCEPTION_HANDLER':
            'utils.custom_exception_handler.custom_exception_handler',
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 100
    },
    'swagger': {
        'SECURITY_DEFINITIONS': {
            "api_key": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            },
        },
    },
    'jwt': {
        'JWT_ALGORITHM': 'HS256',
        'JWT_VERIFY': True,
        'JWT_LEEWAY': 0,
        'JWT_AUDIENCE': None,
        'JWT_ISSUER': None,
        'JWT_AUTH_HEADER_PREFIX': 'JWT',
        # 'JWT_PAYLOAD_GET_USER_ID_HANDLER': 'jwt_auth.utils.jwt_get_user_id_from_payload_handler',
        'SESSION_EXPIRE_AT_BROWSER_CLOSE': True,
        'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=30),
        'JWT_VERIFY_EXPIRATION': True,
        'JWT_ALLOW_REFRESH': True,
        'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1),
        # 'JWT_RESPONSE_PAYLOAD_HANDLER': 'premier_agent_network_drf.jwt.custom_jwt_response_payload_handler',
    }
}

STATIC_VARS = DEV_STATIC_VARS
