from django.shortcuts import render
from django.shortcuts import render
from mywatchlist.models import moviesItem
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_movies_html(request):
    data_barang_movies = moviesItem.objects.all()
    context = {
    'list_movies': data_barang_movies,
    'nama': 'Rafi Madani',
    'npm' : '2106750856'
    }
    return render(request, "mywatchlist.html",context)

def show_movies_xml(request):
    data = moviesItem.objects.all()
    context = {
    'nama': 'Rafi Madani',
    'npm' : '2106750856'
    }
    return HttpResponse(serializers.serialize("xml", data),content_type="application/xml")

def show_movies_json(request):
    data = moviesItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")






