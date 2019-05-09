import time

if __name__ == '__main__':
    print('请输入身高(m)')
    # 体质指数（BMI）=体重（kg）÷身高^2（m）
    a = float(input())
    print('你输入的是', a)
    print('请输入体重(kg)')
    b = float(input())
    print('你输入的是', b)
    BMI = b / (a * a)
    print('.')
    time.sleep(.5)
    print('.')
    time.sleep(.5)
    print('.')
    print('你的BMI指数是', BMI)
