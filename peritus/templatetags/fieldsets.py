import copy

from django import template
from django.utils.datastructures import SortedDict

register = template.Library()


# {% get_fieldset <fields> as foo from form %}

def get_fieldset(parser, token):
    try:
        name, fields, as_, variable_name, from_, form = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('badly formatted arguments for %r' % token.split_contents()[0])

    return FieldSetNode([f.strip() for f in fields.split(',')], variable_name, form)

get_fieldset = register.tag(get_fieldset)


class FieldSetNode(template.Node):
    def __init__(self, fields, variable_name, form_variable):
        self.fields = fields
        self.variable_name = variable_name
        self.form_variable = form_variable

    def render(self, context):
        form = template.Variable(self.form_variable).resolve(context)
        new_form = copy.copy(form)
        new_form.fields = SortedDict([(field_name, form.fields[field_name]) for field_name in self.fields])
        context[self.variable_name] = new_form

        return u''
