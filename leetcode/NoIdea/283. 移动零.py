'''给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。'''


# class Solution:
#     def moveZeroes(self, nums: 'List[int]') -> 'None':
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         l = len(nums)
#         l = len(nums)
#         for i in range(0, l):
#
#             if nums[i] == 0:
#                 n=nums[i]
#                 nums.append(n)
#                 n = nums.pop(i)
#         return nums
# if __name__ == '__main__':
#     nums=[0,1,0,3,12]
#     a=Solution()
#     p=a.moveZeroes(nums)
#     print(p)
class Solution:
    def moveZeroes(self, nums):
        """
        思路：将所有非0元素移到前面，再将空着的全填为0
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 统计非0元素个数
        count = 0
        for i in range(0, len(nums)):
            if (nums[i] != 0):
                nums[count] = nums[i]
                count += 1
        for j in range(count, len(nums)):
            nums[j] = 0
        return nums
if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    a=Solution()
    p=a.moveZeroes(nums)
    print(p)