class none():
    def total(self, n):
        l = []

        for i in range(1,n+1):
            l.append(i * i)
        return l
if __name__ == '__main__':
    n=100
    a=none()
    p=a.total(n)
    print(p)