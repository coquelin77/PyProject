def binary_search(arr, start, end, hkey):
    while start <= end:
        mid = start + int((end - start) / 2)
        if arr[mid] < hkey:
            start = mid + 1
        elif arr[mid] > hkey:
            end = mid - 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    lis = [-1, 0, 1, 2, 3, 3, 4, 4, 5, 10]
    print(binary_search(lis, 0, len(lis)-1, 2))
