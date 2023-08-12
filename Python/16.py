'''
Author: Hivan Du
mail: doo@hivan.me
LastEditors: Hivan Du
LastEditTime: 2023-08-13 02:21:44
'''
# 封装函数，用于输出日历信息
import calendar, time, os
def showdate(year, month):
    res = calendar.monthrange(year, month)

    days = res[1] # 当前月份的天数
    week = res[0] + 1 # 当前月份第一天是周几

    print(f'========= {year} 年  {month} 月 =========')
    print('一   二    三   四   五    六   日')
    print('='*32)
    # 实现日历信息的输出
    d = 1
    while d <= days:
        # 循环周
        for i in range(1, 8):
            # 判断是否输出
            if d > days or (d==1 and i<week):
                print('     ', end='')
            else:
                print('{:0>2d}'.format(d), end="   ")
                d+=1
        print()

dd = time.localtime()
year = dd.tm_year
month = dd.tm_mon

while True:
    os.system('clear')
    # 默认输出当前年月的日历信息
    showdate(year, month)
    print(' < 上一月     下一月 > ')
    c = input('请输入您的选择 "<" or ">"：')
    # 判断用户的输入内容
    if c == '<':
        month -= 1
        if month < 1:
            month = 12
            year -= 1
    elif c == '>':
        month += 1
        if month > 12:
            month = 1
            year += 1
    elif c == 'exit':
        break
    else:
        print('您输入内容错误，请重新输入"<"或者">"来选择。')