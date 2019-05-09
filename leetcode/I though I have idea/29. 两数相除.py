'''给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2'''


class Solution:
    def divide(self, dividend, divisor):
        result = 0
        if dividend == 0 or divisor == 0:
            return 0
        if dividend > 0 and divisor > 0:  # 全正
            while dividend >= divisor:
                dividend = dividend - divisor
                result = result + 1
            return result
        elif dividend < 0 and divisor < 0:  # 全负
            dividend = abs(dividend)
            divisor = abs(divisor)
            while dividend >= divisor:
                dividend = dividend - divisor
                result = result + 1
            return result
        elif dividend > 0 and divisor < 0:  # 正负
            divisor = abs(divisor)
            while dividend >= divisor:
                dividend = dividend - divisor
                result = result + 1
            return 0 - result
        elif dividend < 0 and divisor > 0:  # 负正
            dividend = abs(dividend)
            while dividend >= divisor:
                dividend = dividend - divisor
                result = result + 1
            return 0 - result


if __name__ == '__main__':
    dd=-2147483648
    dr  =-1
    a = Solution()
    p = a.divide(dd, dr)
    print(p)
