import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail-django-recaptcha',
    version='0.1',
    packages=find_packages(),
    install_requires=['django-recaptcha'],
    include_package_data=True,
    license='BSD License',
    description='A simple recaptcha field for Wagtail Form Pages.',
    long_description=README,
    url='http://github.com/springload/wagtail-django-recaptcha',
    author='Jordi J. Tablada',
    author_email='jordi@springload.co.nz',
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
)
