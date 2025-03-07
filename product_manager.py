from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Add a product to the list."""
        self.products.append(product)

    def display_all_products(self):
        """Display all products."""
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        """Calculate the total value of the inventory."""
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Total Inventory Value: {total}")

    def remove_product(self, product_name):
        """Remove a product by its name."""
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Product {product_name} has been removed.")
                return
        print(f"Product {product_name} not found.")
