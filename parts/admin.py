from django.contrib import admin
from .models import Part

class PartAdmin(admin.ModelAdmin):
    list_display = ['id','nazwa', 'opis', 'ilość', 'kupione_od', 'dodane']
    search_fields = ['nazwa','opis']
admin.site.register(Part, PartAdmin)

# Register your models here.
