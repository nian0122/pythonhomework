"""编写程序，实现在磁盘上建立一个文件，并从键盘上写入内容，写完后关闭文件。再打开文件，把文件的内容打印到屏幕上。运行效果如图2所示。"""

with open('text.txt',mode='w',encoding='utf-8') as file:
    file = open("test.txt", "w")
    text = input("请输入内容：")
    file.write(text)
    file.close()


file = open("test.txt", "r")
print(file.read())
file.close()