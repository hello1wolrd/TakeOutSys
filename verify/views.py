# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from datetime import timedelta
from django.core.signing import TimestampSigner
from django.contrib.auth.models import User
# Create your views here.

class VerifyView(View):
    template_name = 'verify/verify.html'

    def get(self, request, *args, **kwargs):
        verify_val = kwargs['pk']
        signer = TimestampSigner()
        try:
            value = signer.unsign(verify_val, max_age=timedelta(seconds=100))
        except SignaturExpired:
            msg = u'验证过期， 重新演奏'
            return render(request, self.template.name, {'msg': msg})
        else:
            pass

        pk = int(value)
        user = get_object_or_404(User, pk=pk)
        personinfo = user.personinfo
        personinfo.auth_mail = True
        personinfo.save()
        
        msg = u'验证通过'
        return render(request, self.template.name, {'msg': msg})




