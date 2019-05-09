'''给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
示例 2:

输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
'''


# class Solution:
#     def nextGreaterElement(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
#         l=[]
#         for i in range(0,len(nums1)-1):
#             for j in range(i+1,len(nums2)-1):
#                 if nums2[j]>nums1[i]:
#                     l.append(nums2[j])
#                     break
#                 else:
#                     l.append(-1)
#         return l
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        l = []
        d = dict()

        for n2 in nums2:
            while len(l) and l[-1] < n2:
                d[l.pop()] = n2
            l.append(n2)

        for i1 in range(len(nums1)):
            nums1[i1] = d.get(nums1[i1], -1)

        return nums1
if __name__ == '__main__':
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    nums3 = [4, 1, 2]
    nums4 = [1, 3, 4, 2]
    a = Solution()
    p = a.nextGreaterElement(nums1,nums2)
    q = a.nextGreaterElement(nums3,nums4)
    print(p,q)