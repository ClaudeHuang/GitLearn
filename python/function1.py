def say_hello():
	print('hello world')

say_hello()
say_hello()

def print_max(a,b):
	if a > b:
		print(a,'is maximum')
	elif a == b:
		print(a,'is equal to',b)
	else:
		print(b,'is maximum')


print_max(3,4)

x=3
y=5

print_max(x,y)