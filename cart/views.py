from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse, HttpResponseBadRequest

def cart_summary(request):

    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities})


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty', 0))
        except (TypeError, ValueError):
            return HttpResponseBadRequest("Invalid input.")

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()
        return JsonResponse({'qty': cart_quantity})

def cart_delete(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        return JsonResponse({'product': product_id})
    return JsonResponse({'error': 'Invalid request'}, status=400)

   

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty', 0))

            cart.update(product=product_id, quantity=product_qty)

            response = JsonResponse({'qty':product_qty})
            return response
