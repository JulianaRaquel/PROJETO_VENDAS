from django.contrib import admin
from .models import Users, Estado, Endereco
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth import admin as admin_auth_django


@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Informações Pessoais', {'fields': ("cpf", "telefone")}),
    )

admin.site.register(Estado)
admin.site.register(Endereco)
