import string
import random

_string = string.ascii_letters + "0123456789"
for i in range(10):
	print(random.choice(_string),end = "")

print()