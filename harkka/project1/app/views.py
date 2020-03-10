from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car
from .forms import CarForm


def list_cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})

def create_car(request):
    form = CarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_cars')
    return render(request, 'cars-form.html', {'form': form})

def update_car(request, id=None):
    pass
    car = Car.objects.get(id=id)
    form = CarForm(request.POST or None, instance=car)

    if form.is_valid():
        form.save()
        return redirect(list_cars)
    return render(request, 'cars-form.html', {'form': form, 'car': car})

def delete_car(request, id=None):
    pass
    car = Car.objects.get(id=id)

    if request.method == 'POST':
        car.delete()
        return redirect('list_cars')
    return render(request, 'car-delete-confirm.html', {'car': car})


# Create your views here.
 