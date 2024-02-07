# CREATING OWN MODULES
import test_module
print(f"Speed of light: {test_module.c}") #Calling the function with module_name.variable_name
print("\n")

# EXERCISE - Coin flip, Roll dice, etc
import random
n = random.randint(1,2)
if n == 1:
    coin_flip = "Heads"
    print(f"It's {coin_flip}")
if n == 2:
    coin_flip = "Tails"
    print(f"It's {coin_flip}")
print("\n")


# LISTS
'''
Variable is a single piece of data
List is a grouped piece of data

SYNTAX:
names = ['item_1', 2, 'item_3']
'''

states_of_america = ["Delaware", "Pennsylvania",
                     "New Jersey", "Georgia",
                     "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina",
                     "New Hampshire", "Virginia",
                     "New York", "North Carolina",
                     "Rhode Island", "Vermont",
                     "Kentucky", "Tennessee",
                     "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri",
                     "Arkansas", "Michigan", "Florida",
                     "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota",
                     "Oregon", "Kansas",
                     "West Virginia", "Nevada",
                     "Nebraska", "Colorado",
                     "North Dakota", "South Dakota",
                     "Montana", "Washington",
                     "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico",
                     "Arizona", "Alaska", "Hawaii"]

print(f"States that joined Union first: {states_of_america[0]}")
print(f"States that joined Union last: {states_of_america[-1]}")


"""
1. Changing items in the List
2. Append - ADDING single Item to the END of list
3. Extend - ADDING multiple Items to the END of list
"""


names = ["Yash", "me", "myself"]
names[1] = 'Yashwanth'
names[2] = 'Yashwanth K'
print(names)

names.append("YASHWANTH K")
names.extend(["me", "myself", "I"])

print(names)

print(len(names))




# EXERCISE - Pick a random name from the list who is gonna buy the meal today.

'''
USE OF choice function is NOT ALLOWED!
Split Function - split(", ") --> splits the string and makes a list on the occurrance of ", "

INPUT:
Enter everybody's names separated by comma: Angela, Ben, Jenny, Michael, Chloe

OUTPUT:
Michael is going to buy the meal today!
'''

import random
name = input("Enter everyone's name (separated by comma): ")
name_list = name.split(", ")
print(name_list)

n = random.randint(0,(len(name_list))-1)
print(f"{name_list[n]} is going to buy the meal today!")

