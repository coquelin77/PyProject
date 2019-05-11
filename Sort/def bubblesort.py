def bubblesort(nums):
    l = len(nums) - 1
    for i in range(l):
            for j in range(l-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]


if __name__ == '__main__':
    li = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print("原列表为：%s" % li)
    bubblesort(nums=li)
    print("新列表为：%s" % li)
