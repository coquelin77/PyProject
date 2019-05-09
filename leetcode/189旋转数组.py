'''给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]'''


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k != 0:
            i = nums[-1]
            nums.insert(0, nums.pop(-1))
            k = k - 1
        return nums


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6, 7]
    n = 3
    a = Solution()
    print(a.rotate(s, n))
# if __name__ == '__main__':
#     k =3
#     nums =[1,2,3,4,5,6,7]
#     swap = nums[~k:-1]
#     nums.insert(0,swap)
#     print(nums)
# if __name__ == '__main__':
#     k=3
#     k=~k
#     nums=[1,2,3,4,5,6,7]
#     for k in nums:
#