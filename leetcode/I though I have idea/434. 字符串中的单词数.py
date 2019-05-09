'''统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5'''


class Solution:
    def countSegments(self, s: str) -> int:
        # slist = list(s)
        # n = 1
        # if len(slist) == 0 or slist[0] == ' ' or slist[-1] == ' ':
        #     return 0
        #
        # for i in slist:
        #     if i == ' ':
        #         n += 1
        # return n
        slist= list(s)
        #list = [1, 1, 1, 1, 1, 1, 2, 3, 4, 4, 5, 1, 2]
        i = 0
        dupe = False
        n=1
        while i < len(slist) - 1:
            if slist[i] == slist[i + 1]:
                del slist[i]
                dupe = True
            elif dupe:
                del slist[i]
                dupe = False
            else:
                i += 1
        if len(slist) == 0 or slist[0] == ' ' or slist[-1] == ' ':
            return 0

        for i in slist:
            if i == ' ':
                n += 1
        return n

if __name__ == '__main__':
    words = "Hello, my name is John"
    a = Solution()
    p = a.countSegments(words)
    print(p)
