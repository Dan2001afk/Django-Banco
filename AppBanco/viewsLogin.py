from django.shortcuts import *
from django.views import *

from .formscliente import ClienteForm
from .forms import *

#login
from .models import *

from django.contrib.auth import *
from django.views import *
from .forms import *
from django.utils.decorators import *
from django.views.decorators.csrf import *
from typing import Any
from django.contrib import messages
import json


""" class RegistrasUsuariosView(View):
    def get(self, request):
        form=UserForm()
        return render(request, 'RegistroU.html',{'form':form})
    
    def post(self, request):
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion')
        return render(request, 'iniciar_sesion',{'form':form})
     """
"""  """

class RegistrarUsuarioView(View):
    template_name = 'login.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = UserForm()  # Definir form con un valor predeterminado
        if request.method == 'POST':
            print("en el metodod")
            #if request.headers.get('content-type') == 'application/json':
            if 'application/json' in request.headers.get('content-type', ''):
                print("en el json")
                self.handle_flutter_data(request)
            else:
                print("no json")
                print(form.is_valid())
                form = UserForm(request.POST)
                
                if form.is_valid():
                    form.save()
                    
                    messages.success(request, 'Usuario registrado correctamente desde formulario HTML.')
                    return redirect('iniciar_sesion')
                else:
                    messages.error(request, 'Error al registrar el usuario desde formulario HTML.')
        else:
            print("no metodo")
            form = UserForm()
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def handle_flutter_data(self, request):
        try:
            data = json.loads(request.body)
            print("Datos recibidos desde Flutter:")
            print(data)  # Imprime los datos recibidos desde Flutter
            form = UserForm(data)
            if form.is_valid():
                print("Datos válidos:")
                print(form.cleaned_data)  # Imprime los datos validados por el formulario
                form.save()
                messages.success(request, 'Usuario registrado correctamente desde Flutter.')
            else:
                print("Errores en el formulario:")
                print(form.errors)  # Imprime los errores de validación del formulario
        except json.JSONDecodeError:
            messages.error(request, 'Error en los datos enviados desde Flutter.')
    




class IniciarSesionView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'iniciosesion.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)

                # Verificar el rol del usuario y redirigir en consecuencia
                if user.rol == 'cliente':
                    try:
                        Documento = user.documento_id
                        print("DDDDDDDDDD"),Documento

                        cliente = Cliente.objects.get(Documento=Documento)
                        if request.method == 'POST' and 'editar' in request.POST:
                            print("Entrando a cliente POST")
                            cliente_form=ClienteForm(request.POST, instance = cliente)
                            if cliente_form.is_valid():
                                cliente_form.save()
                                messages.success(request,'cambios guardados correctamente')
                                return redirect('Clientes')  # Redirigir a la página de clientes
                            else:
                                cliente_form = ClienteForm(instance=cliente)
                            return render(request, "cliente.html", {'cliente':cliente, 'form':cliente_form})
                    except Cliente.DoesNotExist:
                        messages.error(request, 'no se encontraron los datos.')
                else:
                    return redirect('frmempleado')  # Redirigir a otra página para otros roles
            form.add_error(None, 'Credenciales inválidas. Por favor, intenta nuevamente.')
        return render(request, 'iniciosesion.html', {'form': form})
    
def frmcliente(request):
     return render(request,"cliente.html")
def frmempleado(request):
     return render(request,"empleado.html")




