group1 = [1,2,4,6,7,8]
group2 = [1,3,4,7,9]
result=[]
i=0
j=0
while i< len(group1) and j<len(group2):
    if (group1[i] > group2[j]):
        result.append(group1[i])
        j = j + 1
    elif (group1[i] < group2[j]):
        result.append(group1[i])
        i = i + 1
    elif (group1[i] == group2[j]):
        result.append(group1[i])
        i = i + 1
        j = j + 1
while i<len(group1) and j==len(group2):
    result.append(group1[i])
    i=i+1
while i==len(group1) and j<len(group2):
    result.append(group2[j])
    j=j+1
print(result)