from django import forms

class ProduitForm(forms.Form):
    quantite = forms.IntegerField(label='Quantites', min_value=0)