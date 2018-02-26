from __future__ import absolute_import, unicode_literals

import wagtail
from .forms import WagtailCaptchaFormBuilder, remove_captcha_field

if wagtail.VERSION >= (2, 0):
    from wagtail.contrib.forms.models import AbstractEmailForm, AbstractForm
else:
    from wagtail.wagtailforms.models import AbstractEmailForm, AbstractForm


class WagtailCaptchaEmailForm(AbstractEmailForm):
    """Pages implementing a captcha form with email notification should inhert from this"""

    form_builder = WagtailCaptchaFormBuilder

    def process_form_submission(self, form):
        remove_captcha_field(form)
        return super(WagtailCaptchaEmailForm, self).process_form_submission(form)

    class Meta:
        abstract = True


class WagtailCaptchaForm(AbstractForm):
    """Pages implementing a captcha form should inhert from this"""

    form_builder = WagtailCaptchaFormBuilder

    def process_form_submission(self, form):
        remove_captcha_field(form)
        return super(WagtailCaptchaForm, self).process_form_submission(form)

    class Meta:
        abstract = True
