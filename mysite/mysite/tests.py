# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


def create_user(username='test'):
    """
    Creates user object for testing
    """
    return User.objects.create_user(username, password=username)


class HomePageViewTests(TestCase):
    def test_home_context(self):
        response = self.client.get(reverse('home'))
        self.assertTrue(response.context['home'] == 'active')


class UserProfileViewTests(TestCase):
    def test_userprofile_context(self):
        u = create_user()
        self.client.login(**{'username': 'test', 'password': 'test'})
        response = self.client.get(reverse('profile'))
        self.assertTrue(response.context['profile'] == 'active')
        res_user = response.context['userprofile']['user']
        self.assertTrue(res_user == u)

    def test_userprofile_password_update(self):
        u = create_user()
        self.client.login(**{'username': 'test', 'password': 'test'})
        response = self.client.get(reverse('profile_update'))
        self.assertTrue(response.context['profile'] == 'active')
        res_user = response.context['userprofile']['user']
        self.assertTrue(res_user == u)
        print response.context
