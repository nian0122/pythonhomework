"""新建admin.py文件，
导入模块user中的User类，编写Admin类继承User类，
并添加新的权限属性privilege，重写login登录方法，
打印输出一行字符串”Admin login success!”。"""
from user import User
class Admin(User):
    def __init__(self, username, password, email, privilege):
        super().__init__(username, password, email)
        self.privilege = privilege
    def login(self):
        super().login()
        print("Admin login success!")
user=Admin('xiao','nan',90,90)
user.login()