shoppingcart = []

continueshopping = True

while(continueshopping):
    shoppingitem=input("Enter the item to the be added to the cart:")
    shoppingcart.append(shoppingitem)

    userchoice=input("Do you want to Continue shopping yes or no?")
    if userchoice.lower()=="yes":
        continueshopping = True
    elif userchoice.lower() == "no":
        continueshopping = False
    else:
        print("Enter a valid choice yes or no")

print("Thanks for Shopping with us!Please find the items in the cart")
print(shoppingcart)