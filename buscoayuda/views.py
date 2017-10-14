from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse


from .models import TiposDeServicio, Trabajador, TrabajadorForm, UserForm


def index(request):
    trabajadores = Trabajador.objects.all()
    tipos_de_servicios = TiposDeServicio.objects.all()
    form_trabajador = TrabajadorForm(request.POST)
    form_usuario = UserForm(request.POST)

    context = {'trabajadores': trabajadores,
               'tipos_de_servicios': tipos_de_servicios,
               'form_trabajador': form_trabajador,
               'form_usuario': form_usuario,
               'base_url': settings.STATIC_URL}

    my_user = auth.get_user(request)

    if my_user.is_authenticated:
        context['user_name'] = trabajadores.filter(usuarioId=my_user).first().nombre
    # context = {'trabajadores': trabajadores, 'tipos_de_servicios': tipos_de_servicios,
    #            'form_trabajador': form_trabajador, 'form_usuario': form_usuario, 'base_url': settings.STATIC_URL}
    return render(request, 'buscoayuda/index.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, password=password)
        user.first_name = request.POST.get('nombre')
        user.last_name = request.POST.get('apellidos')
        user.email = request.POST.get('correo')
        user.save()

        nuevo_trabajador = Trabajador(nombre=request.POST['nombre'],
                                      apellidos=request.POST['apellidos'],
                                      aniosExperiencia=request.POST.get(
                                          'aniosExperiencia'),
                                      tiposDeServicio=TiposDeServicio.objects.get(
                                          pk=request.POST.get('tiposDeServicio')),
                                      telefono=request.POST.get('telefono'),
                                      correo=request.POST.get('correo'),
                                      imagen=request.FILES['imagen'],
                                      usuarioId=user
                                      )
        nuevo_trabajador.save()

    return HttpResponseRedirect('/')


def detalle_trabajador(request):
    return render(request, "buscoayuda/detalle.html")


def detail(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    return HttpResponse(serializers.serialize("json", [trabajador]))


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        messages.success(request, "Bienvenido al sistema {}".format(
            username), extra_tags="alert-success")
        return HttpResponseRedirect('/')
    else:
        messages.error(
            request, "¡El usuario o la contraseña son incorrectos!", extra_tags="alert-danger")
        return HttpResponseRedirect('/')
