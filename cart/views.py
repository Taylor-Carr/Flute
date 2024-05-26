from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product, Order
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def cart_summary(request):
    cart = Cart(request)
    cart_items = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_items": cart_items, "quantities": quantities, "totals": totals})

@login_required
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

        cart_quantity = len(cart)
        return JsonResponse({'qty': cart_quantity})

@login_required
def cart_delete(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product_id=product_id)
        return JsonResponse({'product': product_id})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty', 0))
        cart.update(product_id=product_id, quantity=product_qty)
        response = JsonResponse({'qty': product_qty})
        return response

@login_required
def checkout(request):
    cart = Cart(request)
    customer = request.user
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        for item in cart.get_prods():
            Order.objects.create(
                product=item.product,
                customer=customer,
                quantity=item.quantity,
                address=address,
                phone=phone,
                date=datetime.datetime.today(),
                status=False
            )
        cart.clear()
        return redirect('order_confirmation')
    return render(request, 'checkout.html')

@login_required
def order_confirmation(request):
    return render(request, 'order_confirmation.html')