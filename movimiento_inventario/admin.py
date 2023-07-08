from django.contrib import admin
from django import forms
from .models import MovimientoInventario, Producto, MovimientoInventarioProducto, Almacen, TipoMoinventario
from django_dynamic_admin_forms.admin import DynamicModelAdminMixin

@admin.register(TipoMoinventario)
class TipoMoinventarioAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'descripcion',)
    

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    pass

class MovimientoInventarioProductoInline(admin.TabularInline):
    raw_id_fields = ['producto']
    model = MovimientoInventarioProducto
    extra = 3

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'umed', 'precio',)
    search_fields = ('codigo', 'descripcion', 'umed', 'precio',)

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    change_form_template = 'change_form.html'

    inlines = [MovimientoInventarioProductoInline,]
    
    fields = (
        ('fecha', 'tipo', 'documento',),
        ('almacen_afectado', 'almacen_destino',),
        ('nit', 'sucursal', 'orden_no',),
        ('transporte',),
        'nota_1', 'nota_2', 'nota_3',
    )
    
    class Media:
        css = {
            'all': ('css/movinventario.css',)
        }
        js = ('js/movinventario.js',)