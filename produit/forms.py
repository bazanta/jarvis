from django import forms
from .models import Commentaire

class ProduitForm(forms.Form):
    quantite = forms.IntegerField(label='Quantites', min_value=0)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Commentaire
        fields = ('text',)