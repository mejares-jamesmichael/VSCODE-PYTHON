def add(*args):
    sum = 0
    for char in args:
        sum += char
    return sum

print(add(1, 2, 3, 4, 5))
print(add(7, 4, 3))
print(add(1, 3, 4, 5))