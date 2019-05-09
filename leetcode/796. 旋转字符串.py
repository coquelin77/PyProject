'''给定两个字符串, A 和 B。
A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。
示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true
示例 2:
输入:
输出: false
注意：
A 和 B 长度不超过 100。'''


# class Solution:
#     def rotateString(self, num1, num2):
#         n1 = list(num1)
#         n2 = list(num2)
#         if len(n1) == len(n2):
#             for i in range(0, len(num1) - 1):
#                 t = n2.pop(0)
#                 n2.append(t)
#                 if n1 == n2:
#                     return True
#             return False
#         else:
#             return False


#     def rotateString(self, A,B ) -> 'bool':
#         if len(A) == len(B):#长度一样才有可能相等
#             for i in range(0,len(B)):
#                 j=B[0]
#                 del B[0]
#                 B.append(j)
#                 if A==B:
#                     return True
#             return False
#         else:
#             return False
# if __name__ == '__main__':
#     A = 'abcde'
#     B = 'abced'
#     if len(A) == len(B):#长度一样才有可能相等
#         for i in range(0,len(B)):
#             j=B[0]
#             del B[0]
#             B.append(j)
#             if A==B:
#                 return True
#         return false
#     else:
#         return false
#
# class text(object):
#     def round(self,nums1,nums2):
#         list(nums1)
#         list(nums2)
#         for i in range(0,len(nums2)):
#             t = nums2[i - 1]
#             del nums2[i - 1]
#             nums2.append(t)
#             if nums1 == nums2:
#                 return True
#         return False
# if __name__ == '__main__':
#     nums1='abcde'
#     nums2 = 'abced'
#     a=text()
#     p=a.round(nums1,nums2)
#     print(p)
class Solution:
    def rotateString(self, num1, num2):
        n1 = list(num1)
        n2 = list(num2)
        if len(n1) == len(n2) and num1 != "" and num2 != "":
            for i in range(0, len(num1) - 1) :
                t = n2.pop(0)
                n2.append(t)
                if n1 == n2:
                    return True
            return False
        elif num1 == "" and num2 == "":
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    A = ''
    B = ''
    p = a.rotateString(A, B)
    print(p)
    print(A == '')