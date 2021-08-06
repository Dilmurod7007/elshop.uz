from django.http import HttpResponse
from django.shortcuts import render
from .models import Mahsulot, Toifa


def index(request):
    mahsulotlar = Mahsulot.objects.all()
    toifalar = Toifa.objects.all()
    return render(request, 'shop/index.html', { 'mahsulotlar': mahsulotlar, 'toifalar': toifalar})


def one(request):
    return render(request, 'shop/one.html')


def two(request):
    return render(request, 'shop/two.html')


def three(request):
    return render(request, 'shop/three.html')


def four(request):
    return render(request, 'shop/four.html')

