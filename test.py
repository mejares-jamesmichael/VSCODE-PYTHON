def calculate_avaerage(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = []
user_input = (input("Enter a number: "))

while user_input.isnumeric():
    numbers.append(int(user_input))
    user_input = input("Enter a number: ")

print ("Average: ", calculate_avaerage(numbers))