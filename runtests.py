#!/usr/bin/env python

from __future__ import absolute_import, unicode_literals

import os
import sys


def run():
    from django.core.management import execute_from_command_line
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.testapp.testapp.settings'

    sys.path.append(os.path.join('tests', 'testapp'))

    execute_from_command_line([sys.argv[0], 'test'] + sys.argv[1:])


if __name__ == '__main__':
    run()
