import logging

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    # give more context on the error since DRF masks it as Not Found
    request = context.get('request')
    error = ''
    if hasattr(exc, 'message_dict'):
        error = exc.message_dict
    elif hasattr(exc, 'message'):
        error = exc.message
    elif hasattr(exc, 'args') and len(exc.args) > 0:
        error = exc.args[0]
    elif hasattr(exc, 'detail'):
        error = exc.detail

    if isinstance(exc, Http404):
        logging.exception("Http404", exc_info=exc)
        return Response({'detail': 'Not Found',
                         'error': error}, status=status.HTTP_404_NOT_FOUND)

    if isinstance(exc, ValueError):
        logging.exception(f"Bad Request - Method - {request.method}", exc_info=exc)
        return Response({'detail': 'Bad Request',
                         'error': error}, status=status.HTTP_400_BAD_REQUEST)

    response = exception_handler(exc, context)

    # No response means DRF couldn't handle it
    # Output a generic 500 in a JSON format
    if response is None:
        logging.exception(f'Internal Server Error - Method - {request.method}', exc_info=exc)
        return Response({'detail': 'Internal Server Error',
                         'error': error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
