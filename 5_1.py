"""约数。完成一个名为 getfactors(n) 的函数。
它接受一个整数作为参数, 返回它所有约数的列表, 包括 1 和它本身。
运行效果参见图5_1"""
def getfactors(n):
    divisor=[1]
    for i in range(2,n+1):
        if n%i==0:
            divisor.append(i)
    print("divisor:",divisor)
n=int(input("Enter a number:"))
getfactors(n)
