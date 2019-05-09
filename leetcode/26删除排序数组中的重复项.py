'''给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。'''
'''/* 方法：双指针法 算法:数组完成排序后，我们可以放置两个指针i 和j，其中i是慢指针，而j是快指针。
 只要 nums[i] = nums[j]，我们就增加 j以跳过重复项。当遇见nums[i] ≠ nums[j]时， 跳过重复项的运算已经结束，此时把值赋值到数组的下一个元素，即i递增1。
 重复此过程直至达到数组的末尾为止。 */'''


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return
        i = 0
        j = i + 1
        while True:
            if i > len(nums) or j > len(nums):
                return j, nums

            while nums[i] == nums[j]:
                nums.append(nums.pop(j))
                if len(nums) == 2 and nums[i] == nums[j]:
                    nums.pop(-1)
                    return j, nums
                elif len(nums) == 2 and nums[i] < nums[j]:
                    return j, nums
            if nums[i] < nums[j]:
                i = i + 1
                j = j + 1
                if j == len(nums):
                    return j, nums
            elif nums[i] > nums[j]:
                return j, nums


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    stand = [1, 2]
    s2 = [1, 1, 1]
    a = Solution()
    p = a.removeDuplicates(nums)
    print(p)
    q = a.removeDuplicates(stand)
    print(q)
    r = a.removeDuplicates(s2)
    print(r)
