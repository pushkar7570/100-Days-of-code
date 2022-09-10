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

content_left = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def insert_coins():
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))

    total_money = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total_money


def check_contents(drink_ingred, content_left):
    flag = 0
    for item in drink_ingred:
        if content_left[item] >= drink_ingred[item]:
            flag = 1
        else:
            return item
    if flag == 1:
        return True


def calculate_cost(inserted_coins, drink):
    if inserted_coins >= drink['cost']:
        left_money = inserted_coins - drink['cost']
        print(f"Here is ${round(left_money, 2)} in change.")
        return True
    else:
        return False


choice = "test"
money = 0
while len(choice) > 1:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print(f"Water: {content_left['water']}ml")
        print(f"Milk: {content_left['milk']}ml")
        print(f"Coffee: {content_left['coffee']}g")
        print(f"Money: ${money}")
    elif choice == "off":
        choice = ""
    else:
        drink = MENU[choice]
        drink_ingred = drink['ingredients']
        check = check_contents(drink_ingred, content_left)

        if check is True:
            inserted_coins = insert_coins()
            if calculate_cost(inserted_coins, drink):
                money += drink['cost']
                for item in drink_ingred:
                    if item in drink_ingred and item in content_left:
                        content_left[item] = content_left[item] - drink_ingred[item]
                print(f"Here is your {choice}☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {check}.")
