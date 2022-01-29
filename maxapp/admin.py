from django.contrib import admin
from maxapp.models import Coche, Imagen

# Register your models here.

class CocheImagenAdmin(admin.StackedInline):
    model = Imagen
    min_num = 1
    max_num = 10
    extra = 1

@admin.register(Coche)
class CocheAdmin(admin.ModelAdmin):

    list_display = [
        'placa',
        'marca',
        'modelo',
        'cantidad',
        'precio'
    ]

    inlines = [CocheImagenAdmin]
    search_fields = ['nombre', 'marca']

    class Meta:
        model = Coche
