class Cart:
    def __init__(self):
        self.cart_items = []  # List to store products in the cart

    def add_to_cart(self, product):
        """Add a product to the cart."""
        self.cart_items.append(product)
        print(f"Product {product.name} added to the cart.")

    def total_cart_value(self):
        """Calculate the total value of the items in the cart."""
        total = sum(item.price * item.quantity for item in self.cart_items)
        return total

    def display_cart(self):
        """Display the contents of the cart."""
        if not self.cart_items:
            print("The cart is empty.")
        else:
            print("Cart contents:")
            for item in self.cart_items:
                item.display_info()
