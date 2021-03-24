from app.config.forms import productForm
from django.core.exceptions import ObjectDoesNotExist
from ..core.erp.models import * 

class dataPostLogic():
    def create_product(self,data):
        product = Product.objects.create(
            name = data['name'],
            image = data['image'],
            pvp = data['pvp'],
        )
        return {
            'menssage' : 'producto creado con exito'
        }
    def get_product(self,id):
        try:
            return Product.objects.all().values(
                'name',
                'image',
                'pvp',
            ).get(pk=id)
        except Product.DoesNotExist:
            return {
                'message' : 'no se encuentran datos'
            }
    def update_product(self, id, data):
        Product.objects.filter(pk=id).update(
            name = data['name'],
            image = data['image'],
            pvp = data['pvp'],
        )
        return {
            'message' : 'producto actualizado con exito'
        }
    def delete_product(self, id):
        try:
            Product.objects.get(pk=id).delete()
            return {
                'message' : 'producto eliminado con exito'
            }
        except Product.DoesNotExis:
            return {
                'message' : 'no exite el producto'
            }
    def search_product(self,)