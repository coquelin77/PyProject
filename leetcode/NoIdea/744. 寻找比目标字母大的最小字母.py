'''给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。

数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。

示例:

输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "c"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "d"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "g"
输出: "j"

输入:
letters = ["c", "f", "j"]
target = "j"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "k"
输出: "c"'''


# class Solution:
#     def nextGreatestLetter(self, letters: 'List[str]', target: 'str') -> 'str':
#         if target<letters[0]:
#             for j in letters:
#                 if target < j:
#                     return j
#         elif target>letters[-1]:
#             for j in letters:
#                 if target > j:
#                     return j
#         else:
#             for i in range(0,len(letters)-1):
#                 if letters[i]==target:
#                     return letters[i+1]
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for x in letters:
            if x >target:
                return x
        return letters[0]
if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "c"
    a = Solution()
    p = a.nextGreatestLetter(letters, target)
    print(p)
