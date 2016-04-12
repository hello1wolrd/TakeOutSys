# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.forms import formset_factory

from image.forms import ImageForm
from .forms import ProductForm
from image.models import Image
from .models import Product


# Create your views here.
class ProductConfigView(View):
    form_class = ProductForm
    image_form = ImageForm
    template_name = 'product/config.html'

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
            self.save_all_image(image_form_set, product)
            print "ok-----------"

        return render(request, self.template_name, {'form': form, 'image_form_set': ImageFormSet()})

    def save_all_image(slef, form_set, product):
        for item in form_set: 
            image = item.cleaned_data['image']
            description = item.cleaned_data['img_description']
            img_obj = Image(product=product, image=image, description=description)
            img_obj.save()


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

