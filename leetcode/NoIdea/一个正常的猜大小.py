import random


class guess:
    def LargeOrless(self, n):
        num = random.randint(1, 100)
        while True:
            if n > num:
                print("多了")
            elif n < num:
                print("少了")
            elif n == num:
                print("对了"+"正确答案是"+str(n))
                return n
            else:
                print("错了")


if __name__ == '__main__':
    a = guess()

    for i in range(1, 100):
        n = i
        a.LargeOrless(n)
