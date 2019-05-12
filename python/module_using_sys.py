import sys
	# 内置模块引用

print('the command line arguments are:')
for i in sys.argv:
	print(i)

print('\n\nthe pyhonpath is', sys.path, '\n')