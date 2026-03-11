
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        self.cart_items.append((product, quantity))

    def cart_total(self):
        total = 0
        for product, quantity in self.cart_items:
            total += product.price * quantity
        return total
    
    def view_cart(self):
        for product, quantity in self.cart_items:
            print(f"{product.name} - Quantity: {quantity}, Total: {product.price * quantity}")