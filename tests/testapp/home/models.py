from __future__ import absolute_import, unicode_literals

import wagtail
from modelcluster.fields import ParentalKey

from wagtailcaptcha.models import WagtailCaptchaEmailForm, WagtailCaptchaForm

if wagtail.VERSION >= (2, 0):
    from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
    from wagtail.contrib.forms.models import AbstractFormField
else:
    from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
    from wagtail.wagtailforms.models import AbstractFormField


class TestCaptchaEmailFormField(AbstractFormField):
    page = ParentalKey('TestCaptchaEmailFormPage', related_name='form_fields')


class TestCaptchaEmailFormPage(WagtailCaptchaEmailForm):
    content_panels = WagtailCaptchaEmailForm.content_panels + [
        InlinePanel('form_fields', label="Form fields"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


class TestCaptchaFormField(AbstractFormField):
    page = ParentalKey('TestCaptchaFormPage', related_name='form_fields')


class TestCaptchaFormPage(WagtailCaptchaForm):
    content_panels = WagtailCaptchaForm.content_panels + [
        InlinePanel('form_fields', label="Form fields"),
    ]
