from django.contrib import admin
from django_dynamic_admin_forms.admin import DynamicModelAdminMixin
from .models import Almacen, MovimientoInventario, TipoMovimiento

@admin.register(TipoMovimiento)
class TipoMovimientoAdmin(admin.ModelAdmin):
    pass

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'codigo') 
    

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(DynamicModelAdminMixin, admin.ModelAdmin):
    fields = ('tipo', 'almacen', 'cantidad')
    dynamic_fields = ('tipo', 'almacen')
    # autocomplete_fields = ('almacen',)
    
    def get_dynamic_almacen_field(self, data: dict):
        queryset = Almacen.objects.all()
        options = data.get('almacen')
        hidden = True
        
        if data.get('tipo'):
            if data.get('tipo').nombre == 'TRANSFERENCIA':
                print('transferencia')
                queryset = Almacen.objects.filter(nombre__icontains='transferencia')
                hidden = False
            if data.get('tipo').nombre == 'ENTRADA':
                queryset = Almacen.objects.filter(nombre__icontains='entrada')
                hidden = False
            if data.get('tipo').nombre == 'SALIDA':
                queryset = Almacen.objects.filter(nombre__icontains='salida')
                hidden = False
            
        return queryset, options, hidden