"""Fibonacci 数列。 Fibonacci 数列指的是这样一个数列：1、1、2、3、5、8、13、21、……
在数学上，Fibonacci 数列以如下被以递归的方法定义：
F0=1，F1=1，Fn=F(n-1)+F(n-2)（n>=2，n∈N*）。
写一个函数fib（n）, 给定整数 N ,输出前 N 个 Fibonacci 数字。
运行效果参见图5_3。"""
def fib(n):
        if n==1:
            return 1
        elif n==2:
            return 1
        else:
            return fib(n-2)+fib(n-1)
n=int(input("请输入你想输出多少个斐波那契数列元素:"))
for i in range(1,n+1):
    print(fib(i))