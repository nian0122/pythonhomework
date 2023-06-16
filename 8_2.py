"""编写程序，
实现读取一个英文文本文件内容，
将文本中的大写字母转换为小写字母，小写字母转换为大写字母。
运行效果如图1所示。"""
s="kserygfalhdbvljLGLHVLYGljhvjhvVLJGLJHVLJLljh"
from s4_1 import Zhuanghuan
with open('str.dat',mode='r+',encoding='utf-8') as f:
    f.write(s)
    f.close()
    f=open('str.dat',mode='r+',encoding='utf-8')
    str=f.read()
    a=Zhuanghuan(str)
    print(a.daxiaoxiezhuanghuan())