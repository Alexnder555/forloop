numbers_list = []
even_integers = []
odd_integers = []

for number in range(301):
  numbers_list.append(number)
print(numbers_list)

for number in numbers_list:
  if number % 2 == 0:
      even_integers.append(number)
print("Even integers")
print(even_integers)
for number in numbers_list:
  if number % 2 != 0:
    odd_integers.append(number)
print("Odd integers")
print(odd_integers)