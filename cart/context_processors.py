from .cart import Cart

#context processor, cart works across site

def cart(request):
    return {'cart': Cart(request)}