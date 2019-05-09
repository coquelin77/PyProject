if __name__ == '__main__':
    li=[1,4,5,6,8]
    for i in range(1,len(li)-1):
        li.append(li.pop(-i))
    print(li)