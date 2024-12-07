sum = 0
while True:
    number = 0
    number = int(input("Enter a number: "))
    if number == 0:
        break
    sum += number

print(f"Sum: {sum}")