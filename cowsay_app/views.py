from django.shortcuts import render

# Create your views here.
from cowsay_app.models import Cowsay,History
from cowsay_app.forms import CowsayForm
import subprocess




def cowsay_view(request):
   
    g= ""
    if request.method == "POST":
        form = CowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            string = data.get("cowsay")
            f = subprocess.run(["cowsay", string], capture_output=True)
            g = f.stdout.decode()
            History.objects.create(string=string)
    theinput= CowsayForm()
    return render(request, "cowsay.html", {"form": theinput, "f": g})
    


def history_view(request):
    the_strings = History.objects.all().order_by("-id")[0:10]

    return render(request,"history.html",{"strings":the_strings})