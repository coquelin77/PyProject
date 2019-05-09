'''给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。



示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。'''


# class Solution:
#     def findTheDifference(self, s: 'str', t: 'str') -> 'str':
#         #pass
#         ss=list(s)
#         tt=list(t)
#         for i in tt:
#             if i not in ss:
#                 return i
# if __name__ == '__main__':
#     s = "abcd"
#     t = "abcde"
#     a=Solution()
#     p=a.findTheDifference(s,t)
#     print(p)
#解1:s，t分别排序好，用指针从头开始逐一比对，发现不同即返回
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    a=Solution()
    p=a.findTheDifference(s,t)
    print(p)
#
#解2: 用dict，分别把s，t存成dict，若t中有key是s中没有的，或者相同的key，t的value比s大，那么返回该key


# class Solution:
#     def findTheDifference(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         a = {}
#         b = {}
#         for i in s:
#             if i in a:
#                 a[i] += 1
#             else:
#                 a[i] = 1
#         for i in t:
#             if i in b:
#                 b[i] += 1
#             else:
#                 b[i] = 1
#         for i in b:
#             if i not in a or b[i] != a[i]:
#                 return i
