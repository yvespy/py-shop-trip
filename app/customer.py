import math
from datetime import datetime

from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, other_location: list) -> float:
        return math.sqrt(
            (
                self.location[0] - other_location[0]) ** 2 + (
                self.location[1] - other_location[1]) ** 2
        )

    def can_afford_trip(self, trip_cost: float) -> bool:
        return self.money >= trip_cost

    def update_money_and_location(self,
                                  total_cost: float,
                                  new_location: list) -> None:
        self.money -= total_cost
        self.location = new_location

    def print_receipt(self,
                      shop_name: str,
                      purchased_products: dict,
                      total_cost: float) -> None:
        print(f"\nDate: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase at {shop_name}!")
        print("You have bought:")
        for product, (quantity, cost) in purchased_products.items():
            print(f" {quantity} {product}s for {cost} dollars")
        print(f"Total cost in {total_cost: .2f} dollars")
        print("See you again!")
