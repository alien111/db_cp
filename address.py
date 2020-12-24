import random

streets = ["Zelenaya", "Lenina", "Sadovaya", "Pervomayskaya", "Parkovaya", "Lesnaya", "Mira", "Pushkina", "Dlinnaya", "Slavnaya"]
used = []

for i in range(10):
	while(True):
		rn = random.randint(0, 10)
		if (rn not in used):
			break

	print(streets[rn] + ", " + str(random.randint(1, 100)), end = '')
	if (random.randint(0, 1) == 1):
		print(', bld ' + str(random.randint(1, 5)))
	else:
		print()
	used.append(rn)
