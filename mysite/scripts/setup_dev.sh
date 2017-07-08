#!/usr/bin/env bash

python manage.py flush --noinput;
python manage.py migrate;
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').delete(); User.objects.create_superuser('admin', '', 'test')" | python manage.py shell
echo "from django.contrib.auth.models import User; User.objects.filter(username='test').delete(); User.objects.create_user('test', '', 'test')" | python manage.py shell
python manage.py runscript polls_testdata;
python manage.py runscript socialaccount_testdata;
python manage.py test;
exit;