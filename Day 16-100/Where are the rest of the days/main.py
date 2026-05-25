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

profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry {item} not sufficient ")
            return False
    else:
        return True

def process_coins():
    print("Insert coin")
    total = int(input("How many quaters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def is_transaction_successful(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Payment successful, Here is your change ${change}")
        return True
    else:
        print("Sorry payment failed, total refunded")
        return False

def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your coffee {drink_name}")

print("Welcome to the coffee machine")
while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        break
    elif user_input == "report":
        print(f" Water: {resources['water']}ml")
        print(f" Milk: {resources['milk']}ml")
        print(f" Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_input in MENU:
        drink = MENU[user_input]
        is_resource_sufficient(drink["ingredients"])
        payment = process_coins()
        is_transaction_successful(payment, drink["cost"])
        profit += payment
        make_coffee(user_input, drink["ingredients"])
    else:
        print(f"Sorry {user_input} is not a valid option")


