from django.conf import settings as django_settings

URI = getattr(django_settings, 'COUCHDB_URI', 'http://localhost:5984/')

AUTOCREATE_DATABASES = getattr(django_settings, 'COUCHDB_AUTOCREATE_DATABASES', [])

# {'foodb': [ViewDefinition('docname', 'viewname', 'function(doc) { emit(null, null); }), ]}'),}
AUTOCREATE_VIEWS = getattr(django_settings, 'COUCHDB_AUTOCREATE_VIEWS', {})
