##### super()
- `super( subclass , object )`
	- 用于调用父类的一个方法，指的是[[py.内置特殊属性|内置特殊属性]] `__mro__`中的下一个父类。
	- `subclass`：要调用父类方法的子类
	- `object`：子类的实例或子类本身
	- 在方法中 `super().method(arg)` 和 `super(class, self).method(arg)` 相同
```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super(B, self).greet()  # 调用父类 A 的 greet 方法
        print("Hello from B")

class C(A):
    def greet(self):
        super(C, self).greet()  # 调用父类 A 的 greet 方法
        print("Hello from C")

class D(B, C):
    def greet(self):
        super(D, self).greet()  # 调用父类 B 的 greet 方法
        print("Hello from D")

# super().greet() 和 super(D, self).greet() 相同

d = D()
d.greet()
# Hello from A
# Hello from C
# Hello from B
# Hello from D

super(D, d).greet()
# Hello from A
# Hello from C
# Hello from B

D.__mro__
# (__main__.D, __main__.B, __main__.C, __main__.A, object)
# D -> B -> C -> A
# 调用顺序为 A -> B -> C -> D
```