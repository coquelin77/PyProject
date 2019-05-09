import os
import time
with open('/Users/zhangyiming/Downloads/demo.txt', 'a') as f:
    f.write(str(time.time()) + '\n')

with open('/Users/zhangyiming/Downloads/demo.txt', 'r') as f:
    print(f.read())
