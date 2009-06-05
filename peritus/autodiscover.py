import imp
from django.conf import settings

class Autodiscover(object):
    def __init__(self, module_name):
        self.module_name = module_name

    def __call__(self):
        for app in settings.INSTALLED_APPS:
            try:
                app_path = __import__(app, {}, {}, [app.split('.')[-1]]).__path__
            except AttributeError:
                continue

            try:
                imp.find_module(self.module_name, app_path)
            except ImportError:
                continue

            __import__("%s.%s" % (app, self.module_name))
