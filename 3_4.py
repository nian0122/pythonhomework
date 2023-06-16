def fun(i):
    n = 0
    while i >= 1:
        i /= 10
        n += 1
    return n
for i in range(1, 1001):
    a = i
    n = fun(i)
    sum = 0
    while i >= 1:
        g = i % 10
        sum += g ** n
        i /= 10
        i = int(i)
    if a == sum:
        print("水仙花数:{0}".format(a),end="  ")
