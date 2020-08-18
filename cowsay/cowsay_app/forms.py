from django import forms
from cowsay_app.models import Cowsay



class CowsayForm(forms.Form):
    cowsay = forms.CharField(widget=forms.Textarea)