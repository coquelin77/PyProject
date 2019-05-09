'''实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1'''
if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    #h,e,l,l,o
    #l,l
    i=0
    j=0
    list(haystack)
    list(needle)
    while True:
        if(haystack[i]==needle[j]):
            #i=i+1
            j=j+1
'''class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        
        l = len(needle)
        L = len(haystack)
        if l > L: return -1
        
        
        for i in range(L-l+1):
            if haystack[i] == needle[0]:
                
                tag=1
                for j in range(l):
                    if haystack[i+j] != needle[j]:
                        tag=0
                        break
                
                if tag:
                    return i
                else:
                    pass
                
        return -1
'''