# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from config.celery import app
from datetime import timedelta
from django.core.signing import TimestampSigner

def get_verify_link(user_pk):
    verify_link = u'http://localhost:8000/verify/'
    signer = TimestampSigner()
    value = signer.sign(str(user_pk))

    return verify_link + value


@app.task
def add(a, b):
    return a + b


@app.task
def send_verify_email(email, user_pk):
    print '-----------------taks----------------------------'
    email = '504888883@qq.com'
    verify_link = get_verify_link(user_pk)
    send_mail(u'验证邮箱', verify_link, 'testtakeout@163.com', [email], fail_silently=False)
