# class Solution:
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         I = 1
#         V = 5
#         X = 10
#         L = 50
#         C = 100
#         D = 500
#         M = 1000
#         list(s)
#         result = 0
#         for i in range(0, len(s) - 1):
#             if (s[i] == 'I'):
#                 result = result + 1
#             elif (s[i] == 'V' and s[0]!='V'):
#                 if (s[i - 1] == 'I'):
#                     result = result - 1
#
#                 result = result + 5
#             elif (s[i] == 'X'):
#                 if (s[i - 1] == 'I' and s[0]!='I'):
#                     result = result - 1
#
#                 result = result + 10
#             elif (s[i] == 'L'):
#                 if (s[i - 1] == 'X'):
#                     result = result - 10
#
#                 result = result + 50
#             elif (s[i] == 'C'):
#                 if (s[i - 1] == 'X'):
#                     result = result - 10
#
#                 result = result + 100
#             elif (s[i] == 'D'):
#                 if (s[i - 1] == 'C'):
#                     result = result - 100
#
#                 result = result + 500
#             elif (s[i] == 'M'):
#                 if (s[i - 1] == 'C'):
#                     result = result - 100
#
#                 result = result + 1000
#         return result

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  # 建立map
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
        return ans

if __name__ == '__main__':
    s ='MCMXCIV'
    a = Solution()
    a.romanToInt(s)