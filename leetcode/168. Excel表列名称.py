class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            n, mod = divmod(n, 26)
            if mod == 0:
                mod = 26
                n -= 1
            res += chr((mod + 64))
        return res[::-1]


if __name__ == '__main__':
    a = Solution()

    p = a.convertToTitle(1)
    print(p)
    p = a.convertToTitle(-1)
    print(p)
    p = a.convertToTitle(256)
    print(p)
    p = a.convertToTitle(65536)
    print(p)