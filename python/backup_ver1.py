import os
import time

# 1.将要备份的文件及目录(文件夹)放入同一列表中
source = ['/Users/claudehuang/swat/notes']
	# 目录中有空格则需要使用双引号

# 2.备份文件至主文件夹目录中
target_dir = '/Users/claudehuang/swat/backup'

# 3.备份的压缩文件文件名为日期+时间
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
	# 注意 os.sep 变量 - 它会根据你的操作系统变换目录分隔符，
	# 比如 GNU/Linux，Unix，macOS 下是 '/', Windows 下就会是 '\\'。
	# 使用 os.sep 代替直接用某个分割符可以让我们的程序具有移植性，也就是可能跨所有平台使用。


# *如果目录不存在则可以重新创建
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

# 4.使用系统zip命令进行压缩备份
zip_command = 'zip -r {0} {1}'.format(target,''.join(source))

# 运行
print('zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:  #os.system命令运行成功回返回0
	print('successful backup to', target)
else:
	print('backup failed')