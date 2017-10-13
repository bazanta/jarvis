# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from cart.cart import Cart
from produit.models import FicheProduit

def add_to_cart(request, product_id, quantity):
    product = FicheProduit.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.prix, quantity)

def remove_from_cart(request, product_id):
    product = FicheProduit.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def panier(request):
    return render_to_response('panier.html', dict(cart=Cart(request)))