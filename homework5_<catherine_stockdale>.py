#Step 1: Create a List that Contains 6 Items
shoes = ["Sambas", "Birkenstocks", "Cowgirl boots", "Hokas", "Chacos", "Vans Slip-ons"]
#Step 2: Print the items to the output console
print(shoes)
#Step 3: Print the first two items in the list using a slice.  The output message should be: The first two items in the list are: item1, item2
first_two = shoes[:2]
print(f"The first two items in the list are: {first_two[0]}, {first_two[1]}")
#Step 4: Print the middle two items in the list using a slice.  The output message should be: The middle two items in the list are: item3, item4
middle_two = shoes[2:4]
print(f"The middle two items in the list are: {middle_two[0]}, {middle_two[1]}")
#Step 5: Print the first and last items in the list using indexes.  The output message should be: The first and last items in the list are: item1, item6
print(f"The first and last items in the list are: {shoes[0]}, {shoes[5]}")

#Transition to Tuple Exercise for Restaurant Menu Items 
#Step 1 Tuple Exercise: A restaurant only offers five basic foods on its menu. Decide on these five foods and store them in a tuple.
menu = ("spaghetti", "lasagna", "pizza", "ravioli", "tiramisu")
#Step 2: Print each item on the menu using a for loop.
for item in menu: 
    print(item)
#Step 3: The restaurant has updated its menu, replacing two of the items with different foods.  Copy the tuple replacing two of the foods on the menu
new_menu = ("spaghetti", "lasagna", "fettucine alfredo", "ravioli", "chocolate cake")
#Step 4: Print each item on the revised menu using a loop.
for item in new_menu:
    print(item)