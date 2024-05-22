from store.models import Product
class Cart():
    def __init__ (self, request):
        self.session = request.session
        # Gets previous session key
        cart = self.session.get('session_key')
        #creates new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #makes sure cart is avaible on all pages
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)


        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        #get id from cart
        product_ids = self.cart.keys()
        #use ids to search products in DB
        products = Product.objects.filter(id__in=product_ids)
        #return products searched
        return products 