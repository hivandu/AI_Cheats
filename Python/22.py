'''
Author: Hivan Du
mail: doo@hivan.me
LastEditors: Hivan Du
LastEditTime: 2023-08-17 21:17:44
'''
# 魔术方法
# 定义一个人
class Person():

    # 构造方法
    def __new__(cls, *args, **kwargs):
        print(args)
        # print(kwargs)
        print(cls)
        return object.__new__(cls)

    # 初始化方法
    def __init__(self, name, age, sex):
        print('触发初始化方法:__init__')
        self.name = name
        self.age = age
        self.sex = sex

    def __call__(slef, *args, **kwargs):
        print('你把对象当成了函数进行调用。')

    # 析构方法
    def __del__(self):
        print('触发了析构方法:__del__')

# 实例化对象
zs = Person('张三丰', 210, '男')
print(zs)
zs()