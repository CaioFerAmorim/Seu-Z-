from django.contrib import admin
from .models import Pessoa
from .models import Beneficiario
from .models import Voluntario

admin.site.register(Pessoa)
admin.site.register(Beneficiario)
admin.site.register(Voluntario)
