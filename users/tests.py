# -*- coding: utf-8 -*-
import random
import string

from django.test import TestCase
from django.core.urlresolvers import reverse


# Create your tests here.
def get_random_str(size):
    str = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))
    return str

def get_random_username(username_size):
    str = get_random_str(username_size)
    return str

def get_random_email(email_size):
    str = get_random_str(email_size)
    return str + '@qq.com'

def get_invalid_email(email_size):
    str = get_random_str(email_size)
    return str + '@sohu.com'

def get_random_password(password_size):
    str = get_random_str(password_size)
    return str

class SignupViewTests(TestCase):
    def test_repeat_email(self):
        username = get_random_username(10)
        password = get_random_str(10)
        email = get_random_email(10)

        post_param = {
            'username': username,
            'password': password,
            'email': email,
        }
        response = self.client.post(reverse('users:signup'), post_param)
        self.assertEqual(response.status_code, 200)

        post_param['username'] = get_random_username(10)
        response = self.client.post(reverse('users:signup'), post_param)
        self.assertContains(response, u"邮箱已注册", status_code=200)

    def test_repeat_username(self):
        username = get_random_username(10)
        password = get_random_str(10)
        email = get_random_email(10)

        post_param = {
            'username': username,
            'password': password,
            'email': email,
        }
        response = self.client.post(reverse('users:signup'), post_param)
        self.assertEqual(response.status_code, 200)

        post_param['email'] = get_random_email(10)
        response = self.client.post(reverse('users:signup'), post_param)
        self.assertContains(response, u'用户名已存在', status_code=200)


class LoginViewTest(TestCase):
    def test_normal_login(self):
        username = get_random_username(10)
        password = get_random_password(10)

        post_param = {
            'username': username,
            'password': password,
        }
        response = self.client.post(reverse('users:login'), post_param)
        self.assertEqual(response.status_code, 200)


