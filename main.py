from random import randint

def generate_password(size = 10) -> str:
	letters = "abcdefghijklmnopqrstuvwxyz"
	numbers = "0123456789"
	terms = letters + numbers

	password = ""
	for i in range(size):
		random_index = randint(0, len(terms) - i)
		random_c = terms[random_index]

		password += random_c

		terms = terms.replace(random_c, "")

	return password

print(generate_password())