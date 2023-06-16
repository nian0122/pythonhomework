import random
while 1:
    computer = int(random.randint(0, 2))
    if computer == 0:
        computer = "石头"
    elif computer == 1:
        computer = "剪刀"
    elif computer == 2:
        computer = "布"
    player = int(input("可用的选择有：\n（0）石头\n（1）剪刀\n（2）布\n请选择对应的数字："))
    dot = {0: "石头", 1: "剪刀", 2: "布"}
    i = dot.get(player)
    if player not in range(0, 3):
        print("无效的选择，请选择 0/1/2")
    elif computer == i:
        print(str.format("请选择对应的数字：{0}\n您选择了：{1}\n计算机选择了：{2}\n平局，要不再来一局！", player, i, computer))
    elif (computer == "石头" and i == "剪刀") or (computer == "剪刀" and i == "布") or (computer == "布" and i == "石头"):
        print(str.format("请选择对应的数字：{0}\n您选择了：{1}\n计算机选择了：{2}\n输了，游戏结束！", player, i, computer))
        break
    else:
        print(str.format("请选择对应的数字：{0}\n您选择了：{1}\n计算机选择了：{2}\n恭喜，你赢了！", player, i, computer))

