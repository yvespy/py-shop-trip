import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customers = config["customers"]
    shops = config["shops"]

    customer_objects = []
    shop_objects = []

    for customer in customers:
        car = Car(customer["car"]["brand"],
                  customer["car"]["fuel_consumption"])
        customer_objects.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                car
            )
        )

    for shop in shops:
        shop_objects.append(Shop(
            shop["name"], shop["location"], shop["products"]))

    for customer in customer_objects:
        print(f"\n{customer.name} has {customer.money: .2f} dollars")

        best_shop = None
        min_total_cost = float("inf")
        best_purchased_products = {}

        for shop in shop_objects:
            distance_to_shop = customer.calculate_distance(shop.location)
            distance_to_home = customer.calculate_distance(shop.location)
            fuel_cost_to_shop = customer.car.calculate_fuel_cost(
                distance_to_shop, fuel_price)
            fuel_cost_to_home = customer.car.calculate_fuel_cost(
                distance_to_home, fuel_price)

            product_cost, purchased_products = shop.calculate_product_cost(
                customer.product_cart)
            total_trip_cost \
                = fuel_cost_to_shop + product_cost + fuel_cost_to_home

            print(f"{customer.name}'s trip to "
                  f"{shop.name} costs {total_trip_cost: .2f}")

            if total_trip_cost < min_total_cost:
                min_total_cost = total_trip_cost
                best_shop = shop
                best_purchased_products = purchased_products

        if best_shop and customer.can_afford_trip(min_total_cost):
            print(f"{customer.name} rides to {best_shop.name}")
            customer.update_money_and_location(
                min_total_cost, best_shop.location)
            customer.print_receipt(
                best_shop.name, best_purchased_products,
                min_total_cost - fuel_cost_to_home)
            print(f"{customer.name} rides home")
            customer.update_money_and_location(0, customer.location)
            print(f"{customer.name} now has {customer.money: .2f} dollars")
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
