from django.shortcuts import render, redirect
from .forms import AddVehiculo
from .models import Vehiculo
import vehiculo.templates
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'index.html', {'vehiculos': vehiculos})

@permission_required('vehiculo.add_vehiculo')
def add(request):
    data = {'form': AddVehiculo()}
    
    if request.method == 'POST':
        form = AddVehiculo(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar')
        else:
            data["form"] = form
    return render(request, 'add.html', data)


@login_required
def listar(request):
    vehiculos = Vehiculo.objects.all()
    context = {
        "vehiculos": vehiculos
        }
    for vehiculo in vehiculos:
        if vehiculo.precio < 10000:
            vehiculo.condicion_precio = 'Bajo'
        elif vehiculo.precio >= 10000 and vehiculo.precio < 30000:
            vehiculo.condicion_precio = 'Medio'
        else:
            vehiculo.condicion_precio = 'Alto'
    
    return render(request, 'listar.html', context
                )