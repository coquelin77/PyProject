'''在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。



示例 1：

输入：[1,2,3,3]
输出：3
示例 2：

输入：[2,1,2,5,3,2]
输出：2
示例 3：

输入：[5,1,5,2,5,3,5,4]
输出：5'''
nums = [5, 1, 5, 2, 5, 3, 5, 4]
numset = set(nums)
print(numset)
for i in range(0 len(nums)-1):
    if
# class Solution(object):
#     def repeatedNTimes(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """


# if __name__ == '__main__':
#     nums = [5, 1, 5, 2, 5, 3, 5, 4]
#     N = len(nums)/2
#     p = 1
#     for i in range(0, len(nums)-1):
#         for j in range(i+1, len(nums)-1):
#             if i == j:
#                 p = p+1
#                 if p == N:
#                     print(p)
