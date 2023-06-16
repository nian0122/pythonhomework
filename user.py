"""新建user.py文件，
编写User类，包含用户姓名、性别、密码属性，
并编写一个名为login的登录方法，
打印输出一行字符串”User login success!”。"""
class User:
    def __init__(self, name, gender, password):
        self.name = name
        self.gender = gender
        self.password = password

    def login(self):
        print("User login success!")
if __name__ == '__main__':
    user=User('xiao','nan',90)
    user.login()
