from django.contrib import admin
from enlaces.models import Enlace

# Parte del tercer parcial
class EnlaceAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'url', 'fecha')

admin.site.register(Enlace, EnlaceAdmin)