# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from .forms import PersonInfoForm
from .models import PersonInfo
# Create your views here.

class PersonConfigView(View):
    form_class = PersonInfoForm
    template_name = 'personinfo/config.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        #form = self.form_class(request.POST)
        user = request.user

        if form.is_valid():
            love = form.cleaned_data['love']
            sex = form.cleaned_data['sex']
            head_img = form.cleaned_data['head_img']

            try:
                personinfo = PersonInfo.objects.get(user=user)
            except PersonInfo.DoesNotExist:
                personinfo = PersonInfo(user=user, love=love, sex=sex)
            
            personinfo.head_img = head_img
            personinfo.save()
            print "redirect to main page"
        
        return render(request, self.template_name, {'form': form})
        

