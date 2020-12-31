MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0.0


# TODO: 4 Check resources sufficient?
def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


# TODO: 5 Process coins
def process_coins():
    """"Returns the total calculated from coins inserted"""
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many penny?: ")) * 0.01
    return total


# TODO: 6 Check transition successful?
def transaction(money_inserted, drink_cost):
    """"Return True when the payment is accepted, or False if money is insufficient"""
    if money_inserted >= drink_cost:
        change = round(money_inserted - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7 Make Coffee
def make_coffee(name, order_ingredients):
    """"Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {name} ☕️")


should_continue = True

while should_continue:
    # TODO: 1 Prompt user by asking 'what would you like?' (espresso/latte/cappuccino)
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 3 Print report
    if user_choice == 'report':
        resource_water = resources["water"]
        resource_milk = resources["milk"]
        resource_coffee = resources["coffee"]
        print(f"Water: {resource_water}ml, \nMilk: {resource_milk}ml, \nCoffee: {resource_coffee}g, \nMoney: ${profit}")
    # TODO: 2 Turn off the Coffee Machine by entering "off" to the prompt
    elif user_choice == 'off':
        should_continue = False
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])