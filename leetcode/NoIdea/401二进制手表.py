'''二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。



例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
案例:

输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]


注意事项:

输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。


'''


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for i in range(5):
            if i > num:
                break
            res1 = []
            self.hour_dfs(i, 3, 0, res1)
            res2 = []
            self.minute_dfs(num - i, 5, 0, res2)
            for k in res1:
                for r in res2:
                    res.append('{}:{}'.format(k, r))
        return res

    def hour_dfs(self, count, cur_index, out, res):
        # count 剩余led灯的数量
        # cur_index 当前遍历到的灯的索引 3 2 1 0
        if count == cur_index + 1:
            temp = (1 << (cur_index + 1)) - 1 + out
            if temp >= 12:
                return
            res.append(temp)
            return
        elif count > cur_index + 1:
            return
        elif count == 0:
            if out >= 12:
                return
            res.append(out)
            return
        else:
            self.hour_dfs(count, cur_index - 1, out, res)
            self.hour_dfs(count - 1, cur_index - 1, out + (1 << cur_index), res)

    def minute_dfs(self, count, cur_index, out, res):
        # count 剩余led灯的数量
        # cur_index 当前遍历到的灯的索引 3 2 1 0
        if count == cur_index + 1:
            temp = (1 << (cur_index + 1)) - 1 + out
            if temp >= 60:
                return
            if temp < 10:
                temp = '0' + str(temp)
            res.append(temp)
            return
        elif count > cur_index + 1:
            return
        elif count == 0:
            if out >= 60:
                return
            if out < 10:
                out = '0' + str(out)
            res.append(out)
            return
        else:
            self.minute_dfs(count, cur_index - 1, out, res)
            self.minute_dfs(count - 1, cur_index - 1, out + (1 << cur_index), res)


if __name__ == '__main__':
    n = 3
    a = Solution()
    p=a.readBinaryWatch(n)
    print(p)