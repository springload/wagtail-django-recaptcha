from __future__ import absolute_import, unicode_literals

from wagtailcaptcha.forms import WagtailCaptchaFormBuilder


class CustomCaptchaFormBuilder(WagtailCaptchaFormBuilder):
    pass  # This doesn't implement any new functionality but is needed to test that subclassing is possible.
