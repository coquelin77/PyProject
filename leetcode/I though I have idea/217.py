class Solution:
    def containsDuplicate(self, nums):
        nums_single = set(nums)
        if len(nums)!=len(nums_single):
            return True
        return False
if __name__ == '__main__':
    nums1=[1,2,3,4,4,5,6,6,6,7,7,8,8,8,8,8,9]
    nums2=[1,2,3,4,5,8,9]
    a=Solution()
    p=a.containsDuplicate(nums=nums1)
    q=a.containsDuplicate(nums=nums2)
    print(p,q)