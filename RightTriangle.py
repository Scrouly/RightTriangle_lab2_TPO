from math import sqrt, pow


class RightTriangle:
    def __init__(self, a, b):
        if a <= 0:
            raise Exception("leg value must be greater than 0")
        else:
            self.a = a
        if b <= 0:
            raise Exception("leg value must be greater than 0")
        else:
            self.b = b
        self.values = []

    def hypotenuse(self):
        c = sqrt(pow(self.a, 2) + pow(self.b, 2))
        return c

    def perimeter(self):
        p = self.a + self.b + self.hypotenuse()
        return p

    def triangle_values(self):
        self.values.append(self.hypotenuse())
        self.values.append(self.perimeter())
        return self.values


triangle = RightTriangle(1, -2.43)
print(triangle.triangle_values())
