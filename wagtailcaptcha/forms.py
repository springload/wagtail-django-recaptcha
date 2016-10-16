from wagtail.wagtailforms.forms import FormBuilder

from captcha.fields import ReCaptchaField


class WagtailCaptchaFormBuilder(FormBuilder):
    CAPTCHA_FIELD_NAME = 'wagtailcaptcha'

    def __init__(self, fields):
        super(WagtailCaptchaFormBuilder, self).__init__(fields)
        # Add wagtailcaptcha to FIELD_TYPES declaration
        self.FIELD_TYPES.update({self.CAPTCHA_FIELD_NAME: self.create_wagtailcaptcha_field})

    def create_wagtailcaptcha_field(self, field, options):
        return ReCaptchaField(**options)

    @property
    def formfields(self):
        # Add wagtailcaptcha to formfields property
        fields = super(WagtailCaptchaFormBuilder, self).formfields
        fields[self.CAPTCHA_FIELD_NAME] = ReCaptchaField(label='')

        return fields
