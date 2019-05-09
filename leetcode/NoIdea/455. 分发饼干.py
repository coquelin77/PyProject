class Solution:
    def findContentChildren(self, g, s):
        n1 = len(g)
        n2 = len(s)
        g.sort()
        s.sort()
        cnt, i, j = 0, 0, 0
        while(i < len(g) and j < len(s)):
            if s[j] >= g[i]:
                i += 1
                j += 1
                cnt += 1
            else:
                j += 1
        return cnt


if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]
    a = Solution()
    p = a.findContentChildren(g, s)
    print(p)
