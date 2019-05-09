'''977. 有序数组的平方
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
 '''


class Solution:
    def sortedSquares(self, A):
        for e in range(0,len(A-1)):
            if A[e] < 0 :
                abs(A[e])
if __name__ == '__main__':
    nums=[-4, -1, 0, 3, 10]
    a=Solution()
    p=a.sortedSquares(nums)
    print(p)