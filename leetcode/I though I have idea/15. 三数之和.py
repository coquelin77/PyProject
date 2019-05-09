'''给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]'''


class Solution:
    def threeSum(self, nums):
        set(nums)
        can = []
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        may = [nums[i], nums[j], nums[k]]
                        can.append(may)
        return can


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    a = Solution()
    p = a.threeSum(nums)
    print(p)
