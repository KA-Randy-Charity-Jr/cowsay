from django.shortcuts import render

# Create your views here.
from cowsay_app.models import Cowsay
from cowsay_app.forms import CowsayForm



def cowsay_view(request):
    theinput= CowsayForm()
    return render(request,"cowsay.html",{"form":theinput})