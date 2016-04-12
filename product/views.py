from django.shortcuts import render
from django.views.generic import View
from django.forms import formset_factory

from image.forms import ImageForm
from .forms import ProductForm
from .models import Product
from .models import Attributes

# Create your views here.
class ProductConfigView(View):
    form_class = ProductForm
    image_form = ImageForm
    template_name = 'product/config.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        ImageFormSet = formset_factory(self.image_form)
        
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
            product = Product(title=title, price=price, score=score, description=description)
            product.save()
            self.save_all_image(image_form_set, product)
            print "ok-----------"

        return render(request, self.template_name, {'form': form, 'image_form_set': ImageFormSet()})

    def save_all_image(slef, form_set, product):
        for item in form_set:
            image = item.cleaned_data['image']
            description = item.cleaned_data['img_description']
            Image(product=product, image=image, description=description)
            image.save()

            
