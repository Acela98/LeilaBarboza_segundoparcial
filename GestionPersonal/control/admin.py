from django.contrib import admin


from .models import Empleado
from .models import Jornada

admin.site.register(Empleado)
admin.site.register(Jornada)


