import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Testing dependencies
testing_extras = [
    # For coverage and PEP8 linting
    'flake8>=2.2.0',
    'isort>=4.2.5',
]

# Documentation dependencies
documentation_extras = [

]

setup(
    name='wagtail-django-recaptcha',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A simple recaptcha field for Wagtail Form Pages.',
    long_description=README,
    url='http://github.com/springload/wagtail-django-recaptcha',
    author='Springload',
    author_email='hello@springload.co.nz',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=['django-recaptcha'],
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras,
    },
    zip_safe=False
)
