products = []
while True:
	name = input("請輸入商品名稱(q to quit) :")
	if name == "q":
		break
	price = int(input("請輸入商品價格 :"))
	products.append([name, price])

print(products)

# for p in products:
# 	print(p)
# 	print(p[0])

with open("products.csv", "w", encoding = "utf-8") as file:
	file.write("商品,價格\n")
	for p in products:
		file.write(p[0] + "," + str(p[1]) + "\n") #只能用逗點