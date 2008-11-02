from django.http import HttpResponse
from django.utils import simplejson
from django.core.serializers import serialize
from django.db.models.query import QuerySet


# This snippet was stolen from
# http://www.djangosnippets.org/snippets/154/
class HttpJSONResponse(HttpResponse):
    def __init__(self, object):
        if isinstance(object, QuerySet):
            content = serialize('json', object)
        else:
            content = simplejson.dumps(object)

        super(HttpJSONResponse, self).__init__(content, mimetype='application/json')

