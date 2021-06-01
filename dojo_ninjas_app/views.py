from django.shortcuts import render, redirect
from .models import Dojos, Ninjas

def index(request):
    #retrieve all dojos and ninjas from database to display on main route.
    context = {
        "all_dojos": Dojos.objects.all(),
        "all_ninjas": Ninjas.objects.all(),
    }
    return render(request, "index.html", context)

def dojos(request):
    #create new dojo record using data from POST. 
    new_dojo = Dojos.objects.create(name= request.POST["name"], city= request.POST["city"], state= request.POST["state"])
    return redirect("/")

def ninjas(request):
    #retrieve id of selected record from POST.
    dojo= Dojos.objects.get(id=int(request.POST['dojo']))
    #include id of record from dojo model to add as foreign key dojo to create new record to add to ninja model.
    new_ninja = Ninjas.objects.create(first_name= request.POST["firstname"], last_name= request.POST["lastname"], dojo= dojo)
    return redirect("/")

