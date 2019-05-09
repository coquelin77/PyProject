import sys
class Solution(object):
    def happy(self, festival):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        p = '祝现场和洗衣机前的观众朋友们' + festival + '快乐'
        return p


if __name__ == '__main__':
    a = Solution()
    f = sys.argv[1]
    print(a.happy(f))
