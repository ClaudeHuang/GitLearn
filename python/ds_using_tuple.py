zoo = ('python','elephant','penguin') 

	# 代表一个元组，而非列表，其中的内容不可改变
print('number of animals in the zoo is',len(zoo))

	# 元组中的元组依然是元组，特性不会改变

new_zoo =('monkey','camel',zoo)

print('number of cages in the new zoo is', len(new_zoo))
print('all animals in new zoo are', new_zoo)
print('animals brought from old zoo are', new_zoo[2])
print('last animals brought from old zoo is', new_zoo[2][2])
print('number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))