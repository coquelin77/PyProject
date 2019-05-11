# 1创建一个空列表，命名为names,往里面添加old_driver,rain,jack,shanshan,peiqi,black_girl 元素
names = []
add = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']
_insert = ['oldboy', 'oldgirl']
for i in range(1, 6):
    names.append(add[i])
print('1', names)
# 2往names列表里black_girl前面插入一个alex
names.insert(4, 'alex')
print('2', names)
# 3把shanshan的名字改成中文，姗姗
names[4] = '珊珊'
print('3', names)
# 4往names列表里rain的后面插入一个子列表，[oldboy, oldgirl]
names.insert(1, _insert)
print('4', names)
# 5返回peiqi的索引值
print('5', names.index('peiqi'))
# 6创建新列表[1,2,3,4,2,5,6,2],合并入names列表
newable = [1, 2, 3, 4, 2, 5, 6, 2]
names.extend(newable)
print('6', names)
# 7取出names列表中索引4-7的元素
for j in range(4, 8, 1):
    catch = names[j]
    print('7', catch)
# 8.取出names列表中索引2-10的元素，步长为2
for p in range(2, 11, 2):
    match = names[p]
    print('8', match)
# 9.取出names列表中最后3个元素
for q in range(len(names - 4), len(names - 1), 1):
    laugh = names[q]
    print('9', laugh)
# 10.循环names列表，打印每个元素的索引值，和元素
for circle in range(0,len(names-1)):
    print(names[circle],circle)
# 11.循环names列表，打印每个元素的索引值，和元素，当索引值 为偶数时，把对应的元素改成-1
for m in  range(0,len(names-1)):
    print(m,names[m])
    if m%2==0:
        names[m]=-1
    print(11,names)
# 12.names里有3个2，请返回第2个2的索引值。不要人肉数，要动态找(提示，找到第一个2的位置，在此基础上再找第2个)
names = ['old_driver','rain','jack','shanshan','peiqi','black_girl',1,2,3,4,2,5,6,2]
first_index = names.index(2)
new_list = names[first_index+1:]
second_index = new_list.index(2)
second_val = names[first_index+second_index+1]
print(new_list,first_index,second_index)
print("second values", second_val)
#13.现有商品列表如下:
'''
    products = [ ['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799] ]
    需打印出这样的格式：

    ---------商品列表----------
    
0. Iphone8    6888
    
1. MacPro    14800
    
2. 小米6    2499
    
3. Coffee    31
    
4. Book    80
    
5. Nike Shoes    799
'''
products = [['Iphone',6888],['MacPro',14800],['小米',2499],['Coffee',31],['Book',80],['NikeShoes',799]]
print("-------- 商品列表 ---------")
for index, i in enumerate(products):
    print("%s. %s   %s" %(index,i[0],i[1]))
#14
exit_flag = False # 标志位，控制while循环
products = [['Iphone',6888],['MacPro',14800],['小米',2499],['Coffee',31],['Book',80],['NikeShoes',799]]
shopping_cart = [] # 创建购物车
while not exit_flag:
    print("--------- 商品列表 ---------")
    for index, i in enumerate(products):
        print("%s. %s  %s" %(index, i[0],i[1]))
    choice = input("请问你想买什么:")
    if choice.isdigit():
        choice = int(choice)
        if choice >=0 and choice < len(products):
            print("%s. %s  %s" %(index,i[0],i[1]))
            shopping_cart.append(products[choice])
        else:
            print("您输出的数值有误！")
    elif choice == "q":
        exit_flag = True
        if len(shopping_cart) > 0:
            print("--------- 您的购物车商品 ----------")
        for index, i in enumerate(shopping_cart):
            print("%s. %s %s" %(index,i[0],i[1]))
    else:
        print("您输出的数值有误！")
#