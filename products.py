import os # operating system

#Read file
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf=8') as f:
		for line in f:
			if 'Products,Price' in line:
				continue # continue to loop
			name, price = line.strip().split(',')
			products.append([name, price])
	return products #Var 'products' now contain all the data from above function

#let the user input
def user_input(products):
	while True:
		name = input('please input the product name: ')
		if name == 'q':
			break
		price = input('please input the product price: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products #as appended fomr data, need to use return function to save

# print all the purchase record
def print_products(products):
	for p in products:
		print(p[0], 'price is', p[1]) #no need to return to save as only use for loop to print

# write into the file
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('Products,Price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # to check if the file exist 
		print('Yes the file exist')
		products = read_file(filename)
	else: 
		print('Cant find the file')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()