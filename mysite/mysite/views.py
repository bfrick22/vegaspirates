# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

from .forms import UserProfileForm


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


class UserProfileView(TemplateView):
    template_name = "profile.html"


class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name_suffix = '_update_form'
    success_url = '../profile/'

    def get_object(self, queryset=None, **kwargs):
        return User.objects.get(id=self.request.user.id)