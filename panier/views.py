# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from cart.cart import Cart
from produit.models import FicheProduit
from produit.forms import *

def add_to_cart(request, product_id, quantity):
    product = FicheProduit.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.prix, quantity)

def update_from_cart(request, product_id, quantity):
    product = FicheProduit.objects.get(id=product_id)
    cart = Cart(request)
    cart.update(product, quantity, product.prix)

def delete_from_cart(request, product_id):
    product = FicheProduit.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def panier(request):
    form = ProduitForm()
    return render(request,'panier.html', {'cart':Cart(request),'form':form})

def panierSup(request, id):
    delete_from_cart(request, id)
    return redirect('panier') 

def panierModif(request, id):
    form = ProduitForm(request.POST)
    if form.is_valid():
        qte = form.cleaned_data['quantite']
        update_from_cart(request, id, qte)
    return redirect('panier') 
