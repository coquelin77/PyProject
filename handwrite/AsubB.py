
def setSub(group1, group2):

    result=[]
    i=0
    j=0
    while i< len(group1) and j<len(group2):
        if (group1[i] > group2[j]):
            #result.append(group1[i])
            j = j + 1
        elif (group1[i] < group2[j]):
            result.append(group1[i])
            i = i + 1
        elif (group1[i] == group2[j]):
            #result.append(group1[i])
            i = i + 1
            j = j + 1
    while i<len(group1) and j==len(group2):
        result.append(group1[i])
        i=i+1
    return result

if __name__ == '__main__':

    print(setSub([1, 2, 4, 6, 7, 8], [1, 3, 4, 7, 9]))
    print(setSub([-2,1,2,3], [-2,3,5]))
    print(setSub([1,2,3], [2]))
    print(setSub([2], [1,2,3]))
    print(setSub([1,2,3], [7,8,9,10,11]))
    print(setSub([1,2,3,4,5], [8,9]))
    print(setSub([], [1,2]))
    print(setSub([2,3], []))