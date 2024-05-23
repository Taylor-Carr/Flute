from store.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        # Get the cart from the session, or create a new one if it doesn't exist
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        quantity = int(quantity)  # Ensure quantity is an integer

        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity

        self.session.modified = True

    def __len__(self):
        return sum(self.cart.values())
    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        #get id from cart
        product_ids = self.cart.keys()
        #use ids to search products in DB
        products = Product.objects.filter(id__in=product_ids)
        #return products searched
        return products 

    def get_quants(self):
        quantities = self.cart
        return quantities 