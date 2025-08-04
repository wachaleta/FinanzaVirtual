from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

#Importar LIbresrías o Paquetes para Login/Logout:
from django.views.generic import FormView, RedirectView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token

from django.views.decorators.http import require_http_methods


def home(request):
    return redirect("/Crear_Transaccion/0")

@login_required
def transacciones(request, id=0):

    return render(request, "transacciones/crear_transaccion.html")

def vue(request):

    return render(request, "index.html")

@login_required
def ver_transacciones(request, id=0):

    return render(request, "transacciones/ver_transacciones.html")

@login_required
def modificar_transacciones(request, transaccion="", id=0):

    return render(request, "transacciones/modificar_transaccion.html")

@login_required
def modificar_transferencia(request, id=0):

    return render(request, "transacciones/modificar_transferencia.html")

@login_required
def perfiles(request):

    return render(request, "perfiles/ver_perfiles.html")

@login_required
def cuentas(request):

    return render(request, "cuentas/ver_cuentas.html")

@login_required
def categorias(request):
    return render(request, "categorias/ver_categorias.html")

@login_required
def transacciones_programadas(request):
    return render(request, "transacciones/transacciones_programadas.html")

@login_required
def prueba(request):
    return render(request, "prueba/prueba.html")

class Logout(RedirectView):

    url = '/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(Logout, self).get(request, *args, **kwargs)

class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self, request,  *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            auth_login(self.request, form.get_user())
            return super(Login, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        return context
