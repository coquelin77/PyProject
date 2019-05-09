'''给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true'''


# class Solution:
#     def canConstruct(self, ransomNote: 'str', magazine: 'str') -> 'bool':
#         pass
#
# if __name__ == '__main__':
#     ransomNote = "aa"
#     magazine = "aa"
#     r = list(ransomNote)
#     m = list(magazine)
#     for i in range(0, len(m) - 1):
#         for j in range(0, len(r)):
#             if m[i] == r[j]:
#                 pass
#             else:
#                 m += 1
#     if i == len(m) or j == len(r):
#         print('1')
#     else:
#         print('2')

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        have_done=[]
        for i in range(len(ransomNote)):
            if ransomNote[i] not in have_done:
                if ransomNote.count(ransomNote[i])<=magazine.count(ransomNote[i]):
                    pass
                else:
                    return False
                have_done.append(ransomNote[i])
        return True