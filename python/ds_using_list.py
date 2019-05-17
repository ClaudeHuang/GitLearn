shoplist = ['apple','mango','carrot','banana']

print('i have',len(shoplist),'items to purchase')

print('these items are:',end=' ')
for item in shoplist:
	print(item, end=' ')

print('\ni also have to buy rice.')
shoplist.append('rice')
print('my shopping list is now', shoplist)

print('i will sort my list now')
shoplist.sort()

	# 使用sort方法对列表进行排序
	
print('sorted shopping list is',shoplist)

print('the first item i will buy is',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('i brought the', olditem)
print('my shopping list is now', shoplist)