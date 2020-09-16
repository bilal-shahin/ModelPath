from django import  forms
import modelisation.models
from django.core import validators


class SearchMetabolitesForm(forms.Form):
    search_field = forms.CharField(label="",widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Search ID, name, formula or InChiKey'}
    ))

class SearchReactionsForm(forms.Form):
    reactions_id = forms.CharField(required=False, label="id", widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'ID/name'}
    ))
    reactions_ec_number = forms.CharField(required=False, label="ec_number", widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'EC_number'}
    ))
    reactions_substrates = forms.CharField(required=False, label="substrates", widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'substrates'}
    ))
    reactions_products = forms.CharField(required=False, label="products", widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'products'}
    ))
    reactions_models = forms.CharField(required=False, label="model", widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'model ID'}
    ))

    def clean(self):
        data = super().clean()
        if sum([len(data[x]) for x in self.fields.keys()])==0:
            raise forms.ValidationError('No field has been filled.')

