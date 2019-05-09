import time


class limit(object):
    def alpha(self, limit):
        start = time.perf_counter()  # 记录开始的时间
        while True:
            limit -= 1  # 循环一次limit-1
            if limit <= 0:  # 如果limit减到0
                delta = time.perf_counter() - start  # 算出结束-开始的时间
                return delta  # 返回这个值


if __name__ == '__main__':
    a = limit()
    limit = 10 * 1000 * 1000
    p = a.alpha(limit)
    print('程序运行时间是', p)
