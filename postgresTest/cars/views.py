from django.shortcuts import render, redirect
from cars.models import Car, Driver
from .forms import UserForm

def car_detail(request, pk):
    owner_obj = Driver.objects.get(pk=pk)
    car_objs = Car.objects.filter(owner_id=owner_obj.id)
    context = {
        "vehicles": car_objs,
        "drivers": owner_obj,
    }
    return render(request, "car_detail.html", context)

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})
