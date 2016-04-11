# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import SignupForm, LoginForm
# Create your views here.


class SignupView(View):
    form_class = SignupForm
    template_name = 'users/signup.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        if form.is_valid():
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            #return HttpResponseRedirect('')
            config_url = reverse('profile:config')
            print "Redirect to TakeOut-index reverse"
            return HttpResponseRedirect(config_url)

        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class()

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print "Redirect to old user"

        return render(request, self.template_name, {'form': form})

