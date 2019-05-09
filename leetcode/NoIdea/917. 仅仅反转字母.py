'''给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。



示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"


提示：

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S 中不包含 \ or "'''


# class Solution(object):
#     def reverseOnlyLetters(self, S):
#         """
#         :type S: str
#         :rtype: str
#         """
#
#
# if __name__ == '__main__':
#     ip = "Test1ng-Leet=code-Q!"
#     op = "Qedo1ct-eeLg=ntse-T!"
#     il = list(ip)
#     ol = list(op)
#     for i in range(0, len(ip)):
#         if (str(il[i]) <= 'Z' and str(il[i]) >= 'A') or (str(il[i]) <= 'z' and str(il[i]) >= 'a'):
#             pri=il.pop(0)
#             il.append(pri)
#         else:
#             i=i+1
#     print(il)
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        i = 0
        j = len(S) - 1
        while i < j:
            while i < j and not S[i].isalpha():
                i += 1
            while i < j and not S[j].isalpha():
                j -= 1

            if i < j:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
