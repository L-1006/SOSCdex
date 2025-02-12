from .base import *

DEBUG = False

# Force python-social-auth (Discord OAuth2) to use https redirection
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

# Correctly read the headers when using a proxy like nginx
# Failing to configure this setting will result in CSRF errors in HTTPS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
