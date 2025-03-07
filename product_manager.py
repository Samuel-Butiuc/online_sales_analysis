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
