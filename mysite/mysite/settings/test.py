from __future__ import absolute_import
from .base import *

DEBUG = True

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# Tell nose to measure coverage
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=mysite,polls',
    '--cover-html',
]