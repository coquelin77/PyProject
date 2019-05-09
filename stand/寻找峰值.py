class V(object):
    def baidu(self, x):
        # bai=innum//100
        # shi=(innum-(bai*100))//10
        # ge=innum-(bai*100)-(shi*10)
        #
        # return bai*shi*ge
        mark = 0
        if x < 0:
            mark = 1
            x = 0 - x
        bai = x // 100
        shi = (x - (bai * 100)) // 10
        ge = x - (bai * 100) - (shi * 10)
        bai, shi, ge = ge, shi, bai
        result = bai * 100 + shi * 10 + ge
        if mark == 1:
            result = 0 - result

        return result


if __name__ == '__main__':
    # innum = 252
    # innums = 202
    a = V()
    # print(a.baidu(innum))
    # print(a.baidu(innums))
    num = int(input("请输入数字"))
    print(a.baidu(num))
