def quicksort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quicksort(lst, lo, p)
        quicksort(lst, p+1, hi)
    return

def partition(lst, lo, hi):
    pivot = lst[hi-1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[hi-1] < lst[i+1]:
        lst[i+1], lst[hi-1] = lst[hi-1], lst[i+1]
    return i+1
lst = [10, 4, 1, 0, -1, 2, 3, 4, 3, 5]
print(quicksort(lst,0,len(lst)-1))