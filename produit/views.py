from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from models import *
from forms import *
from panier.views import *

def indexProduit(request):
    produits = FicheProduit.objects.all()

    # Gestion de la pagination
    paginator = Paginator(produits, 9) 
    page = request.GET.get('page')
    try:
        produits = paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)

    return render(request,'indexProduit.html', {'produits' : produits})

def addProductPanier(request, id):
    add_to_cart(request, id, 1)
    messages.success(request, 'Ajout panier OK')
    return redirect('indexProduit')

def detailProduit(request, id):
    produit = FicheProduit.objects.get(id=id)

    formCommentaire = CommentForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            # Ajout du produit au panier
            qte = form.cleaned_data['quantite']
            add_to_cart(request, id, qte)
            # Redirection
            messages.success(request, 'Ajout panier OK')
            return redirect('detailProduit', id=id)
    else:
        form = ProduitForm(initial={'produit': id})

    return render(request,'detailProduit.html', {'produit' : produit, 'form' : form, 'formCommentaire' : formCommentaire})

@login_required
def addCommentaire(request, id):
    produit = FicheProduit.objects.get(id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Ajout du commentaire
            comment = form.save(commit=False)
            comment.produit = produit
            comment.auteur = request.user
            comment.save()
            # Redirection
            messages.success(request, 'Commentaire ajoute.')
            return redirect('detailProduit', id=id)
    messages.error(request, 'Commentaire incorrecte.')
    return redirect('detailProduit', id=id)