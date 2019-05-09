# '''给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: 6
# 示例 2:
#
# 输入: [1,2,3,4]
# 输出: 24
# 注意:
#
# [-4,-3,-2,-1,60]
# 给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。'''
#
#
# class Solution:
#     def maximumProduct(self, nums):
#         # if len(nums)<3:
#         #     return
#         # elif len(nums)==3:
#         #     result = nums[0]*nums[1]*nums[2]
#         #     return result
#         # else:
#         #     a = max(nums)
#         #     nums.remove(a)
#         #     b = max(nums)
#         #     nums.remove(b)
#         #     c = max(nums)
#         #     nums.remove(c)
#         #     return a*b*c
#
#         # a = 0
#         # b = 0
#         # c = 0
#         # x = 0
#         # y = 0
#         # z = 0
#         # maxbig =[]
#         # maxsmall=[]
#         # for i in range(0, len(nums)):
#         #     if nums[i] > 0:
#         #         pass
#         #     elif nums[i] < 0:
#         #         if nums[i]<maxsmall:
#         #             maxsmall.append(nums[i])
#         #     else:
#         #         pass
#         if len(nums)<3:
#             return
#         elif len(nums)==3:
#             result = nums[0]*nums[1]*nums[2]
#             return result
#         # else:
#         #     absolutely = abs(nums)
#         #     a = max(absolutely)
#         #
#         #     b = max(nums)
#         #
#         #     c = max(nums)
#         #
#         #     return a*b*c
#
#         '''分两种情况：1、三个正数 2、一个最大正数，两个最大负数，然后比较两种得到数据的大小来得出最终返回的最大值结果'''
#
# if __name__ == '__main__':
#     nums1 = [1, 2, 3, 4]
#     nums2 = [-4, -3, -2, -1, 60]
#     x = Solution()
#     n = x.maximumProduct(nums1)
#     m = x.maximumProduct(nums2)
#     print(n, m)
class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        result = []
        result.append(nums[-1] * nums[-2] * nums[-3])
        result.append(nums[-1] * nums[0] * nums[1])
        return max(result)
if __name__ == '__main__':
    nums1 = [1, 2, 3, 4]
    nums2 = [-4, -3, -2, -1, 60]
    x = Solution()
    n = x.maximumProduct(nums1)
    m = x.maximumProduct(nums2)
    print(n, m)
