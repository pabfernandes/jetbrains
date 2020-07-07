# Stage #3: Enough coffee for everyone

# step 1: requests amount of water, milk and coffee beans available

# requesting the amounts:
# variables: water_aval - available water type integer
#            milk_aval - available milk type integer
#            coffee_aval - available coffee type integer
print(f"Write how many ml of water the coffee machine has:")
water_aval = int(input())
print(f"Write how many ml of milk the coffee machine has:")
milk_aval = int(input())
print(f"Write how many grams of coffee beans the coffee machine has:")
coffee_aval = int(input())

# Based in the quantities available, the machine should return messages according to availability and number
# of coffee cups desired by the  user

# Based in the recipe: 200 ml of water, 50 ml of milk, 15 g of coffee beans, calculate max number of cups
water_rest = water_aval // 200
milk_rest = milk_aval // 50
coffee_rest = coffee_aval // 15

# Check the minimum between them
max_cups = min(water_rest, milk_rest, coffee_rest)

# Ask for user input about how many cups of coffee and return message
print(f"Write how many cups of coffee you will need:")
cups_of_coffee = int(input())

if cups_of_coffee > max_cups:
    print(f"No, I can make only {max_cups} cups of cofffee")
elif cups_of_coffee == max_cups:
    print(f"Yes, I can make that amount of coffee")
elif cups_of_coffee < max_cups:
    print(f"Yes, I can make that amount of coffee (and even {max_cups - cups_of_coffee} more than that)")
