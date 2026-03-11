from product import Product

class ProductManager:

    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)

    def get_product_info(self, products):
        for product in self.products:
            print(product.info())

    def total_amount(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total
    
    def get_products(self):
        return self.products
    
    