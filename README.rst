.. image:: https://img.shields.io/pypi/v/wagtail-django-recaptcha.svg
   :target: https://pypi.python.org/pypi/wagtail-django-recaptcha

Wagtail ReCaptcha
================
**Wagtail forms with a ReCaptcha form field/widget integration app.**

wagtail-django-captcha provides an easy way to integrate the `django-recaptcha <https://github.com/praekelt/django-recaptcha>`_ field when using the Wagtail formbuilder.


Installation
------------

#. Install or add ``wagtailcaptcha`` to your Python path.

#. Add ``wagtailcaptcha`` to your ``INSTALLED_APPS`` setting.

#. Config django-recaptcha as explained in `here <https://github.com/praekelt/django-recaptcha>`_.


Usage
-----

Field
~~~~~
The quickest way to add a captcha field to a Wagtail Form Page is to inherit from the two options provided, ``WagtailCaptchaForm`` or ``WagtailCaptchaEmailForm``. The first options inherits from ``AbstractForm`` while the seconds does it from ``AbstractEmailForm``. Either way your page is going to display a captcha field at the end of the form.

Example

.. code-block:: python

    from wagtail.wagtailforms.models import AbstractFormField
    from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
    from wagtail.wagtailcore.fields import RichTextField

    from modelcluster.fields import ParentalKey
    
    from wagtailcaptcha.models import WagtailCaptchaForm


    class SubmitFormField(AbstractFormField):
        page = ParentalKey('SubmitFormPage', related_name='form_fields')


    class SubmitFormPage(WagtailCaptchaForm):
        body = RichTextField(blank=True, help_text='Edit the content you want to see before the form.')
        thank_you_text = RichTextField(blank=True, help_text='Set the message users will see after submitting the form.')

        class Meta:
            verbose_name = "Form submission page"
            description = "Page with the form to submit"


    SubmitFormPage.content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('body', classname="full"),
        FieldPanel('thank_you_text', classname="full"),
        InlinePanel(SubmitFormPage, 'form_fields', label="Form fields"),
        MultiFieldPanel([
            FieldPanel('to_address'),
            FieldPanel('from_address'),
            FieldPanel('subject'),
        ], "Email notification")
    ]


The captcha field can't be added from the admin UI but will appear in your frontend as the last of the form fields.
