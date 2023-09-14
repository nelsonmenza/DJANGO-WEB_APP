from django.shortcuts import HttpResponse, render

from .models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands": bands})
