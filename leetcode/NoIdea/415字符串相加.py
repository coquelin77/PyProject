'''给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。'''


# class Solution(object):
#     def addStrings(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         return str(eval(num1) + eval(num2))#作弊方法
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        jin = 0
        res = ""
        i = 0
        j = 0
        while i < len(num1) and j < len(num2):
            tmp = int(num1[i]) + int(num2[j]) + jin
            res += str(tmp % 10)
            jin = tmp / 10
            i += 1
            j += 1

        while i < len(num1):
            tmp = int(num1[i]) + jin
            res += str(tmp % 10)
            jin = tmp / 10
            i += 1

        while j < len(num2):
            tmp = int(num2[j]) + jin
            res += str(tmp % 10)
            jin = tmp / 10
            j += 1
        if jin:
            res += str(jin)
        return res[::-1]


if __name__ == '__main__':
    num1 = ['1', '3', '5', '7', '9']
    num2 = ['2', '4', '6', '8', '0']
    n1 = "233"
    n2 = "144"
    a = Solution()
    p = a.addStrings(n1, n2)
    print(p)
    q = a.addStrings(num1, num2)
    print(q)
