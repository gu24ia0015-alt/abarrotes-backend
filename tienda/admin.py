from django.contrib import admin
from .models import Categoria, Proveedor, Producto, Cliente, Venta, DetalleVenta


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'contacto', 'telefono', 'email')
    search_fields = ('nombre', 'contacto', 'email')
    ordering = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'codigo_barras', 'precio', 'stock', 'categoria', 'proveedor', 'activo')
    list_filter = ('categoria', 'proveedor', 'activo')
    search_fields = ('nombre', 'codigo_barras')
    ordering = ('nombre',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'email')
    search_fields = ('nombre', 'email', 'telefono')
    ordering = ('nombre',)


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'total')
    list_filter = ('fecha', 'cliente')
    search_fields = ('cliente__nombre',)
    ordering = ('-fecha',)
    inlines = [DetalleVentaInline]


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'venta', 'producto', 'cantidad', 'subtotal')
    list_filter = ('producto',)
    search_fields = ('producto__nombre',)
