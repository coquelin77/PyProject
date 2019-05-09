def insert_sort(lst):
    n = len(lst)
    if n == 1: return lst
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:break
    return lst


lst = [10, 4, 1, 0, -1, 2, 3, 4, 3, 5]
print(insert_sort(lst))
