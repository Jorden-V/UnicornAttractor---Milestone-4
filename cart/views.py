from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html" )

@login_required()
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = 1

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect('view_features')

@login_required()
def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specifies amount"""
    quantity = 1
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))