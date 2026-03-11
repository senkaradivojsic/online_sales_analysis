from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product("Laptop", 86000, 5)
manager.add_product("Smartphone", 50000, 10)
manager.add_product("Headphones", 15000, 20)
manager.add_product("Monitor", 30000, 7)

for product in manager.get_products():
    print(product)

total = manager.total_amount()
print(f"Total amount of all products: {total}")