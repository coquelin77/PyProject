# '''给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]
# 说明:
#
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
# '''
#
#
# class Solution:
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#
#
#         """
#
#         i = 0
#         j = 0
#         result = []
#         while i < len(nums1) and j < len(nums2):
#             if (nums1[i] > nums2[j]):
#                 # result.append(group2[j])
#                 j = j + 1
#             elif (nums1[i] < nums2[j]):
#                 # result.append(group1[i])
#                 i = i + 1
#             elif (nums1[i] == nums2[j]):
#                 result.append(nums1[i])
#                 i = i + 1
#                 j = j + 1
#             result=list(set(result))
#         return result
#
#     def selectSoft(nums1, nums2):
#         for i in range(0, len(nums1) - 1):
#             index = i
#             for j in range(i + 1, len(nums1)):
#                 if nums1[index] > nums1[j]:
#                     index = j
#             nums1[i], nums1[index] = nums1[index], nums1[i]
#
#         for i in range(0, len(nums2) - 1):
#             index = i
#             for j in range(i + 1, len(nums2)):
#                 if nums2[index] > nums2[j]:
#                     index = j
#             nums2[i], nums2[index] = nums2[index], nums2[i]
#         return nums1, nums2
#
#
# if __name__ == '__main__':
#     group1 = [1, 2, 2, 1]
#     group2 = [2, 2]
#     a = Solution()
#     p = a.intersection(group1, group2)
#     print(p)
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    a = Solution()
    n1 = [4, 9, 5]
    n2 = [9, 4, 9, 8, 4]
    p=a.intersection(n1,n2)
    print(p)