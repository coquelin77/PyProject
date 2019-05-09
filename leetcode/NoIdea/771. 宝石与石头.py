class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(S.count(i) for i in J)

if __name__ == '__main__':
    a="aA"
    b="aAAbbbb"
    f= Solution()
    p=f.numJewelsInStones(a,b)
    print(p)