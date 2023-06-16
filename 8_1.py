"""编写程序，
将字符串“Hello Python”、“BigDate”、“SQL”存入到文件“data.dat”中并读出显示。"""


with open('data.dat',mode='r+',encoding='utf-8') as file:
    file.write('“Hello Python”、“BigDate”、“SQL”')
    file.close()
    file=open("data.dat",mode='r+',encoding='utf-8')
    str=file.read()
    print(str)