def binary_search(hkey, nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < hkey:
            low = mid + 1
        elif nums[mid] > hkey:
            high = mid - 1
        else:
            return mid



if __name__ == '__main__':
    a = [1, 3, 4, 5, 6, 7, 8]
    key = 3
    n = binary_search(nums=a, hkey=key)
    print(n)