from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
drink_maker = CoffeeMaker()
transaction_machine = MoneyMachine()

should_continue = True

while should_continue:
    user_choice = input(f"What would you like? ({coffee_menu.get_items()}): ")
    if user_choice == 'off':
        should_continue = False
    elif user_choice == 'report':
        drink_maker.report()
        transaction_machine.report()
    else:
        drink = coffee_menu.find_drink(user_choice)
        if drink_maker.is_resource_sufficient(drink) and transaction_machine.make_payment(drink.cost):
            drink_maker.make_coffee(drink)
