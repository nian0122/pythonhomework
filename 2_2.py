d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
i = int(input("请输入"))
a = d.get(i, "输入的键不存在！")
print(a)
