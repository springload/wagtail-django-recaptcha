from __future__ import absolute_import, unicode_literals

from django.conf import settings

WAGTAIL_RECAPTCHA_VERSION = getattr(settings, 'WAGTAIL_RECAPTCHA_VERSION', 2)