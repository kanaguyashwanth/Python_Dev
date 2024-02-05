# CODING EXERCISE: Your Life in Weeks

'''
What is your current age?

OUTPUT: You have x Days, y Weeks and z Months left
ASSUMPTION: 1 Year = 365 Days
            1 Year = 52  Weeks
            1 Year = 12  Months
            Assuming that we live till 90 years.
'''

age = int (input("What is your age? "))
x_age = int (input("How long u gonna live?"))
rem_age = x_age - age

days_rem = rem_age * 365	# Days
weeks_rem = rem_age * 52	# Weeks
months_rem = rem_age * 12	# Months

message = f"You have {days_rem} days, {weeks_rem} weeks and {months_rem} months left"
print(message)
