def square(x):
　　return x**2

if __name__ == '__main__':

    res=map(square,[1,2,3,4,5])
    res=[i for i in res if i>10]
    print(res)