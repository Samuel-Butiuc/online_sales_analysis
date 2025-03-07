class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Display the product details."""
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def update_quantity(self, quantity):
        """Update the product quantity."""
        self.quantity = quantity
        print(f"Quantity of {self.name} updated to {self.quantity}")
