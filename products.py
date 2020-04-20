products = []
while True:
	name = input('Please input the name of product:')
	if name == "q":
		break
	price = input('Please input the price of product:')
	price = int(price)
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

#Open and prepare to write the item stored in program into the file "products.csv **If the file not existing, then it will create a new file
#"with" is python special function which all code will close after leaving with
with open("products.csv", "w", encoding='utf-8') as f:
	f.write('product','price\n')
	#for loop to write in each item in products
	for p in products:
		#Combine all str in the parameter to 1 big str, then write into f *actual writing
		f.write(p[0] + "," + str(p[1]) + '\n')


