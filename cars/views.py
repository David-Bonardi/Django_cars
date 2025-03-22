from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    #Query set do Django
    cars = Car.objects.filter(model='Santana')

    #Fazendo o render da View
    return render(
        request,
        'cars.html',
        {'cars': cars}
        )
