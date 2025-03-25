from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    #configurando parâmetros na URL
    search = request.GET.get('search')

    #Query set do Django
    if search:
        cars = cars.filter(model__icontains=search)

    #Fazendo o render da View
    return render(
        request,
        'cars.html',
        {'cars': cars}
        )


