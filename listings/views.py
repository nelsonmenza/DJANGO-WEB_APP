from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import BandForm, ContactUsForm
from .models import Band


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band": band})


def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via Merchex Contact Us form',
                      message=form.cleaned_data['message'],
                      from_email=form.cleaned_data['email'],
                      recipient_list=['nelsonmenza30@gmail.com'])

            return redirect("email-sent")
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
            return redirect("band-detail", band.id)
    else:
        form = BandForm
    return render(request, "listings/band_create.html", {"form": form})
