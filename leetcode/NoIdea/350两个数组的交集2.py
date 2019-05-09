class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        sorted(nums1)
        sorted(nums2)


if __name__ == '__main__':

    nums1 = [1, 2, 2, 2, 1]
    nums2 = [2, 2, 1, 2, 2]
    #at this time n1=1,1,2,2,2     n2=1,2,2,2,2
    sorted(nums1)
    sorted(nums2)
    result = []
    i=j=0
    if len(nums1) > len(nums2):
        print()
    elif len(nums1) < len(nums2):
        print()
    elif len(nums1) == len(nums2):
        while i<=len(nums1) or j<=len(nums2):
            if nums1[i]==nums2[j]:
                result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]>nums2[j]:
                j+=1
            elif nums1[i]>nums2[j]:
                i+=1
    # nums1 = [1, 2, 2, 2, 1]
    # nums2 = [2, 2, 1, 2,1]
    # sorted(nums1)
    # sorted(nums2)
    # for i in nums1:
    #     for j in nums2:
    #         if i==j:
    #             result.append(i)
    #             i+=1
    #             j+=1

    # at this time nums1=1,1,2,2,2 nums2=1,2,2,2
    # for i in range(0,len(nums1)):
    #     for j in range(0,len(nums2)):
    #         if nums1[i]==nums2[j]:
    #             result.append(nums1[i])
    #         elif nums1[i]>nums2[j]:
    #             j=j+1
    #         elif nums1[i]<nums2[j]:
    #             i=i+1

    print(result)
