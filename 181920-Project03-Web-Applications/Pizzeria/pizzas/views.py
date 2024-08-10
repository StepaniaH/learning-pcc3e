from django.shortcuts import render

from .models import Pizza

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_name):
    pizza = Pizza.objects.get(name=pizza_name)
    toppings = pizza.topping_set.all() # [Important]
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
