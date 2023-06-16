"""阶乘。 编写代码，定义一个求阶乘的函数fact(n)，要求输入N, 返回 N! 的值。运行效果参见图5_2。"""
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
N=int(input("请输入阶乘数字:"))
print(fact(N))