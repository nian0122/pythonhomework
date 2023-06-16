"""编写程序，实现手机号的验证。验证规则如下：长度必须为11位，前2位是13、15或18，后9位都是数字。运行效果如下（运行两次，分别输入13912345678和11912345678）：
	第1次运行：
输入一个手机号：13912345678
13912345678 是一个合法的手机号
	第2次运行：
输入一个手机号：v
11912345678 不是一个合法的手机号
"""
"""while True:
    phone_number = input("输入一个手机号：")
    if len(phone_number) != 11:
        print(phone_number, "不是一个合法的手机号")

    elif not phone_number[:2] in ["13", "15", "18"]:
        print(phone_number, "不是一个合法的手机号")
    elif not phone_number[2:].isdigit():
        print(phone_number, "不是一个合法的手机号")
    else:
        print(phone_number, "是一个合法的手机号")
    break"""
import re
while True:
    phone = input("输入一个手机号：")
    SERCH=r'^1[358]\d{9}$'
    if re.match(SERCH, phone):
        print(phone, "是一个合法的手机号")
    else:
        print(phone, "不是一个合法的手机号")