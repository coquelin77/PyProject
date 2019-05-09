'''给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21'''
class Solution(object):
    def reverse(self, x):
        if x >= 0:#如果是正数，
            x = str(x)#防止超出int范围
            x = x[::-1]#用切片的方法倒序输出
        else:
            x = str(x)#防止超出int范围
            x = x[1:]#去符号
            x = '-' + x[::-1]#加符号用切片的方法倒序输出
        x = float(x)#转换为浮点数
        if (x < float(-2 << 30)) | (x >= float(2 << 30)):#判断浮点数是否大于int范围
            return 0
        x = int(x)#转换为int
        return x