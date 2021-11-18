from django.shortcuts import render
from pyshorteners import Shortener

# Create your views here.
from django.conf import settings as conf_settings

def home(request):
    if request.method == "POST":
        url = request.POST.get("url")

        shortener = Shortener(api_key=conf_settings.ACCESS_TOKEN)
        surl = shortener.bitly.short(url)
        return render(request, "home/index.html", {"surl": surl})

    return render(request, "home/index.html")