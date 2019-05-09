class Solution:

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        result = 0
        if length == 1:
            result = ord(s) - 64
        else:
            for i in range(length):
                index = length - 1 - i
                val = s[i]
                result += 26 ** index * (ord(val) - 64)

        return result


if __name__ == '__main__':
    alphabet = 'A'
    a = Solution()
    p = a.titleToNumber(alphabet)
    print(p)
