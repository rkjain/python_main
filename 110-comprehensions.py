# List Comprehension
some_numbers = list(range(1,20))


just_numbers = [number / 2 for number in some_numbers]

# Condtitionals in list comprehension
alt_numbers = [number for number in some_numbers if number % 3 == 0]
even_numbers = [ number if number % 2 == 0 else False for number in some_numbers ]

# Genearator expression
my_new_list = (number + 1 for number in some_numbers)
print(list(my_new_list))

# Set Comprehension
set_a = { number for number in some_numbers }

# Dict Comprehension
dict_a = { f"key_{number}": number for number in some_numbers }


print(set_a)
print(dict_a)
print(just_numbers)
print(alt_numbers)
print(even_numbers)
