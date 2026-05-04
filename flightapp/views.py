from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .models import *
from .forms import FlightForm


#ovaa funkcija ke go obrabotuva baranjeto za adresata /index.html
def index(request):
    all_flights = Flight.objects.all() #site letovi
    context = {"flights": all_flights,"page_title":"Flights Application"}
    return render (request,'index.html',context)

@login_required
def details(request,id): #id-to go prakjame kako parametar posle vo linkot {{% url 'details' flight.id %}}
    try:
        flight = Flight.objects.get(id=id) #go naogjame toj flight sto sakame da vidime details za nego...
    except Flight.DoesNotExist:
        return index(request)  #ako nema samo vrakjame redirect na index.html
    context = {'flight':flight}
    return render(request,'details.html',context)


@login_required
def addForm(request):
    if request.method == "POST":
        form  = FlightForm(request.POST,request.FILES)
        if form.is_valid():
            flight = form.save(commit=False) #da ne se zacuva vo baza uste..
            flight.user=request.user
            flight.save() # tuka se zacuvuva vo baza objektot flight
            return redirect('index')
    form = FlightForm()
    return render(request,'add_form.html',{'form':form})