number = 23
running = True

while running:
	guess = int(input('enter an integer : '))

	if guess == number:
		print('congratulations you guess it!')
		running = False
	elif guess < number:
		print('no it is a little higher than you input')
	else:
		print('no it is a little lower than you input')
else:
	print('the while loop is over')

print('done')