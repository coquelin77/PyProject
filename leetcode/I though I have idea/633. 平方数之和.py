'''给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5


示例2:

输入: 3
输出: False'''


class Solution:
    def judgeSquareSum(self, c: 'int') -> 'bool':
        if c == 1:
            return True
        for i in range(0, c):
            for j in range(0, c):
                if (i * i) + (j * j) == c:
                    return True
        return False


if __name__ == '__main__':
    a = Solution()

    c = 5
    p = a.judgeSquareSum(c)
    print(p)

    c = 4
    p = a.judgeSquareSum(c)
    print(p)

    c = 1
    p = a.judgeSquareSum(c)
    print(p)
