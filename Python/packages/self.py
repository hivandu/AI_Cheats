'''
Author: Hivan Du
mail: doo@hivan.me
LastEditors: Hivan Du
LastEditTime: 2023-08-14 22:25:30
'''
# My.py

# 定义类
class MyException():
    pass

# 定义函数
def func():
    print('我是一个模块中的func函数')

# 定义变量
myStr = 'iloveyou'

name = __name__
print(f'__name__: {name}')

if __name__ == '__main__':
	  print('这个位置的代码只有当前脚本被直接运行时才会运行。')