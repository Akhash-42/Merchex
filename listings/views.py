from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.models import Band, Listing
from listings.forms import contactUsForm, BandForm, ListingForm
from django.core.mail import send_mail

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def about(request):
    return render(request,'listings/about.html')

def contact(request):
    if request.method == 'POST':
        form = contactUsForm(request.POST)
        if form.is_valid():
            send_mail(subject =
                      f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us form',
                      message = form.cleaned_data['message'],
                      from_email = form.cleaned_data['email'],
                      recipient_list=['admin@merchex.xyz']
                      )
            return redirect('email-sent')
    else:
        form = contactUsForm()
    return render(request,'listings/contact.html', {'form' : form})

def listings(request):
    titles = Listing.objects.all()
    return render(request,'listings/listings.html', {'titles':titles})

def band_detail(request, band_id):
    band = Band.objects.get( id = band_id)
    return render(request, 'listings/band_detail.html',{'band' : band})

def listing_detail(request, id):
    list = Listing.objects.get( id = id)
    # band = Band.objects.get(id =id)
    return render(request,'listings/listing_detail.html',{'list' : list})

def email(request):
    return render(request,'listings/email.html')

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail',band.id)
    else :
        form = BandForm()
    return render(request,'listings/band_create.html',{'form' : form})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('list-detail',band.id)
    else :
        form = ListingForm()
    return render(request,'listings/listing_create.html',{'form' : form})

def band_update(request,band_id):
    band = Band.objects.get(id = band_id)
    if request.method == 'POST':
        form = BandForm(request.POST,instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail',band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form' : form})

def listing_update(request,id):
    list = Listing.objects.get(id = id)
    if request.method == 'POST':
        form = ListingForm(request.POST,instance= list)
        form.save()
        return redirect('list-detail',id)
    else:
         form = ListingForm(instance= list)
    return render(request, 'listings/listing_update.html', {'form' : form})

def band_delete(request,band_id):
    band = Band.objects.get(id = band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band' : band})

def listing_delete(request,id):
    list = Listing.objects.get(id = id)
    if request.method == 'POST':
        list.delete()
        return redirect('list')
    return render(request, 'listings/listing_update.html', {'list' : list})