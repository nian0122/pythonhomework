# s = input("请输入字符串：")
# res = ""
# for str in s:
#     if str >= 'a' and str <= 'z':
#         res += str.upper()
#     elif str >= 'A' and str <= 'Z':
#         res += str.lower()
#     else:
#         res += str
# print(res)
class Zhuanghuan:
    def __init__(self,str):
        self.str=str
    def daxiaoxiezhuanghuan(self):
        res = ""
        for str in self.str:
            if str >= 'a' and str <= 'z':
                res += str.upper()
            elif str >= 'A' and str <= 'Z':
                res += str.lower()
            else:
                res += str
        return res
if __name__ == '__main__':
    str=Zhuanghuan("dfsfad")
    print(str.daxiaoxiezhuanghuan())