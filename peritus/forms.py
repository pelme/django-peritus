
class AsUlFix(object):
    def as_ul(self):
        """
        Returns this form rendered as HTML <li>s -- excluding the <ul></ul>.
        
        help_text is wrapped in a <p> tag.

        Use this class as a mixin for your forms:

        class MyForm(AsUlFix, forms.Form):
            ...
        """
        return self._html_output(u'<li>%(errors)s%(label)s %(field)s%(help_text)s</li>', u'<li>%s</li>', '</li>', u'<p class="helptext">%s</p', False)

from django import forms

class CleanUniqueField:
    """Wrap the clean_XXX method."""

    def __init__(self, form, name):
        try:
            self.clean = getattr(form, 'clean_' + name)
        except AttributeError:
            self.clean = None

        self.form = form
        self.name = name

    def __call__(self):
        if self.clean:
            result = self.clean()
        else:
            result = self.form.cleaned_data[self.name]

        queryset = self.form._meta.model.objects
        if self.form.instance.pk:
            queryset = queryset.exclude(pk=self.form.instance.pk)

        try:
            queryset.get(**{self.name: result})
        except self.form._meta.model.DoesNotExist:
            return result
        else:
            raise forms.ValidationError(_(u'The %s is already in use.') % self.verbose_name)

class ModelForm(forms.ModelForm):
    """A hack around the Django ticket #4895."""

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for field in self._meta.model._meta.fields:
            if field.unique and field.name in self.base_fields:
                setattr(self, 'clean_' + field.name, CleanUniqueField(self, field.name))
