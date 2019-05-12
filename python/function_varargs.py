def total(a = 5, *numbers, **phonebook):
	# *后所有的参数都会进入‘number’的元组中
	# **同理
	print('a', a)

	#遍历元组中所有项
	for single_item in numbers:
		print('single_item',single_item)

	#遍历字典中所有项
	for first_part, second_part in phonebook.items():
		print(first_part,second_part)

print(total(10,1,2,3,jack=1123,john=2231,inge=1560))