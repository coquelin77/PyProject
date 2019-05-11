def binary_search(nums,start,end,hkey):
	if start > end:
		return -1
	mid = start + (end - start) // 2
	if nums[mid] > hkey:
		return binary_search(nums, start, mid - 1, hkey)
	if nums[mid] < hkey:
		return binary_search(nums, mid + 1, end, hkey)
	return mid

if __name__ == '__main__':
    a = [1, 3, 4, 5, 6, 7, 8]
    key = 3
    low = 0
    high=len(a)-1
    n = binary_search(nums=a, hkey=key,start=low,end=high)
    print(n)
