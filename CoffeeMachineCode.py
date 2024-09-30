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
profit =0
def is_resource_sufficient(ingredients):
    """Return True when order can be made .False if ingredients are insufficient"""
    for item in ingredients:
       if ingredients[item]>=resources[item]:
           print(f"The resourses are not sufficient {item}")
           return False
    return True  
def is_transaction_successfull(money_recieved,drink_cost):
    """returns True when payment is accepted or return False if money is insufficient.""" 
    global profit
    if money_recieved>=drink_cost:
        profit+=drink_cost
        change=round(money_recieved-drink_cost,2)
        print(f"The change is {change}")
        return True  
    else:
        print("The money is insufficient.Money refunded")
        return False
def check_balance():
    """Return total calculated coins inserted ."""
    print("Please insert coin:")
    total = int(input ("How many quarrters:"))*.25   
    total += int(input ("How many dimes:"))*.1 
    total += int(input ("How many nickles:"))*0.05
    total += int(input ("How many penniies:"))*.01
    return total

is_on= True
while is_on :
    choice=input("What would you like (espresso/latte/cappuccino/off/report): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml") 
        print(f"Milk: {resources['milk']}ml") 
        print(f"Coffee: {resources['coffee']}g") 
        print(f"Money: ${profit}")
    else:
        drink=MENU.get(choice)  # Using .get() method to handle non-existent drink
        if drink:
            if is_resource_sufficient(drink["ingredients"]):
                payment = check_balance()
                if payment is not None:  # Check if payment is not None
                    if not is_transaction_successfull(payment, drink["cost"]):  # Corrected spelling
                        continue  # Skip rest of the loop if transaction fails
                    print(f"Here is your {choice}. Enjoy!")
        else:
            print("Invalid choice. Please select from the available options.")


        
