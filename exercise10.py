user_dictionary = {}
user_string = (input('input: '))

for char in user_string:
    if char in user_dictionary:
        user_dictionary[char] += 1
    else:
        user_dictionary[char] = 1

print(f"ouput: {user_dictionary}")