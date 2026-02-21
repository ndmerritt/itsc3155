import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier(resources)


def report():
    """Print current resource levels."""
    print(f"Bread: {resources['bread']} slices")
    print(f"Ham: {resources['ham']} slices")
    print(f"Cheese: {resources['cheese']} ounces")


def main():

    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            break

        elif choice == "report":
            report()

        elif choice in recipes:
            order = recipes[choice]

            if sandwich_maker_instance.check_resources(order["ingredients"]):
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, order["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, order["ingredients"])
        else:
            print("Invalid choice. Please choose small, medium, large, report, or off.")


if __name__=="__main__":
    main()