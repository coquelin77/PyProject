# class Solution:


# def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#
#         start = 0
#         end = len(nums)
#         arr = nums
#         hkey=target
#         while start <= end:
#             mid = start + int((end - start) / 2)
#             if arr[mid] < hkey:
#                 start = mid + 1
#             elif arr[mid] > hkey:
#                 end = mid - 1
#             else:
#                 return mid
#         return -1
#
#
# def search(self, nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     low = 0
#     high = len(nums) - 1
#     mid = (low + high) / 2
#     while low <= high:
#         mid = (low + high) / 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target in nums:
            return nums.index(target)
        else:
            return -1


if __name__ == '__main__':
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    a = Solution()
    p = a.search(nums1, target1)
    q = a.search(nums2, target2)
    print(p, q)
