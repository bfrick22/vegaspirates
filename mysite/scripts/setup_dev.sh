#!/usr/bin/env bash


../manage.py createsuperuser << EOF
admin

mypassword
mypassword
EOF

../manage.py migrate;

../manage.py reset polls;
../manage.py runscript polls_testdata;

../manage.py reset socialaccount;
../manage.py runscript socialaccount_testdata;

../manage.py test

exit;