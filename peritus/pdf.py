# encoding: utf-8

from django.template.loader import render_to_string
from django.utils.encoding import smart_str
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import ho.pisa as pisa

def render_to_pdf(template_src, context_dict):
    # Work-around to fix broken å
    html = render_to_string(template_src, context_dict).replace(u'å', '&aring;').replace(u'Å', '&Aring;')
    html = smart_str(html, encoding='iso-8859-1')

    result = StringIO() 
    pdf = pisa.pisaDocument(StringIO(html), result)

    if pdf.err:
        raise Exception('Could not render PDF!')

    return result.getvalue()
