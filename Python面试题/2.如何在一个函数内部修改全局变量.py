a=1
def test():
    global a   #利用global 修改全局变量
    a=2
    print(a)
    return
test()