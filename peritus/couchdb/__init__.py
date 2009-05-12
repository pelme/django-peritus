import couchdb
from couchdb.design import ViewDefinition

from peritus.couchdb.conf import settings

server = couchdb.Server(settings.URI)

for db in settings.AUTOCREATE_DATABASES:
    if not db in server:
        server.create(db)

for db, views in settings.AUTOCREATE_VIEWS.items():
    ViewDefinition.sync_many(db, views)
