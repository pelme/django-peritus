from django.conf import settings as django_settings

def settings(request):
    return {'settings': django_settings,}
    
def dumb_admin(request):
    return {'root_path': '/admin/'}