class ScaffoldFormTemplate(object):

    def __init__(self, formclass, form_name='form'):
        self.formclass = formclass
        self.form_name = form_name
        
    def generate(self, row):
        html = ''
        fields = self.formclass.base_fields
        for i in fields:
            html += row % {'field': i, 'form': self.form_name}
        return html

    def as_ul(self):
        return self.generate('''       
<li>
    {%% if %(form)s.%(field)s.errors %%}
    <ul class="errorlist">
        {%% for error in %(form)s.%(field)s.errors %%}
        <li>{{ error }}</li>
        {%% endfor %%}
    </ul>
    {%% endif %%}
    <label>{{ %(form)s.%(field)s.label }}</label>
    {{ %(form)s.%(field)s }}
    {%% if %(form)s.%(field)s.help_text %%}<p>{{ %(form)s.%(field)s.help_text }}</p>{%% endif %%}
</li>
    ''')