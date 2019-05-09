from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    time15 = 1
    sum_of_num = 0
    fvar = 0
    while time15<=5:
        fvar = raw_input("请输入：")
        if fvar>0:
            sum_of_num=fvar
    print('输入的数中大于0的数之和是:'+str(sum_of_num))