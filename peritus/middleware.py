import sys
import traceback

from django.conf import settings
from django.http import HttpResponseServerError, Http404, HttpResponseNotFound

# This snippet was stolen from
# http://www.djangosnippets.org/snippets/650/
# Add this line to MIDDLEWARE_CLASSES:
# 'peritus.middleware.AJAXSimpleExceptionResponse',


class AJAXSimpleExceptionResponse:
    def process_exception(self, request, exception):
        if settings.DEBUG and request.is_ajax():
            # Special case for Http404 exceptions
            if isinstance(exception, Http404):
                return HttpResponseNotFound(exception.message)

            exc_type, exc_info, tb = sys.exc_info()
            response = "%s\n" % exc_type.__name__
            response += "%s\n\n" % exc_info
            response += "TRACEBACK:\n"
            for tb in traceback.format_tb(tb):
                response += "%s\n" % tb

            return HttpResponseServerError(response)
