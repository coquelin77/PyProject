def binary_search(hkey, nums):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = start + (end - start)//2
        if hkey > nums[mid]:
            start = mid + 1
        elif hkey < nums[mid]:
            end = mid - 1
        else:
            return mid


if __name__ == '__main__':
    li = [1, 3, 4, 6, 8, 12, 14, 15]
    hotkey = 3
    a = binary_search(hkey=hotkey, nums=li)
    print(a)