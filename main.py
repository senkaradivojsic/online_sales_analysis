from product_manager import ProductManager
from cart import Cart

manager = ProductManager()
cart = Cart()

manager.add_product("Laptop", 86000, 3)
manager.add_product("Smartphone", 50000, 5)
manager.add_product("Headphones", 15000, 10)
manager.add_product("Monitor", 30000, 6)
manager.remove_product("Smartphone")

for product in manager.get_products():
    print(product)
    
cart.add_to_cart(manager.get_products()[0], 1)
cart.add_to_cart(manager.get_products()[1], 2)
cart.add_to_cart(manager.get_products()[2], 1)
view_cart = cart.view_cart()
print(f"Total in cart: {cart.cart_total()}")