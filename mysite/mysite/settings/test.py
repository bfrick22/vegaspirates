from __future__ import absolute_import
import sys

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# Tell nose to measure coverage
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=mysite,polls',
    '--cover-html',
]

if 'test' in sys.argv:
    CACHE_MIDDLEWARE_SECONDS = 0

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3'
        }
    }