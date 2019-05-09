'''给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]'''
# class Solution(object):
#     def twoSum(self,nums,target):
#         for i in range(0,len(nums)-1):#从数组第一个元素遍历
#             for j in range(i+1,len(nums)):#搭配后面每一个元素
#                 if(nums[i]+nums[j]==target):#如果和等于target就返回数组下标
#                     l=[]
#                     l.append(i+1)
#                     l.append(j+1)
#                     return l
class Solution(object):
    def twoSum(self,nums,target):
        dict = {}
        sums=[]

        for i in range(0, len(nums)):
            a = target-nums[i]
            if a in dict:
                sums.append(dict[a])
                sums.append(i)
                return sums
            else:
                dict[nums[i]]=i
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    a =Solution()
    print(a.twoSum(nums,target))


