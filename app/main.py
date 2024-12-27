from app.loaded_data import load_data
from app.utils import calc_distance_cost, calc_purchases_cost


def shop_trip() -> None:
    fuel_price, customers, shops = load_data()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs = []
        for shop in shops:
            total_costs = (calc_distance_cost(customer, shop, fuel_price)
                           + calc_purchases_cost(customer, shop))
            total_costs = round(total_costs, 2)
            costs.append((total_costs, shop))
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {total_costs}"
            )
        costs_amount, shop = min(costs)

        if costs_amount <= customer.money:
            print(f"{customer.name} rides to {shop.name}")
            print("")
            customer.money -= costs_amount
            shop.print_check(customer)
            print("")
            customer.go_home()
            print("")
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
