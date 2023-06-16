"""设计一个三维向量类Vector3D，
包含三维向量的一些基本运算，
如加法、减法以及点乘、叉乘。
如v1 = (1, 2, 3)，v2 = (4, 5, 6)，
运行效果如图1所示。"""
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("三维向量相加:\n", v1 + v2)
print("三维向量相减:\n", v1 - v2)
print("三维向量点乘:\n", v1.dot(v2))
print("三维向量叉乘:\n", v1.cross(v2))
