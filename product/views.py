from django.shortcuts import render
from django.http import HttpResponse
from .models import AllProduct


def Home(request):
    return render(request, 'product/home.html')


def About(request):
    return render(request, 'product/about.html')

def Timber(request):
    allproduct = AllProduct.objects.all()
    context = {'allproduct':allproduct}
    return render(request, 'product/timber.html',context)
    

