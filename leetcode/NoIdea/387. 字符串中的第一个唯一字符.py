'''给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。'''


# class Solution:
#     def firstUniqChar(self, s: 'str') -> 'int':
#         pass
# if __name__ == '__main__':
#     s = "loveleetcode"
#     l= list(s)
#     for i in range(0,len(l)-1):
#         if l[i] in range(l[i+1],len(l)-1):
#             pass
#         else:
#             print(i)
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1=list(set(s))
        list1.sort(key=s.index)
        for each in list1:
            if s.count(each)==1:
                return s.index(each)
        return -1