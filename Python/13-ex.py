# 专门定义数据变量，存放已经注册的用户信息
userdict = {} # 用于接收所有用户和密码的字典
userlist = [] # 用于接收所有用户名的列表
blackUserList = [] # 定义一个小黑屋专用列表

# 定义一个读取所有用户数据的函数
def readAllUsers():
    # 读取所有的注册信息
    with open('./data/user.txt', 'a+', encoding="utf-8") as fp:
        global userdict
        global userlist
        fp.seek(0,0) # 调整指针到文件头
        res = fp.readlines() # 按照每一行读取所有用户数据
        for i in res: # 循环读取每一行数据
            r = i.strip() # 处理每一行尾部的换行符
            mydict = r.split(':')
            userdict.update({mydict[0]:mydict[1]})
            userlist = userdict.keys()

    # 读取所有黑名单用户
    with open('./data/black.txt', 'a+', encoding='utf-8') as fp:
        global blackUserList
        fp.seek(0,0)
        res = fp.readlines()
        for i in res:
            r = i.strip() #
            blackUserList.append(r)

# 封装一个函数 完成注册功能
def register():
    # 定义一个变量，用于控制外循环
    site = True
    # 执行循环， 用户名操作
    while site:
        # 用户输入用户名
        username = input('欢迎注册，请输入用户名：')

        # 用户名需要检测是否已经存在
        if username in userlist:
            print('当前用户已经存在，请更换用户名。')
        else:
            # 利用循环，都正确的时候结束循环。
            while True:
                # 用户输入密码
                password = input('请输入您的密码: ')
                
                # 检测密码长度不能低于6位
                if len(password) >= 6:
                    # 请确认您的密码
                    re_password = input('请再输入一次您的密码: ')
                    # 检测密码和确认密码是否一致
                    if re_password == password:
                        # 用户名和密码都正确，可以写入文件
                        # 打开文件，写入数据
                        with open('./data/user.txt', 'a+', encoding='UTF-8') as fp:
                            fp.write(f'{username}:{password}\n')
                        print(f'注册成功：用户名:{username}')
                        # 结束循环
                        # 结束外循环
                        site = False
                        # 结束内循环
                        break
                    else:
                        print('两次输入的密码不同，请重新输入。', username, password, re_password)

                # 密码长度不够
                else:
                    print('密码格式不正确：', username, password)


# 封装登录函数
def login():
    
    # 自定义变量, 控制登录外循环
    isLogin = True
    # 定义变量，用来记录用户输入密码错误次数
    errorNum = 3

    # 创建循环
    while isLogin:

        # 获取用户登录时输入的用户名
        username = input('欢迎登录，请输入您的用户名：')
        
        # 检测当前用户名是否存在
        if username in blackUserList:
            print('您的账户已经被锁定，并且还未给管理员上供品。')
            isLogin = False # 结束外循环
        elif username in userlist:
            while True:
                # 让用户输入密码
                pwd = input('请输入您的密码：')
                # 检测用户输入的密码是否正确
                if pwd == userdict[username]:
                    print(pwd)
                    isLogin = False # 结束外循环
                    break # 结束内循环
                else:
                    # 密码错误，修改变量次数
                    errorNum -= 1
                    # 判断当前密码错误次数
                    if errorNum == 0:
                        print('给你机会你不中用啊细狗。账户已锁定，请联系管理人员并上供品。')
                        # 锁定当前账户，把锁定的用户拉入黑名单
                        with open('./data/black.txt', 'a+', encoding='UTF-8') as fp:
                            fp.write(username+'\n')
                        isLogin = False
                        break
                    else:
                        print(f'您的密码输入有误, 您还能再尝试{errorNum}次。')
        else:
            # 用户名不存在
            print('用户名错误，亲重新输入')

# 判断当前脚本是否作为一个主进程脚本在执行
if __name__ == '__main__':
    '''
    这里的代码，只有在使用Python解释器直接运行时才会执行
    如果当前脚本作为了模块被其他文件导入后使用，那么这个地方的代码不会执行
    因此这个地方的代码，适合写当前脚本中的一些测试，这样不会影响其他脚本
    '''
    # 调用初始化方法，加载数据
    readAllUsers()
    
    isBegin = True
    while isBegin:
        myStr = '''
        ======================
        ** 登录（0） 注册（1）**
        ======================
        '''
        print(myStr)

        # 让用户选择对应的操作
        num = input('请输入对应的序号，体验功能：')
        if num == '0':
            login()
            isBegin = False
        elif num == '1':
            register()
            isBegin = False
        else:
            print('后续功能还在开发中。')
            isBegin = False