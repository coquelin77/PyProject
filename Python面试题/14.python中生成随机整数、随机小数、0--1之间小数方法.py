import random
import numpy as np

res = random.randint(10, 30)
res1 = np.random.randn(5)
res2 = random.random()
print('随机整数：', res)
#随机整数： 20
print('5个随机小数：', res1)
#5个随机小数： [1.01618007 2.05695795 1.00978217 - 0.2845249 - 0.63788356]
print('0-1随机小数：', res2)
#0 - 1随机小数： 0.07391688288336429

# {随机整数：random.randint(a, b), 生成区间内的整数
# 随机小数：习惯用numpy库，利用np.random.randn(5)
# 生成5个随机小数
# 0 - 1
# 随机小数：random.random(), 括号中不传参}