from django.shortcuts import render
from django.views.generic import TemplateView
from core.erp.models import *

def indexView(request):
    data = {
        'product' : Product.objects.all()
    }
    return render(request, 'index.html', data)

def productView(request):
    return render(request, 'products.html')

def singleView(request):
    return render(request, 'single.html')

def contactView(request):
    return render(request, 'contact.html')

def usView(request):
    return render(request, 'us.html')

def dosView(request):
    return render(request, 'dos.html')

def testView(request):
    return render(request, 'test.html')
