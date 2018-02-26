from __future__ import absolute_import, unicode_literals

import json

from django.test import TestCase

from home.forms import CustomCaptchaFormBuilder
from home.models import (
    TestCaptchaEmailFormPage,
    TestCaptchaFormPage,
    TestCustomFormBuilderCaptchaEmailFormPage,
    TestCustomFormBuilderCaptchaFormPage,
)
from wagtailcaptcha.forms import WagtailCaptchaFormBuilder

try:
    from test.test_support import EnvironmentVarGuard  # Python 2
except ImportError:
    from test.support import EnvironmentVarGuard  # Python 3


class CaptchaTestingModeMixin(TestCase):
    """Allow Captcha to pass regardless of the value provided"""

    def setUp(self):
        self.captcha_testing_mode_env = EnvironmentVarGuard()
        self.captcha_testing_mode_env.set('RECAPTCHA_TESTING', 'True')

        self.captcha_form_data = {'recaptcha_response_field': 'PASSED'}


class TestCaptchaEmailFormPageTestCase(CaptchaTestingModeMixin, TestCase):
    fixtures = ['test_data.json']

    def test_default_form_builder_is_set(self):
        page = TestCaptchaEmailFormPage()

        self.assertIs(page.form_builder, WagtailCaptchaFormBuilder)

    def test_form_builder_can_be_replaced(self):
        page = TestCustomFormBuilderCaptchaEmailFormPage()

        self.assertIs(page.form_builder, CustomCaptchaFormBuilder)

    def test_captcha_field_is_removed_from_submission_data(self):
        page = TestCaptchaEmailFormPage.objects.get(slug='email-form')
        form_data = dict(self.captcha_form_data, name='Robert')
        form = page.get_form(form_data)

        with self.captcha_testing_mode_env:
            self.assertTrue(form.is_valid())

        form_submission = page.process_form_submission(form)
        submission_data = json.loads(form_submission.form_data)

        self.assertNotIn(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, submission_data)


class TestCaptchaFormPageTestCase(CaptchaTestingModeMixin, TestCase):
    fixtures = ['test_data.json']

    def test_default_form_builder_is_set(self):
        page = TestCaptchaFormPage()

        self.assertIs(page.form_builder, WagtailCaptchaFormBuilder)

    def test_form_builder_can_be_replaced(self):
        page = TestCustomFormBuilderCaptchaFormPage()

        self.assertIs(page.form_builder, CustomCaptchaFormBuilder)

    def test_captcha_field_is_removed_from_submission_data(self):
        page = TestCaptchaFormPage.objects.get(slug='form')
        form_data = dict(self.captcha_form_data, name='Robert')
        form = page.get_form(form_data)

        with self.captcha_testing_mode_env:
            self.assertTrue(form.is_valid())

        form_submission = page.process_form_submission(form)
        submission_data = json.loads(form_submission.form_data)

        self.assertNotIn(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, submission_data)
