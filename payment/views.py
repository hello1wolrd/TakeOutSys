# -*- coding: utf-8 -*-
import pdb

from django.shortcuts import render
from django.views.generic import View
from shopcart.models import ShopCart

# Create your views here.
class PaymentPendingView(View):
    template_name = 'payment/checkout.html'
    
    def check_product(self, product_id):
        pass
    
    def modify_inventory(self):
        pass

    def generate_order(self):
        #购物车永远只有一个
        #每次生成一个历史订单， 数据是购物车数据+额外信息
        #购物车可以临时保存15分钟， 这15分钟可以保证， 已经
        #购买的物品不会被回收系统
        pass

    def post(self, request, *args, **kwargs):
        cart_items = request.POST.get('data', [])
        user = request.user
        user.id = 1111
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

        pdb.set_trace()
        return render(request, self.template_name, {})

