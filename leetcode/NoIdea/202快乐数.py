'''编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例:

输入: 19
输出: true
解释:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1'''


class Solution:
    def __init__(self):
        self.base = {4, 16, 37, 58, 89, 145, 42, 20}

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sums = sum(map(lambda x: x ** 2, map(int, str(n))))
        if sums in self.base:
            return False
        if sums != 1:
            return self.isHappy(sums)
        else:
            return True


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = 0
        while result != 1 and result != 4:
            result = 0
            n = str(n)
            for i in n:
                result += int(i) ** 2
            n = result
        if result == 1:
            return True
        return False


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flags = []
        while n != 1:
            tmp = 0
            for char in str(n):
                tmp += int(char) ** 2
            if tmp not in flags:
                flags.append(tmp)
                n = tmp
            else:
                return False
        return True
