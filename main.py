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
   }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

ing_left = resources

while True :


    def amount():
        quarters = int(input("Enter the number of quarter: "))
        dimes = int(input("Enter the number of dimes: "))
        nickles = int(input("Enter the number of nickles: "))
        pennies = int(input("Enter the number of pennies: "))
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        return total

    def money():
        if cost > money_recived:
            print(f"not enough money 😶")
        elif cost < money_recived:
            print(f"here is ur {round((money_recived - cost),2)} change 🤗")
            print("Enjoy your coffee ☕ !")


    i_want = input("What would you like? (espresso/latte/cappuccino): ")


    if i_want == 'espresso':
        if ing_left['water'] < MENU[i_want]['ingredients']['water'] or ing_left['coffee'] < MENU[i_want]['ingredients'][
            'coffee'] :
            print("insufficient supplies 😪")
            break
        money_recived = amount()
        cost = ((MENU['espresso'])['cost'])
        money()
        ing_left['water'] = resources['water'] - (((MENU['espresso'])['ingredients'])['water'])
        ing_left['coffee'] = resources['coffee'] - (((MENU['espresso'])['ingredients'])['coffee'])
    elif i_want == 'latte':
        money_recived = amount()
        cost = ((MENU['latte'])['cost'])
        money()
        ing_left['water'] = resources['water'] - (((MENU['latte'])['ingredients'])['water'])
        ing_left['coffee'] = resources['coffee'] - (((MENU['latte'])['ingredients'])['coffee'])
        ing_left['milk'] = resources['milk'] - (((MENU['latte'])['ingredients'])['milk'])

    elif i_want == 'cappuccino':
        money_recived = amount()
        cost = ((MENU['cappuccino'])['cost'])
        money()
        ing_left['water'] = resources['water'] - (((MENU['cappuccino'])['ingredients'])['water'])
        ing_left['coffee'] = resources['coffee'] - (((MENU['cappuccino'])['ingredients'])['coffee'])
        ing_left['milk'] = resources['milk'] - (((MENU['cappuccino'])['ingredients'])['milk'])
    elif i_want == 'report':
        print(ing_left)
    elif i_want != 'espresso':
        if ing_left['water'] < MENU[i_want]['ingredients']['water'] or ing_left['coffee'] < MENU[i_want]['ingredients']['coffee'] or ing_left['milk'] < MENU[i_want]['ingredients']['milk']:
            print("insufficient supplies")
            break





