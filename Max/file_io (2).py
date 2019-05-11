import io
#file = open('%PATH%','r')
#file.read()
#file.close()
###########################优化###############################
#try:
#    file = open('%PATH%', 'r')
#    print(file.read())
#finally:
#    if file:
#        file.close()
###########################优化###############################
#with open('./example.txt', 'r') as file:
#    print(file.read())
#for line in file.readlines():
#    print(line.strip())
#file = open('./example.txt', 'rb')#读取二进制文件
#file.read()
#file.close()
##########################################################
#file = open('./example.txt', 'r',encoding='gbk')#读取二进制文件
#file.read()
#file.close()
##########################同理################################
with open('./example.txt','wb',encoding='UTF-8') as file:
    file.write('Hello Wolrd')