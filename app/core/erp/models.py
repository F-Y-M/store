from django.db import models
from datetime import datetime

gender_choices = (
    ('male','Masculino'),
    ('female','Femenino'),
)

class Product(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)

    class Meta:
        verbose_name ='Product'
        verbose_name_plural ='Products'
        ordering = ['id']

    def __str__(self):
        return self.name

class Client(models.Model):
    names = models.CharField(verbose_name='Nombres', max_length=50)
    surnames = models.CharField(verbose_name='Apellidos', max_length=50)
    dni = models.CharField(verbose_name='Dni',unique=True, max_length=50, blank=True)
    address = models.CharField(verbose_name='Direccion', max_length=50, blank=True, null=True)
    sexo = models.CharField(verbose_name='Sexo',choices=gender_choices, max_length=6, blank=True, default='male', null=True)

    class Meta:
        verbose_name ='Client'
        verbose_name_plural ='Clients'
        ordering = ['id']

    def __str__(self):
        return self.name

class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField( max_digits=9, decimal_places=2, default=0.00)
    iva = models.DecimalField( max_digits=9, decimal_places=2, default=0.00)
    total = models.DecimalField( max_digits=9, decimal_places=2, default=0.00)

    class Meta:
        verbose_name ='Sale'
        verbose_name_plural ='Sales'
        ordering = ['id']

    def __str__(self):
        return self.name

class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        verbose_name ='DetSale'
        verbose_name_plural ='DetSales'
        ordering = ['id']

    def __str__(self):
        return self.name
