class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0  # Changed to float to avoid precision loss
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.items.append({"title": title, "price": price, "quantity": quantity})  # Store item info as a dictionary
        self.total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}")
        else:
            print("There is no discount to apply.")

    def get_items(self):
        return self.items

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()  # Get the last item
            self.total -= last_item["price"] * last_item["quantity"]
        else:
            print("No items to void.")
            self.total = 0.0
