from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

#  import our db
from .models import Store

def index(request):
    if 'count' or 'product_id' or 'total_spent' or 'total' not in request.session:
        request.session['count'] = 0
        request.session['product_id'] = 0
        request.session['total_spent'] = 0.00
        request.session['total'] = 0
    query = Store.objects.values('id', 'name', 'price')
    return render(request,'amadon_app/index.html', {'query' : query})

def process(request, methods=['POST']):
    quantity = request.POST['quantity']
    query = Store.objects.filter(id=request.POST['product_id']).values('price')
    print("QUERY: ", query)
    for row in query:
        for key in row:
            price = float(row[key])
            request.session['total'] = price * float(quantity)
            request.session['count']+=int(quantity)
            request.session['total_spent']+=request.session['total']
            print("TOTAL: ", request.session['total'])
            print("COUNT: ", request.session['count'])
            print("TOTALSPENT ", request.session['total_spent'])
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request,'amadon_app/checkout.html')
