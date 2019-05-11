def bubble_sort(nums):
    l = len(nums) - 1
    for i in range(l):
        count = 0
        for j in range(l - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                count += 1
        if 0 == count:
            break


if __name__ == '__main__':
    li = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print("原列表为：%s" % li)
    bubble_sort(nums=li)
    print("新列表为：%s" % li)
