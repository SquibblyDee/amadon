from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

#  import our db
from .models import Store

def index(request):
    query = Store.objects.values('id', 'name', 'price')
    return render(request,'amadon_app/index.html', {'query' : query})

def process(request, methods=['POST']):
    print(request.POST['product_id'])
    print(request.POST['quantity'])
    # print("PRODUCT ID ", product_id)
    # print("QUANTITY ", quantity)
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request,'amadon_app/checkout.html')
