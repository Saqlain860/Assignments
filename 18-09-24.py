#python program to write a code for randam number
import random
for i in range(1):
    number = random.randint(1,30)
    inpu  = int(input("Enter a number between 1 to 30: "))
    if number==inpu:
        print("congrats you have won the game")
    elif number!=inpu:
        print("oops,you have loose the game",number)
print(number)

 #billing program3
items = {
    "apple": 200,
    "banana": 40,
    "milk": 60,
    "bread": 30,
    "eggs": 7
}
def calculate_bill(purchased_items):
    total = 0
    for item, quantity in purchased_items.items():
        total += items[item] * quantity
    return total
purchased_items = {}
while True:
    item = input("Enter the item (or type 'done' to finish, 'add' to add a new item): ").lower()
    if item == 'done':
        break
    elif item == 'add':
        new_item = input("Enter the name of the new item: ").lower()
        if new_item in items:
            print("Item already exists.")
        else:
            price = float(input(f"Enter the price of {new_item}: "))
            items[new_item] = price
            print(f"{new_item} added with a price of rs{price:.2f}")
    elif item in items:
        quantity = int(input(f"Enter the quantity of {item}: "))
        if item in purchased_items:
            purchased_items[item] += quantity
        else:
            purchased_items[item] = quantity
    else:
        print("Item not found. Please enter a valid item.")

total_bill = calculate_bill(purchased_items)
print(f"The total bill is: rs{total_bill:.2f}")

# write s program to reverse the string
# ex: input:"learning python is very easy"
# o/p1 : easy very is python learning
# o/p2 : ysae yrev si nohtyp gninrael
s = "learning python is very easy"
s1 = s.split()
s2 = " ".join(s1[::-1])
print(s2)

s3 = s[::-1]
print(s3)

     
                 
 
 

 
 
     
                 
 
 












