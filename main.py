from product import Product
from product_manager import ProductManager
from cart import Cart
import random

# Create instances of Product
product1 = Product("Laptop", 2000, 10)
product2 = Product("Smartphone", 800, 15)
product3 = Product("Headphones", 150, 30)
product4 = Product("Tablet", 500, 5)
product5 = Product("Monitor", 300, 8)

# Create an instance of ProductManager
product_manager = ProductManager()

# Add products to the manager
product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)
product_manager.add_product(product4)
product_manager.add_product(product5)

# Create an instance of Cart
cart = Cart()

# Randomly select 3 products from the ProductManager and add them to the cart
random_products = random.sample(product_manager.products, 3)  # Randomly select 3 products
for product in random_products:
    cart.add_to_cart(product)

# Display the cart contents and total value
cart.display_cart()
total_cart_value = cart.total_cart_value()
print(f"Total Cart Value: {total_cart_value}")
