from django import forms

from ..core.erp.models import *

class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'image',
            'pvp',
        ]
        labels = {
            'name' : 'Mombre',
            'image' : 'Imagen',
            'pvp' : 'Precio',   
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'names', 
            'surnames', 
            'dni', 
            'address', 
            'sexo', 
        ]
        labels = {
            'names' : 'Nombres',
            'surnames' : 'Apellidos',
            'dni' : 'Identificacion',
            'address' : 'Direccion',
            'sexo' : 'Sexo',
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = [
            'cli',
            'date_joined',
            'subtotal',
            'iva',
            'total',
        ]
        labels = {
            'cli' : 'Cliente',
            'date_joined' : 'Fecha de unido',
            'subtotal' : 'Sub-total',
            'iva' : 'Iva',
            'total' : 'Total',
        }

class DetSalesForm(forms.ModelForm):
    class Meta:
        model = DetSale
        fields = [
            'sale',
            'prod',
            'price',
            'cant',
            'subtotal',
        ]
        labels = {
            'sale' : 'Venta',
            'prod' : 'Producto',
            'price' : 'Precio',
            'cant' : 'Cantidad',
            'subtotal' : 'Sub-total',
        }