'''给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        numDict = {}
        for i in range(len(nums)):  # xrange在网页上好使
            if nums[i] in numDict and i - numDict[nums[i]] <= k:
                return True
            else:
                numDict[nums[i]] = i
        return False


if __name__ == '__main__':
    s = [1, 2, 3, 1]
    n = 3
    a = Solution()
    print(a.containsNearbyDuplicate(s, n))
