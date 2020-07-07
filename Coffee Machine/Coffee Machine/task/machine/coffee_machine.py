# Stage #4: Action

# Initializing variables:
mach_money = 550
mach_water = 400
mach_milk = 540
mach_coffee = 120
mach_cups = 9

print("The coffee machine has:")
print(f"{mach_water} of water")
print(f"{mach_milk} of milk")
print(f"{mach_coffee} of coffee beans")
print(f"{mach_cups} of disposable cups")
print(f"{mach_money} of money")

# First, the Machine has to read what you wanna do
print("What you want to do? Type in the option:")
choose_option = input()

# Recipes:      water   milk    coffe   price
# espresso:     250     0       16      4
# latte:        350     75      20      7
# cappuccino    200     100     12      6

if choose_option == "buy":
    print("Which kind of coffee do you want? 1 - espresso, 2 - latte or 3 - cappuccino?")
    coffee_type = int(input())
    if coffee_type == 1:
        mach_water -= 250
        mach_coffee -= 16
        mach_money += 4
        mach_cups -= 1
    elif coffee_type == 2:
        mach_water -= 350
        mach_milk -= 75
        mach_coffee -= 20
        mach_money += 7
        mach_cups -= 1
    elif coffee_type == 3:
        mach_water -= 200
        mach_milk -= 100
        mach_coffee -= 12
        mach_money += 6
        mach_cups -= 1
elif choose_option == "fill":
    mach_water += int(input())
    mach_milk += int(input())
    mach_coffee += int(input())
    mach_cups += int(input())
elif choose_option == "take":
    print(f"I gave you ${mach_money}")
    mach_money = 0

print("The coffee machine has:")
print(f"{mach_water} of water")
print(f"{mach_milk} of milk")
print(f"{mach_coffee} of coffee beans")
print(f"{mach_cups} of disposable cups")
print(f"{mach_money} of money")

