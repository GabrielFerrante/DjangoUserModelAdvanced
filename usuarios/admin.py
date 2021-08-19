from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioChangeForm, CustomUsuarioCreationForm, UserChangeForm
from .models import CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreationForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ['first_name', 'last_name', 'email', 'fone', 'cpf', 'is_staff']
    #Dados de cadastro do usuário
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone', 'cpf')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields':  ('last_login', 'date_joined')}),
    )
