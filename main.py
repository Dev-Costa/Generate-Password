from random import randint

size = 10

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
terms = letters + numbers

password = ""
for i in range(size):
	random_index = randint(0, len(terms) - i)
	random_c = terms[random_index]

	password += random_c

	terms = terms.replace(random_c, "")

print(password)