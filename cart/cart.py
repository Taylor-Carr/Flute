from store.models import Product
from .models import Cart as CartModel, CartItem
from django.conf import settings

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.customer = request.user
        self.cart, created = CartModel.objects.get_or_create(customer=self.customer)

    def add(self, product, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(cart=self.cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

    def save(self):
        self.cart.save()
        self.session.modified = True

    def delete(self, product_id):
        product = Product.objects.get(id=product_id)
        cart_item = CartItem.objects.get(cart=self.cart, product=product)
        cart_item.delete()

    def update(self, product_id, quantity):
        product = Product.objects.get(id=product_id)
        cart_item = CartItem.objects.get(cart=self.cart, product=product)
        cart_item.quantity = quantity
        cart_item.save()

    def __len__(self):
        return sum(item.quantity for item in self.cart.items.all())

    def get_prods(self):
        return self.cart.items.all()

    def get_quants(self):
        return {item.product.id: item.quantity for item in self.cart.items.all()}

    def cart_total(self):
        return self.cart.get_total_price()

    def clear(self):
        self.cart.items.all().delete()