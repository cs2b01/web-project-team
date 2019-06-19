from django import forms
from questionsanswers.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _


#TODO: email must be unique.

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm,  self).__init__(*args, **kwargs)

        self.fields['username'].help_text   = "Información requerida. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ están permitidos."
        self.fields['email'].help_text      = "Esta información solo la podrás ver tú."
        self.fields['first_name'].help_text = "Esta información será mostrada a todos los usuarios."
        self.fields['last_name'].help_text  = "Esta información será mostrada a todos los usuarios."
        self.fields['password1'].help_text  = ( "<p> Tu contraseña debe respetar los siguientes criterios:</p>" + "<ul>" + "<li>No puede ser tan similar a tu otra información personal.</li>" + "<li>Debe contener al menos 8 caracteres.</li>" + "<li>No puede ser una contraseña comúnmente usada.</li>" + "<li>No puede contener solo números.</li>" + "</ul>")
        self.fields['password2'].help_text  = "Ingrese la misma clave que la anterior."

        self.fields['username'].label   = "Nombre de usuario"
        self.fields['email'].label      = "Correo electrónico"
        self.fields['first_name'].label = "Nombre(s)"
        self.fields['last_name'].label  = "Apellido(s)"
        self.fields['password1'].label  = "Contraseña"
        self.fields['password2'].label  = "Confirmar contraseña"

        self.error_messages = {
            'password_mismatch': _("Las dos contraseñas no son iguales.")
            }
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
