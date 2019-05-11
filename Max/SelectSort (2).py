def selectSoft(nums):
    for i in range(0, len(nums) - 1):
        index = i
        for j in range(i + 1, len(nums)):
            if nums[index] > nums[j]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
    return nums


nums = [10, 4, 1, 0, -1, 2, 3, 4, 3, 5]
print(selectSoft(nums))
