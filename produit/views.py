# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from models import *

def indexProduit(request):
    produits = FicheProduit.objects.all()

    # Gestion de la pagination
    paginator = Paginator(produits, 3) 
    page = request.GET.get('page')
    try:
        produits = paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)

    return render(request,'indexProduit.html', {'produits' : produits})


def detailProduit(request, id):
    produit = FicheProduit.objects.get(id=id)
    return render(request,'detailProduit.html', {'produit' : produit})

