def insert_sort(lst):
    n = len(lst)
    if n == 1: return lst
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break
    return lst

#拿 一个元素出来插入到第一个比它小的后面
if __name__ == '__main__':
    l = [2, 3, 5, 6, 1, 9, 8, 7]
    a = insert_sort(l)
    print(a)
