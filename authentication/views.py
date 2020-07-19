# -*- encoding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, FormView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings
from django.http import *
from .forms import LoginForm


class LoginViews(FormView):

    template_name = 'login.html'
    form_class = LoginForm

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['errors'] = kwargs.get('errors', form.errors)
        return self.render_to_response(context)

    def form_valid(self, form, *args, **kwargs):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        if self.request.POST and 'signup' in self.request.POST:
            email = form.cleaned_data.get("email")
            new_user = User.objects.create_user(username, email, password)
            new_user.save()
        #Auth
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            form._errors = 'Invalid credentials'
            return self.form_invalid(form)


class LogoutView(TemplateView):

    template_name = 'login.html'

    def get(self, request, **kwargs):
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

#EOF
