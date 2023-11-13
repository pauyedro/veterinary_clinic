from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ClienteForm, LocalidadForm, PaisForm, ProvinciaForm, MascotaForm, Tipo_DocForm
from .models import Cliente, Localidad, Pais, Provincia, Mascota, Tipo_Doc



# Create your views here.


#Landing page
def acerca_de(request, template_name="veterinaria/acerca_de.html"):

    return render(request, template_name)


#LISTADOS


def localidades(request, template_name="veterinaria/localidades.html"):
    localidades_list = Localidad.objects.all()
    dato = {"localidades": localidades_list}
    return render(request, template_name, dato)


def clientes(request, template_name="veterinaria/clientes.html"):
    clientes_list = Cliente.objects.all()
    dato = {"clientes": clientes_list}
    return render(request, template_name, dato)


def provincias(request, template_name="veterinaria/provincias.html"):
    provincias_list = Provincia.objects.all()
    paises = Pais.objects.all()
    dato = {"provincias": provincias_list, "paises": paises}
    return render(request, template_name, dato)


def detalle_cliente(request, pk, template_name="veterinaria/detalle_cliente.html"):
    cliente = Cliente.objects.get(id=pk)
    mascotas = Mascota.objects.filter(dueno=cliente.id)
    dato = {"cliente": cliente, "mascotas": mascotas}
    return render(request, template_name, dato)


#Formularios


def nueva_localidad(request, template_name="veterinaria/nueva_localidad.html"):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('localidades')
    else:
        form = LocalidadForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def nuevo_cliente(request, template_name="veterinaria/nuevo_cliente.html"):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('clientes')
    else:
        form = ClienteForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def tipo_doc(request, template_name="veterinaria/tipo_doc.html"):
    if request.method == 'POST':
        form = Tipo_DocForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('nuevo_cliente')
    else:
        form = Tipo_DocForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def nuevo_pais(request, template_name="veterinaria/nuevo_pais.html"):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('nueva_provincia')
    else:
        form = PaisForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def nueva_provincia(request, template_name="veterinaria/nueva_provincia.html"):
    if request.method == 'POST':
        form = ProvinciaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('nueva_localidad')
    else:
        form = ProvinciaForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def nueva_mascota(request, template_name="veterinaria/nueva_mascota.html"):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('clientes')
    else:
        form = MascotaForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def modificar_cliente(request, pk, template_name="veterinaria/nuevo_cliente.html"):
    cliente = Cliente.objects.get(id=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('clientes')
    datos = {'form': form}
    return render(request, template_name, datos)


def eliminar_cliente(request, pk, template_name="veterinaria/eliminar_cliente.html"):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    dato = {'form': cliente}
    return render(request, template_name, dato)


def modificar_localidad(request, pk, template_name="veterinaria/nueva_localidad.html"):
    localidad = Localidad.objects.get(id=pk)
    form = LocalidadForm(request.POST or None, instance=localidad)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('localidades')
    datos = {'form': form}
    return render(request, template_name, datos)


def eliminar_localidad(request, pk, template_name="veterinaria/eliminar_localidad.html"):
    localidad = Localidad.objects.get(id=pk)
    if request.method == 'POST':
        localidad.delete()
        return redirect('localidades')
    dato = {'form': localidad}
    return render(request, template_name, dato)


def modificar_provincia(request, pk, template_name="veterinaria/nueva_provincia.html"):
    provincia = Provincia.objects.get(id=pk)
    form = ProvinciaForm(request.POST or None, instance=provincia)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('provincias')
    datos = {'form': form}
    return render(request, template_name, datos)


def eliminar_provincia(request, pk, template_name="veterinaria/eliminar_provincia.html"):
    provincia = Provincia.objects.get(id=pk)
    if request.method == 'POST':
        provincia.delete()
        return redirect('provincias')
    dato = {'form': provincia}
    return render(request, template_name, dato)