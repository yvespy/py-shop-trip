class Shop:
    def __init__(self, name: str, location: str, products: str) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, customer_cart: dict) -> tuple:
        cost = 0
        purchased_products = {}
        for product, quantity in customer_cart.items():
            if product in self.products:
                product_cost = self.products[product] * quantity
                cost += product_cost
                purchased_products[product] = (quantity, product_cost)
        return cost, purchased_products
