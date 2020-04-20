products = []
while True:
	name = input('Please input the name of product:')
	if name == "q":
		break
	price = input('Please input the price of product:')
	#the most complex but comprehensive coding
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)
	#Cleaner coding
	#p = [name, price]
	#products.append(p)
	#Most clean coding
	products.append([name, price])

print(products)

#print our every item in list of products
for p in products:
	print(p)

#print out every item in list of products' first column
for p in products:
	print(p[0])

#print out every item in list of products' first column and also showing the second column of price
for p in products:
	print(p[0], "cost is", p[1])

	

