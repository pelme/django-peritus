from django.http import HttpResponse
from django.utils import simplejson
from django.core.serializers import serialize
from django.db.models.query import QuerySet


# This snippet was stolen from
# http://www.djangosnippets.org/snippets/154/
class HttpJSONResponse(HttpResponse):
    def __init__(self, object, **dump_kwargs):
        if isinstance(object, QuerySet):
            content = serialize('json', object)
        else:
            content = simplejson.dumps(object, **dump_kwargs)

        super(HttpJSONResponse, self).__init__(content, mimetype='application/json')

    @property
    def data(self):
        """
        Returns the returned data, as a Python object. This is not the original
        object, it is the JSON encoded/decoded version.

        This method is mostly useful for testing.
        """

        return simplejson.loads(self.content)
