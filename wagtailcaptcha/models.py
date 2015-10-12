from six import text_type

from captcha.fields import ReCaptchaField

from wagtail.wagtailadmin.utils import send_mail
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractForm

from .forms import WagtailCaptchaFormBuilder


class WagtailCaptchaEmailForm(AbstractEmailForm):
    """A WagtailCaptchaEmailForm Page. Pages implementing a captcha form with email notification should inhert from it"""

    is_abstract = True  # Don't display me in "Add"

    def __init__(self, *args, **kwargs):
        super(WagtailCaptchaEmailForm, self).__init__(*args, **kwargs)
        self.form_builder = WagtailCaptchaFormBuilder

    def process_form_submission(self, form):
        super(AbstractEmailForm, self).process_form_submission(form)

        if self.to_address:
            content = ''
            for x in form.fields.items():
                if not isinstance(x[1], ReCaptchaField):  # exclude ReCaptchaField from notification
                    content += '\n' + x[1].label + ': ' + text_type(form.data.get(x[0]))
            send_mail(self.subject, content, [self.to_address], self.from_address,)

    class Meta:
        abstract = True


class WagtailCaptchaForm(AbstractForm):
    """A WagtailCaptchaForm Page. Pages implementing a captcha form should inhert from it"""

    is_abstract = True  # Don't display me in "Add"

    def __init__(self, *args, **kwargs):
        super(WagtailCaptchaForm, self).__init__(*args, **kwargs)
        self.form_builder = WagtailCaptchaFormBuilder

    class Meta:
        abstract = True
