from django.shortcuts import render,redirect 
from Gestion.models import Cliente, Empleado,Vehiculo
from Gestion.forms import Buscar_empleadoform




def Inicio(request):
    return render(request, "inicio.html")








#Formulario para agregar nuevos clientes
def formulario_cliente(request):
    if request.method == "POST":
        nuevocliente = Cliente(nombre = request.POST["nombre"],apellido =request.POST["apellido"], dni = request.POST["dni"])
        nuevocliente.save()

        return render (request, "inicio.html")
    return render(request,"formulariocliente.html")



#Formulario para agregar nuevos empleados
def formulario_empleado(request):
    if request.method == "POST":
        nuevoempleado = Empleado(nombre = request.POST["nombre"],apellido =request.POST["apellido"], dni = request.POST["dni"])
        nuevoempleado.save()

        return render (request, "inicio.html")
    return render(request,"formulario_empleado.html")


#Formulario para agregar vehiculos
def formulario_vehiculo(request):
    if request.method == "POST":
        nuevovehiculo = Vehiculo(tipo = request.POST["tipo"],marca =request.POST["marca"], modelo = request.POST["modelo"],precio = request.POST["precio"],estado = request.POST["estado"])
        nuevovehiculo.save()

        return render (request, "inicio.html")
    return render(request,"formulario_vehiculo.html")




def busqueda_empleado(request):
    if request.method == "POST":

        mi_formulario = Buscar_empleadoform(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            empleado = Empleado.objects.filter(nombre__icontains=informacion["nombre"])
            return render(request,"mostrar_empleados.html", {"empleado":empleado})
    else:
        mi_formulario = Buscar_empleadoform()
    
    return render(request, "busqueda_empleado.html",{"mi_formulario":mi_formulario})


