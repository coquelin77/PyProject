class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:#如果是负数，不可能是回文数
            return False
        else:
            y = str(x)[::-1]#y是x的倒序输出
            if y == str(x):#如果y==x，返回真
                return True
            else:#否则返回假
                return False
if __name__ == '__main__':
    x = 12321
    y =123421
    a = Solution()
    print(a.isPalindrome(x))
    print(a.isPalindrome(y))