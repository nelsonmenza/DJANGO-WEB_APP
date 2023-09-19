from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import BandForm, ContactUsForm, ListingsForm
from .models import Band, Listings


def index(request):
    bands = Band.objects.all()
    listings = Listings.objects.all()
    return render(request, "listings/index.html", {"bands": bands,
                                                   "listings": listings})


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})


def listing_list(request):
    listings = Listings.objects.all()
    return render(request, "listings/listing_list.html", {"listings": listings})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band": band})


def listing_detail(request, id):
    listing = Listings.objects.get(id=id)
    return render(request, "listings/listing_detail.html", {"listing": listing})


def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via Merchex Contact Us form',
                      message=form.cleaned_data['message'],
                      from_email=form.cleaned_data['email'],
                      recipient_list=['nelsonmenza30@gmail.com'])
            return redirect("email_sent")
    else:
        form = ContactUsForm()
        return render(request, "listings/contact.html", {"form": form})


def confirmation(request):
    return render(request, "listings/confirmation.html")


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect("band_detail", band.id)
    else:
        form = BandForm
    return render(request, "listings/band_create.html", {"form": form})


def listings_create(request):
    if request.method == "POST":
        form = ListingsForm(request.POST)
        if form.is_valid():
            form.save()
            listing = form.save()
            return redirect("band_list", listing.id)
    else:
        form = ListingsForm
    return render(request, "listings/listings_create.html", {"form": form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect("band_detail", band.id)
    else:
        form = BandForm(instance=band)
    return render(request, "listings/band_update.html", {"form": form})


def listing_update(request, id):
    listing = Listings.objects.get(id=id)
    if request.method == "POST":
        form = ListingsForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("listing_detail", listing.id)
    else:
        form = ListingsForm(instance=listing)
    return render(request, "listings/listing_update.html", {"form": form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == "POST":
        band.delete()
        return redirect("band_list")

    return render(request, "listings/band_delete.html", {"band": band})


def listing_delete(request, id):
    band = Listings.objects.get(id=id)
    if request.method == "POST":
        Listings.delete()
        return redirect("listing_list")

    return render(request, "listings/listing_delete.html", {"band": band})
