##### abc.图形抽象基类设计
```python
from abc import ABC, abstractmethod

# 继承抽象基类ABC来定义抽象基类Shape
class Shape(ABC):
    @abstractmethod  # 抽象方法 用于计算面积
    def area(self):
        pass
    
    @abstractmethod  # 抽象方法 用于计算周长
    def perimeter(self): 
        pass

# 定义子类 Circle，实现基类中定义的抽象方法
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# 定义子类 Rectangle，实现基类中定义的抽象方法
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# 子类实例化
circle = Circle(5)
rectangle = Rectangle(4, 6)


print(f"Circle Area: {circle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

# 继承顺序
Circle.__mro__  #  (__main__.Circle, __main__.Shape, abc.ABC, object)
```