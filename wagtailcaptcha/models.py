from wagtail.wagtailforms.models import AbstractEmailForm, AbstractForm

from .forms import WagtailCaptchaFormBuilder


class WagtailCaptchaEmailForm(AbstractEmailForm):
    """Pages implementing a captcha form with email notification should inhert from this"""

    is_abstract = True  # Don't display me in "Add"

    def __init__(self, *args, **kwargs):
        super(WagtailCaptchaEmailForm, self).__init__(*args, **kwargs)
        self.form_builder = WagtailCaptchaFormBuilder

    def process_form_submission(self, form):
        if WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME in form.fields.keys():
            form.fields.pop(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME)
        return super(WagtailCaptchaEmailForm, self).process_form_submission(form)

    class Meta:
        abstract = True


class WagtailCaptchaForm(AbstractForm):
    """Pages implementing a captcha form should inhert from this"""

    is_abstract = True  # Don't display me in "Add"

    def __init__(self, *args, **kwargs):
        super(WagtailCaptchaForm, self).__init__(*args, **kwargs)
        self.form_builder = WagtailCaptchaFormBuilder

    class Meta:
        abstract = True
