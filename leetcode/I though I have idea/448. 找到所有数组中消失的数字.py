'''给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]'''


# class Solution:
#     def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
#         num = list(set(nums))
#         max = 0
#         maxs = []
#         diff=[]
#         for i in num:
#             if i > max:
#                 max = i
#             for j in range(1, max + 1):
#                 maxs.append(j)
#             for n in maxs:
#                 if n in num:
#                     pass
#                 else:
#                     diff.append(n)
#             return diff
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        a = nums.copy()
        for i in a:
            nums[i - 1] = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                r.append(i + 1)
        return r


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    a = Solution()
    p = a.findDisappearedNumbers(nums)
    print(p)
