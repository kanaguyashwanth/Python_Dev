# CODING EXERCISE: TIP CALCULATOR

'''
Welcome to the tip calculator.
What was the total bill? $124.56
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
OUTPUT: Each person should pay: $19.93 (Only 2 decimal places)
'''

print ('Welcome to the tip calculator.\n')
total_bill = float(input('What was the total bill: \n'))
perc = int(input("What percentage would you like to give? \n"))
n_ppl = int(input("How many people to split the bill? \n"))

each_pay = total_bill + ( (total_bill * perc) / 100 ) / n_ppl
print(round(each_pay,2))