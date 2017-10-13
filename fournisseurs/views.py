# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def indexFournisseurs(request):
    return render(request,"indexF.html")

def detail(request):
    return render(request,"detail.html")

