#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#購買者記帳輸入
products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	products.append([name, price])
print(products)

#印出所有購買紀錄
for s in products:
	print(s[0], '的商品價格為', s[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #encoding=中文字（編碼）
	f.write('品名,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')