# -*- coding: utf-8 -*-
import json
import pdb
from decimal import *

from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import Group
from django.forms import formset_factory
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import six
from django.forms.models import model_to_dict
from django.core import serializers

from image.forms import ImageForm
from .forms import ProductForm
from image.models import Image
from .models import Product
from inventory.models import Inventory


# Create your views here.
class ProductAddView(View):
    form_class = ProductForm
    image_form = ImageForm
    template_name = 'product/addproduct.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        ImageFormSet = formset_factory(self.image_form, extra=2, max_num=2)
        
        return render(request, self.template_name, {'form': form, 'image_form_set': ImageFormSet()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        ImageFormSet = formset_factory(self.image_form)
        image_form_set = ImageFormSet(request.POST, request.FILES)
        
        if image_form_set.is_valid() and form.is_valid():
            title = form.cleaned_data['title']
            price = form.cleaned_data['price']
            score = form.cleaned_data['score']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']

            product = Product(title=title, price=price, score=score, description=description, category=category)
            product.save()
            self.save_inventory(form, product)
            self.save_all_image(image_form_set, product)
            #update redis
            Product.update_items_zrange(category, product)

        return render(request, self.template_name, {'form': form, 'image_form_set': ImageFormSet()})

    def save_inventory(self, form, product):
        inventory_qty = form.cleaned_data['inventory_qty']
        Inventory.create_inventory(product, inventory_qty)

    def save_all_image(slef, form_set, product):
        for item in form_set:
            image = item.cleaned_data.get('image', None)
            description = item.cleaned_data.get('img_description', None)
            
            if image is None or description is None:
                continue

            img_obj = Image(product=product, image=image, description=description)
            img_obj.save()


def custom_perms(perm, group, app, login_url=None, raise_exception=True):
    """
    """
    def check_perms(user):
        a = user
        if isinstance(perm, six.string_types):
            perms = [perm, ]
        else:
            perms = perm

        if isinstance(group, list):
            groups = group
        else:
            groups = [group, ]

        appname = app + '.'
        perm_list = [appname + item for item in perms]
        
        for groupname in groups:
            group_obj = Group.objects.get(name=groupname)
            group_perms = [appname + item.codename for item in group_obj.permissions.all()]
            perm_list.extend(group_perms)

        if user.has_perms(perm_list):
            return True

        return False

        if raise_exception:
            raise PermissionDenied

        return False
    return user_passes_test(check_perms, login_url=login_url)

class ProductChangeView(View):
    form_class = ProductForm
    image_form = ImageForm
    template_name = 'product/changeproduct.html'

    #@method_decorator(custom_perms("delete_product", ['config_product'], 'product'))
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pk = int(kwargs['pk'])
        product = get_object_or_404(Product, pk=pk)
        print '++++++++++++ok'
        form = self.form_class(model_to_dict(product))
        images = product.image_set.all()
        return render(request, self.template_name, {'product': product,
                                                    'form': form, 'images': images})

    def modify_image(self, pk, uploadedfile, description):
        try:
            pk = int(pk)
            image = Image.objects.get(pk=pk)
            image.image = uploadedfile
            image.description = description
            image.save()
        except Image.DoesNotExist:
            print "---------error_______"
            pass

    def add_image(self, uploadedfile, description, product):
        u'''
        add new image
        '''
        img = Image(product=product, description=description)
        img.image = uploadedfile
        img.save()

    def delete_image(self, pk):
        try:
            pk = int(pk)
            Image.objects.get(pk=pk).delete()
        except Image.DoesNotExist:
            print '------------ error'
            pass
    
    def get_img_key(self, key_list):
        img_key = '-'.join(list(['img', key_list[1], key_list[2] ]))
        return img_key

    def check_key(self, key, request, product):
        key_list = key.split('-')

        if len(key_list) != 3:
            return  0

        if 'des' not in key:
            return 0

        if key_list[1] == 'old':
            #no change
            return 1

        if key_list[1] == 'modify':
            pk = key_list[2]
            img_key = self.get_img_key(key_list)
            uploadedfile = request.FILES.get(img_key, None)
            description = request.POST.get(key, None)
            self.modify_image(pk, uploadedfile, description)
            return 1

        if key_list[1] == 'new':
            img_key = self.get_img_key(key_list)
            uploadedfile = request.FILES.get(img_key, None)
            description = request.POST.get(key, None)
            self.add_image(uploadedfile, description, product)
            return 1

        if key_list[1] == 'delete':
            pk = key_list[2]
            self.delete_image(pk)
            return -1

        return False

    def handle_images(self, request, product, max=5):
        #pairs
        count = 0
        for (key, val) in request.POST.items():
            count = count + self.check_key(key, request, product)

        if count > 5:
            return u'max-----images'

        return None

    def post(self, request, *args, **kwargs):
        pk = int(kwargs['pk'])
        print '---------%r' % pk
        form = self.form_class(request.POST)
        images = request.FILES

        if form.is_valid():
            product = get_object_or_404(Product, pk=pk)
            product.title = form.cleaned_data.get('title', '')
            product.price = form.cleaned_data.get('price', '')
            product.score = form.cleaned_data.get('score', '')
            product.category = form.cleaned_data.get('category', '')
            product.description = form.cleaned_data.get('description', '')

            product.save()

            if self.handle_images(request, product) != None:
                return HttpResponse('out over max')
            else:
                return HttpResponse('ok-----------')

        return HttpResponse('error')


class ProductView(View):
    def get(self, request, *args, **kwargs):
        self.page = int(kwargs.get('page', 0))
        items = Product.get_page_items(self.page, 10, self.category)
        return render(request, self.template_name, {'items': items, 'title': self.title})


class ProductVideoView(ProductView):
    category = 'Video'
    template_name = 'product/video.html'
    title = u'商城-影音'


class ProductComputersView(ProductView):
    category = 'Computers'
    template_name = 'product/computers.html'
    title = u'商城-电脑'


class ProductDressView(ProductView):
    category = 'Dress'
    template_name = 'product/dress.html'
    title = u'商城-服装'


class ProductGroceryView(ProductView):
    category = 'Grocery'
    template_name = 'product/grocery.html'
    title = u'商城-食品'


class ProductBooksView(View):
    template_name = 'product/books.html'

    def get(self, request, *args, **kwargs):
        self.page = int(kwargs.get('page', 0))
        books = Product.get_books(self.page, 10, 'Book')

        return render(request, self.template_name, {'books': books})


class ProductTopView(View):
    def get(self, request, *args, **kwargs):
        self.page = 1
        tops = Product.get_items_zrange(self.category, self.page, 10)
        products = Product.get_top_products(tops)
        return render(request, self.template_name, {'products': products})

    def post(self, request, *args, **kwargs):
        pass


class ProductTopBooksView(ProductTopView):
    category = 'Book'
    template_name = 'product/topbooks.html'
    title = u'销量排行榜'


class ProductKeyView(View):
    def get(self, request, *args, **kwargs):
        self.key = kwargs['key']
        self.page = kwargs['page']
        products = Product.get_items_by_key(self.key, self.page, 10)

        json_data = {
            'products': list(products.values())
        }
        #json_data = serializers.serialize('json', json_data)
        
        return JsonResponse(json_data)


