
class AsUlFix(object):
    def as_ul(self):
        """
        Returns this form rendered as HTML <li>s -- excluding the <ul></ul>.
        
        help_text is wrapped in a <p> tag.

        Use this class as a mixin for your forms:

        class MyForm(AsUlFix, forms.Form):
            ...
        """
        return self._html_output(u'<li>%(errors)s%(label)s %(field)s<p>%(help_text)s</p></li>', u'<li>%s</li>', '</li>', u' %s', False)
