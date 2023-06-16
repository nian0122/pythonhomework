"""编写程序，创建类用Cube ，
分别计算柱体的表面积和体积。输入l=1，w=2，h=3，
运行效果如图2所示"""
class Cube:
    def __init__(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
    def surface(self):
        s=(self.l*self.w+self.l*self.h+self.w*self.h)*2
        print("the surface of cube is {}".format(s))
    def volume(self):
        v=self.l*self.w*self.h
        print("the volume cubeis {}".format(v))
cube=Cube(1,2,3)
cube.surface()
cube.volume()

