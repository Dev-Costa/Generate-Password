from random import randint

size = 10

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
terms = letters + numbers

password = ""
for i in range(size):
	random_index = randint(0, len(terms) - i)
	while (terms[random_index] in password):
		random_index = randint(0, len(terms) - i)

	password += terms[random_index]

print(password)