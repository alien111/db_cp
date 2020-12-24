import random
import string

_string = string.ascii_letters + "0123456789"

for i in range(5):
	print(str(i + 1) + ': ', end = '')
	for i in range(10):
		print(random.choice(_string),end = "")
	print(" ", end = "")
	print(random.randint(1000000000,9999999999))