# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View
from shopcart import ShopCart

# Create your views here.
class PaymentPendingView(View):
    template_name = 'payment/checkout.html'
    
    def check_product(self, product_id):
        pass
    
    def modify_inventory(self):
        pass

    def post(self, request, *args, **kwargs):
        cart_items = request.POST.get('data', [])
        user = request.user
        cart_obj = ShopCart.get_cart(user)

        for item in cart_items:
            #-----should check cart
            detail = {
                title: 'title',
                price: 'price',
                img_url: 'img_url',
            }
            ShopCart.add_item_to_cart(cart_obj, item['id'], item['qty'], detail)

        cart_obj.save()
        return True

