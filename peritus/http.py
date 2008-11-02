from django.conf import settings
from django.http import HttpResponseServerError, HttpResponseBadRequest, HttpResponse
from django.utils import simplejson
from django.core.serializers import serialize
from django.db.models.query import QuerySet

# This snippet was stolen from
# http://www.djangosnippets.org/snippets/650/
class AJAXSimpleExceptionResponse:
    def process_exception(self, request, exception):
        if settings.DEBUG and request.is_ajax():
            import sys, traceback
            exc_type, exc_info, tb = sys.exc_info()
            response = "%s\n" % exc_type.__name__
            response += "%s\n\n" % exc_info
            response += "TRACEBACK:\n"
            for tb in traceback.format_tb(tb):
                response += "%s\n" % tb

            return HttpResponseServerError(response)

# This snippet was stolen from
# http://www.djangosnippets.org/snippets/154/
class HttpJSONResponse(HttpResponse):
    def __init__(self, object):
        if isinstance(object, QuerySet):
            content = serialize('json', object)
        else:
            content = simplejson.dumps(object)

        super(HttpJSONResponse, self).__init__(content, mimetype='application/json')

