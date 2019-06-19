import os
os.name # 操作系统类型
os.uname()#获取详细的系统信息
os.environ#查看系统环境变量
os.environ.get('PATH')#获取环境变量的值
os.path.abspath('.')# 查看当前目录的绝对路径
os.path.join('/Users/michael', 'testdir')# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir('/Users/michael/testdir')# 创建一个目录
os.rmdir('/Users/michael/testdir')# 删掉一个目录
os.path.split('/Users/michael/testdir/file.txt')#拆分一个路径为两部分
os.path.splitext('such file')#得到文件扩展名
os.rename('test.txt', 'test.py')# 对文件重命名
os.remove('test.py')# 删掉文件

