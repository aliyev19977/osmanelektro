from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . import models

def index(request):
    products = models.Product.objects.all()

    return render(request, 'electronics/home.html', {'products':products})

