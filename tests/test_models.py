from __future__ import absolute_import, unicode_literals

from django.test import TestCase

from home.models import TestCaptchaEmailFormPage, TestCaptchaFormPage
from wagtailcaptcha.forms import WagtailCaptchaFormBuilder


class TestCaptchaEmailFormPageTestCase(TestCase):
    def test_captcha_form_builder_is_set(self):
        page = TestCaptchaEmailFormPage()

        self.assertIs(page.form_builder, WagtailCaptchaFormBuilder)


class TestCaptchaFormPageTestCase(TestCase):
    def test_captcha_form_builder_is_set(self):
        page = TestCaptchaFormPage()

        self.assertIs(page.form_builder, WagtailCaptchaFormBuilder)
