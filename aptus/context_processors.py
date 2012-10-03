from django.utils.http import urlquote
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME


def login_url_with_redirect(request):
    login_url = getattr(settings, 'LOGIN_URL', '/accounts/signin/')
    path = urlquote(request.get_full_path())
    url = '%s?%s=%s' % (login_url, REDIRECT_FIELD_NAME, path)
    return {'login_url': url}
