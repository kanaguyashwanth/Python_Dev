# for loop
'''
SYNTAX:

for var_name in list_name:
    print (var_name)
'''



# # Example_1: [Printing the List using for loop]
# fruits = ['apple', 'banana', 'orange']
# for x in fruits:
#     print (x)



# # Example_2: [Average student height]
# student_heights = input("Input a list of student heights ").split()     #This would split the 'space' between each entry
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# #Write your code below this row
# sum_heights = 0
# for n in range(0, len(student_heights)):
#     sum_heights += student_heights[n]
#
# average_height = sum_heights / len(student_heights)
# print(average_height)



# Example_3:
# student_scores = input("Input list of student scores: ").split()            # This would split the space between each entry
# # printing the student scores
# for x in range (len(student_scores)):
#     print(student_scores[x])
#
# # deciding the highest score
# highest_score = student_scores[0]
# for x in range (len(student_scores)):
#     if (student_scores[x] > highest_score):
#         highest_score = student_scores[x]
#
# print(f'The highest score is: {highest_score}')



# # Example 4:
# # for loop with range
# for n in range(1,11):      # Prints from 1 to 10 and not 11
#     print(n)
#
# '''
# OUTPUT:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# '''



# # for loop with range and step
# for n in range(1,11,2):
#     print(n)
#
# '''
# OUTPUT:
# 1
# 3
# 5
# 7
# 9
# '''



# # sum of first 100 numbers
# sum_100 = 0
# for n in range(1,101):          # 101 because, it won't take 101.
#     sum_100 += n
# print(f"The sum of first 100 numbers: {sum_100}")



# # sum of first 100 even numbers
# sum_even = 0
# for n in range(1,101):          # 101 because, it won't take 101.
#     if n % 2 == 0:
#         sum_even += n
#
# print(f"The sum of first 100 even numbers: {sum_even}")



# # multiple of 3-fizz, multiple of 5-buzz, multiple of both-fizzbuzz
# for n in range(1,101):
#     if n%3==0 and n%5==0:
#         print("fizzbuzz")
#     elif n%5 == 0:
#         print("buzz")
#     elif n%3==0:
#         print("fizz")
#     else:
#         print(n)

# '''
# NOTE:
# For fizzbuzz program to work properly,
# first condition must be for fizzbuzz
# next can be for either fizz or buzz
# in the end, we print the number if its none of the conditions
# '''



#Password Generator Project
'''
NOTE:
You can use a shuffle the list as below:

import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = ['j', 'u', 'X', 'S', '9', '8', '2', '6', ')', '#', '*', '(']
print (password_list)
random.shuffle (password_list)
print (password_list)
'''

"""
OUTPUT:
Welcome to the PyPassword Generator!
How many letters would you like in your password?
5
How many symbols would you like?
5
How many numbers would you like?
5
Random strings: MVpSg
Random numbers: 40652
Random symbols: &%!%!
New random string: MVpSg40652&%!%!
New List: ['M', 'V', 'p', 'S', 'g', '4', '0', '6', '5', '2', '&', '%', '!', '%', '!']
The shuffled list: ['2', '!', '6', '&', '4', 'V', 'S', '5', 'M', '%', '!', 'g', 'p', '%', '0']
The shuffled string: 2!6&4VS5M%!gp%0
"""

import random
letters = \
[
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print('Welcome to the PyPassword Generator')
n_letters = int(input("How many letters: "))
n_symbols = int(input("How many symbols: "))
n_numbers = int(input("How many numbers: "))


# letter_randomization
'''
NOTE:
len_letters = length of the letters list
n_letters = how many letters
'''
len_letters = len(letters)
random_letters = ''
for n in range(0, n_letters):        # If n_letters = 5, then from 0 to 4(total=5)
    rand_n = random.randint(0,(len_letters-1))
    random_letters += letters[rand_n]
print(random_letters)


# numbers_randomization
len_numbers = len(numbers)
random_numbers = ''
for n in range (0, n_numbers):
    rand_n = random.randint(0,(len_numbers-1))
    random_numbers += numbers[rand_n]
print(random_numbers)


# symbols_randomization
len_symbols = len(symbols)
random_symbols = ''
for n in range (0, n_symbols):
    rand_n = random.randint(0,(len_symbols-1))
    random_symbols += symbols[rand_n]
print(random_symbols)


# password_generator
password = random_letters + random_numbers + random_symbols
print(type(password))
print(password)
# converting string type to list type, since strings are immutable
len_password = len(password)
password_list = [] # empty list
for n in range(0, len_password):
    password_list += password[n]
print(f"List of characters for password: {password_list}")


# shuffling_the_password_characters
'''
ALGORITHM:
1. When one first index, swap it with random n
2. Do the same till the last index
'''

len_passwordlist = len(password_list)
for n in range(0, len_passwordlist):
    rand_n = random.randint(0, len_passwordlist-1)
    temp = password_list[n]
    password_list[n] = password_list[rand_n]
    password_list[rand_n] = temp
print(f"The shuffled list of password: {password_list}")
