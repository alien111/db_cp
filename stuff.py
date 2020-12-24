import random

productPrice = [55, 309, 1190, 38900, 417, 1695, 155, 603, 1614, 2279, 251]

transactions = []

for i in range(25):
	productNumber = random.randint(0, 10)

	billNumber = random.randint(0, 19)

	quantity = random.randint(1, 10)

	print(str(i + 1) + ": " + str(productNumber + 1) + ' ' + str(quantity) + ' ' + str(billNumber + 1) + ' ' + str(productPrice[productNumber] * quantity))

