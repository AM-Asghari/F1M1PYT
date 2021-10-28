
grocerylist = ["meat","cheddar","burger buns","pickles","cabbage","cucumber","tomatoes"]
print("Your Grocery list contains:", grocerylist[0],grocerylist[1],grocerylist[2],grocerylist[3],grocerylist[4],grocerylist[5],grocerylist[6])

shoppingcart = []
print(f'Current shopping cart {shoppingcart}')

for x in range(7):

    f = input("Please enter an item to add to your shopping cart:\n")
    shoppingcart.append(str(f))

print(f'Updated shopping cart {shoppingcart}')

if grocerylist == shoppingcart:
    print("Done shopping")
else:
    print("Continue shopping")