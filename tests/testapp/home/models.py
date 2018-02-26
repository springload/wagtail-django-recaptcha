from __future__ import absolute_import, unicode_literals

import wagtail
from django.db import models
from modelcluster.fields import ParentalKey

from wagtailcaptcha.models import WagtailCaptchaEmailForm, WagtailCaptchaForm
from .forms import CustomCaptchaFormBuilder

if wagtail.VERSION >= (2, 0):
    from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
    from wagtail.contrib.forms.models import AbstractFormField
else:
    from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
    from wagtail.wagtailforms.models import AbstractFormField


class TestCaptchaEmailFormField(AbstractFormField):
    page = ParentalKey('TestCaptchaEmailFormPage', related_name='form_fields', on_delete=models.CASCADE)


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
    page = ParentalKey('TestCaptchaFormPage', related_name='form_fields', on_delete=models.CASCADE)


class TestCaptchaFormPage(WagtailCaptchaForm):
    content_panels = WagtailCaptchaForm.content_panels + [
        InlinePanel('form_fields', label="Form fields"),
    ]


class TestCustomFormBuilderCaptchaEmailFormField(AbstractFormField):
    page = ParentalKey(
        'TestCustomFormBuilderCaptchaEmailFormPage',
        related_name='form_fields',
        on_delete=models.CASCADE,
    )


class TestCustomFormBuilderCaptchaEmailFormPage(WagtailCaptchaEmailForm):
    form_builder = CustomCaptchaFormBuilder
    is_creatable = False  # Don't show in the admin


class TestCustomFormBuilderCaptchaFormField(AbstractFormField):
    page = ParentalKey('TestCustomFormBuilderCaptchaFormPage', related_name='form_fields', on_delete=models.CASCADE)


class TestCustomFormBuilderCaptchaFormPage(WagtailCaptchaForm):
    form_builder = CustomCaptchaFormBuilder
    is_creatable = False  # Don't show in the admin
