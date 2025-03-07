from product import Product
from product_manager import ProductManager

# Create instances of Product
product1 = Product("Laptop", 2000, 10)
product2 = Product("Smartphone", 800, 15)
product3 = Product("Headphones", 150, 30)

# Create an instance of ProductManager
product_manager = ProductManager()

# Add products to the manager
product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)

# Display all products
product_manager.display_all_products()

# Display total inventory value
product_manager.total_inventory_value()
