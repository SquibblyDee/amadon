from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

#  import our db
from .models import Store

def index(request):
    # create session keys if they aren't already present
    if 'count' not in request.session:
        request.session['count'] = 0
        request.session['product_id'] = 0
        request.session['total_spent'] = 0
        request.session['total'] = 0
    # query the desired data before rendering index and returning the query's contents
    query = Store.objects.values('id', 'name', 'price')
    return render(request,'amadon_app/index.html', {'query' : query})

def process(request, methods=['POST']):
    # assigning post data to a variable to cut down on typing
    quantity = request.POST['quantity']
    # pulling the one value we need from the db using the product_id as reference
    query = Store.objects.filter(id=request.POST['product_id']).values('price')
    # Iterate through the query results to get the desired value
    for row in query:
        for key in row:
            # do all the math we need and push it back to the respective session keys
            price = float(row[key])
            request.session['total'] = price * float(quantity)
            request.session['count']+=int(quantity)
            request.session['total_spent']+=request.session['total']
    # then return a redirerct to our checkout page html
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request,'amadon_app/checkout.html')
