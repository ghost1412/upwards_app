"""
Middleware to log all requests and responses.
Uses a logger configured by the name of django.request
to log all requests and responses according to configuration
specified for django.request.
"""
# import json
import logging
from django.http import JsonResponse

from django.utils.deprecation import MiddlewareMixin
import time

request_logger = logging.getLogger('django.request')


class LoggingMiddleware(MiddlewareMixin):
    """Request Logging Middleware."""

    def __init__(self, *args, **kwargs):
            """Constructor method."""
            super().__init__(*args, **kwargs)

    def process_request(self, request):
        """Set Request Start Time to measure time taken to service request."""
        if request.method in ['POST', 'PUT', 'PATCH']:
            request.req_body = request.body
        if str(request.get_full_path()).startswith('/api/'):
            request.start_time = time.time()

    def process_exception(self, request, exception):
        """Log Exceptions."""
        name = type(exception).__name__
        message = str(exception)
        request_logger.exception(msg=message)
        response_data = {'name': name, 'error': message}

        return JsonResponse(response_data, status=200)