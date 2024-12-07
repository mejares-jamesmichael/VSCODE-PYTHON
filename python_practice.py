# Create a function that takes two numbers as arguments and returns their sum.

# def add (number1, number2):
#     sum = number1 + number2 
#     return sum

# number1 = int(input('Enter 1st number: '))
# number2 = int(input('Enter 2nd number: '))


# # print(add(number1,number2))
# print(f'Sum = {add(number1, number2)}')


# Write a function that takes an integer minutes and converts it to seconds.

# def convert (minutes):
#     seconds = 60 * minutes
#     return seconds
    
# minutes = int(input("Enter number of minutes: "))

# print (f"Minutes to seconds: {convert(minutes)}\n")

#Create a function that takes the age in years and returns the age in days.

def age_conversion(age_year):
    age_days = 365 * age_year
    return age_days

age_year = int(input("Enter your age: "))

print (f"Age to days: {age_conversion(age_year)}")