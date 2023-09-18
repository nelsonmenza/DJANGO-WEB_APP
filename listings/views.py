from django.shortcuts import HttpResponse, get_object_or_404, render

from .models import Band


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band": band})
