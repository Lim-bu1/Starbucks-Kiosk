print("Hello......!!!! Welcome to the Starbucks Coffee Shop\nMay I know your name please\n")
name= input()

menu= ["Latte", "Cappuccino", "Espresso", "Flatwhite", "Cortado"]

print(f"{name} what can I get you today? \nWe are serving {menu}")

order=input()
if order in menu:
    print(f"May i know how many {order} would you like ")
    price = 4
    quantity = input()
    total = price * int(quantity)
    print(total)
    print(f"Thank you for ordering {order}. The total amount is:£ {total}")
    reply = input()
    print("You are welcome and your order will be ready within a moment ")

else:
    print("Sorry sir we don't have it")







