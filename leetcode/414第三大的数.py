'''给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
示例 2:

输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3:

输入: [2, 2, 3, 1]

输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。
'''


class Solution:
    def thirdMax(self, nums):

        list = []
        for id in nums:  # 去重
            if id not in list:
                list.append(id)
        list.sort(reverse=True)  # 降序排列
        if len(list) <= 2:
            return max(list)
        else:
            return list[2]

# class Solution:
#     def thirdMax(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums1=list(set(nums))
#         if len(nums1)<3:
#             return max(nums1)
#         nums1.sort(reverse=1)
#         return nums1[2]
if __name__ == '__main__':
    nums1 = [2, 2, 3, 1]
    a = Solution()
    p = a.thirdMax(nums1)
    print(p)
    nums2 = [2, 2]
    #a = Solution()
    q = a.thirdMax(nums2)
    print(q)
    nums3 = [1,2,3,4,5,6,7,8,9,0]
    #a = Solution()
    m = a.thirdMax(nums3)
    print(m)
    nums4 = [0,0,0,0]
    #a = Solution()
    n = a.thirdMax(nums4)
    print(n)